Title: Server Setup Basics

URL Source: https://becomesovran.com/blog/server-setup-basics.html

Markdown Content:
This is a post I've been meaning to do for a while. While it's simple to explain how to set up an app for self-hosting, it's pointless to host an app on a weak foundation. It's a massive pain in my ass to start every how to with a section on server setup, so I'm also making this post for myself as a reference on how I like to set up a server for apps I'm hosting. I'll start with basic stuff like proper login with SSH and non-root user set up and making users for each app. I'll also touch on NGINX setup, some quality of life tools that make server management easier, log management and basic network security.  
‍

*   [SSH](https://becomesovran.com/blog/server-setup-basics.html#ssh)
*   [Users](https://becomesovran.com/blog/server-setup-basics.html#users)
*   [Logs](https://becomesovran.com/blog/server-setup-basics.html#logs)
*   [Backups](https://becomesovran.com/blog/server-setup-basics.html#backups)
*   [Basic Network Safety](https://becomesovran.com/blog/server-setup-basics.html#network)
*   [NGINX](https://becomesovran.com/blog/server-setup-basics.html#nginx)
*   [Quality of Life Tools](https://becomesovran.com/blog/server-setup-basics.html#qol)
*   [DNS](https://becomesovran.com/blog/server-setup-basics.html#dns)
*   [Docker](https://becomesovran.com/blog/server-setup-basics.html#docker)

SSH


-----

First is login. You’ll need a way to access your device securely. Don't even mess with username and password. You want to use SSH (Secure Shell) and make sure that SSH is the only way to log in. To do that, you’ll need an SSH key and a new user account. On a newly provisioned VPS, you'll be logged in as root, and you want to protect the root account. First off on the VPS or remote machine make a new regular user with and add them to the “sudo” group with:

```
sudo adduser newuser

sudo usermod -aG sudo newuser
```

Now on your local machine run:

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Follow the instructions, it should ask you where you want to save the file and if you want a password or not. Make sure you set a string one. To copy the public key over to your server run on your local machine:

```
ssh-copy-id -i ~/.ssh/id_ed25519.pub newuser@your_server_ip
```

Keep in mind newuser@your-server-ip is the username and the remote device you are trying to copy your public key into. When you get prompted for a password, it will be the password for the account on the remote device, NOT the password you just made for the SSH key. Once verified, it will copy over the public key, and you can now log in Via SSH. To turn off username and password login, type in:  
‍

```
sudo nano /etc/ssh/sshd_config
```

Find these values and set them as you see them here.  
‍

```
Port 2222     # Change default port (use a number between 1024 and 65535)
PermitRootLogin no                 # Disable root login
PasswordAuthentication no          # Disable password authentication
PubkeyAuthentication yes           # Enable public key authentication
AuthorizedKeysFile .ssh/authorized_keys # Specify authorized_keys file location
AllowUsers newuser                 # Only allow specific users to login
```

This disallows every login method besides SSH under the user you copied your public key to. Stops login as Root and only allows the user you specify to log in. Hit CTL+S to save and CTL+x to get out of the file editor. Restart SSH:  
‍

```
sudo service ssh restart
```

This might boot you out of the session. If it does, this is a good time to test the other login methods to see if they are declined before continuing. Also, it should go without saying, but you need to keep the private key safe and if you lose it you will not be able to get in remotely anymore.You can further lock down your login with:  
‍

```
Protocol 2                 # Use only SSH protocol version 2
MaxAuthTries 3             # Limit authentication attempts
ClientAliveInterval 300    # Client alive interval in seconds
ClientAliveCountMax 2      # Maximum client alive count
```

Now, let's dive into users a bit more and see how we can leverage them for a bit of organization and security.

Users


-------

Users are important when it comes to managing a Linux server. There is an idea in server management called the “Principle of The Least Privilege” this basically means that you want to give an app or process the minimum amount of privileges that it needs to do its job. Root has unlimited power, and no app really needs this. Making a user for apps that you're running accomplishes a few things. It can limit potential damage if an application you are running is compromised. It adds isolation when running more than one app, it helps with auditing so you know what app is using what system resources.

In short, users are a great way of helping organize your system and helps you troubleshoot if and when things go wrong. To add a new user, run:  
‍

```
sudo useradd -rms /usr/sbin/nologin -c "a comment" youruser
```

This command makes a user and gives them a home directory for app data but does not allow login as the user. The -c flag is optional, but It's nice to know what the user is for, like “Running Nextcloud” or whatever. Clone app files into the /opt directory with:  
‍

```
sudo mkdir /opt/myapp
```

This command makes a user and gives them a home directory for app data but does not allow login as the user. The -c flag is optional, but It's nice to know what the user is for, like “Running Nextcloud” or whatever. Clone app files into the /opt directory with:  
‍

```
sudo chown appuser:appuser /opt/myapp
```

Ok, with this your login is locked down, and you should have a decent idea about how to use users. Next is logs.  
‍

**Logs

**
----------

Logs are crucial to system administration. They keep track of system health, help troubleshoot issues and detect threats. So you want to set up proper log rotation so they do not take up too much space on your system, plus are easier to read and manage. To set up proper log rotation, you want to edit the logrotate.conf file located in /etc. Individual application configurations are typically stored in /etc/logrotate.d/, so an example configuration for NGINX would look like:  
‍

```
/var/log/nginx/*.log {
    weekly
    missingok
    rotate 52
    compress
    delaycompress
    notifempty
    create 0640 www-data adm
    sharedscripts
    postrotate
        [ -f /var/run/nginx.pid ] && kill -USR1 `cat /var/run/nginx.pid`
    endscript
}
```

This configuration rotates logs weekly, keeps 52 weeks of logs, compresses old logs, makes new logs with the right permissions and then signals NGINX to reopen log files after rotation. You can test it with:

```
sudo logrotate -d /etc/logrotate.conf
```

This will show what it will do without actually rotating logs. With this all set up, you can start to do more advanced stuff like triggering alerts based on log entries. Now this is good for a single server but if you manage more than one server it's a good idea to look into tools like Grafana Loki, Graylog and Fluentd. I won't go into detail here, but if you're looking to up your log game, these a decent place to start.  
‍

**Backups

**
-------------

Backups, and more importantly, testing your backups, are extremely important in server management. Remember: a backup is not a backup unless you test it. Untested backups are essentially useless.

There are three main types of backups. Full, Differential, Incremental. Full backups are a complete copy of all data on a disk. Takes the most resources, but is the easiest to restore from. Differential backups back up all the changes since the last full backup, it's a middle ground strategy for backups on both space and restoration speed. An incremental backup backs up data that was changed since the last backup, this is the fastest backup option but can be the most complex to restore.

I think of it like this. I use incremental backups for things like photos and documents or project files and folders that get edited a lot. I'll use a full backup for backing up and entire server or disk. Differential backups Ill use for backing up full folders like /etc, /opt and log folders.

Now what about storage? If you follow the 3-2-1 rule, you will be golden. 3 copies of your data, 2 storage types, and 1 offsite backup. I'd say if this seems like too much, the “offsite” storage is the most important and not one to skip. In case of a catastrophic meltdown, having a hard disk with your backups is invaluable. Offsite / offline backups can also save your ass from ransomware. So keep that in mind. There is a huge amount of backup software out there. [This link](https://github.com/awesome-foss/awesome-sysadmin#backups) is for exploring some more professional backup tools. [This link](https://github.com/awesome-selfhosted/awesome-selfhosted?tab=readme-ov-file#file-transfer--synchronization) has file sync, transfer and could storage solutions. I use a combo of sync-thing, Borg backup and good old-fashioned FTP.

Remember, that backup, logs and server monitoring is an evolving process based on your needs. The specific strategy you implement should be tailored to your needs and the criticality of your data.

**Basic Network Safety

**
--------------------------

The next step in securing a server is to lock down ports that need don’t need to be exposed to the internet and banning things that try to log in when they should not. UFW and Fail2Ban are two tools that are in widespread use for this. They are simple and easy to use, UFW lets you set traffic rules for ports and Fail2Ban will ban and IP address when it knocks on a port they should not be or if they fail to log in after some predefined rules. UFW or uncomplicated firewall often comes preinstalled on a lot of VPS services, same with Fail2Ban, but if you are on a new machine and you're unsure, run:  
‍

```
sudo apt install ufw

sudo apt install fail2ban
```

### **  
UFW**

We will worry about Fail2Ban later, for now let's focus on UFW setup. First run some default policys with:

```
sudo ufw default deny incoming
 
sudo ufw allow outgoing
```

This is considered best practice, as it follows the “the least privileges” idea I touched on earlier. It reduces attack surface on your machine and gives you precise control over what you do expose. In short, this configuration creates a balance between security and functionality. Your server can reach out to the internet as needed, but external entities can only connect to your server in ways you've explicitly allowed. Now let's allow some stuff in.  
‍

```
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
```

If you are going to be running a web server, you need port 80 and port 443 open. 80 is HTTP and 443 is HTTPS. By default, port 22 is SSH, if you changed this you need to specify the port instead of using the “allow ssh” command. Here are some other useful commands:  
‍

```
#List rules with numbers:
sudo ufw status numbered
#Delete by number:
sudo ufw delete NUMBER
#Delete by rule specification:
sudo ufw delete allow 80
#You can allow connections from specific IP addresses:
sudo ufw allow from 192.168.1.100
#You can also only allow an IP to connect to a specfic port with: 
sudo ufw allow from 192.168.1.100 to any port 22
#If you neeed to allow a range of ports: 
sudo ufw allow 6000:6007/tcp
#To further protect from brut force attacks you can rate limit specific ports with: 
sudo ufw limit ssh
#This would limit port 22 to 6 connections in 30 seconds from a single IP. To see the status of the firewall you can use: 

#Adding this goves you more info
sudo ufw status verbose
#and to reset incase you need to start over: 
sudo ufw reset
#and to enable and disable: 
sudo ufw enable 
sudo ufw disable 

#finaly to enable logging and adjusting the log level: 
sudo ufw logging on
sudo ufw logging medium # levels are low, medium, high, full 
```

On to Fail2Ban now.

### **  
Fail2Ban**

‍  
The main configuration is located in /etc/fail2ban/jail.conf, but it's recommended to create a local configuration file:  
‍

```
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

sudo nano /etc/fail2ban/jail.local
```

‍  
There are some basic settings in the \[DEFAULT\] section of the jail.local section those are:  
‍

```
bantime = 10m
findtime = 10m
maxretry = 5
```

‍  
Ban time is how long an IP is banned. Find time is the time frame in witch Fail2Ban looks for repeated failure, and max retry is the number of failures before an IP is banned. You can tune these as you see fit. There are also custom jails you can set, Fail2Ban also supports jails for commonly used services like SSH. There are even more steps you can take, but I think this covers the basics.

### **NGINX

**

There are a small mess of web servers out there that you can use. Apache, Caddy, nginx, IIS to name a few. I use Nginx. It's what I know, and it works really damn well. Nginx (pronounced engine-x) is a web server, reverse proxy, and load balancer. As a web server, it excels at serving static content and can handle loads of concurrent connections with fairly low resource usage. As a reverse proxy, it can sit in front of your application servers and forward traffic to them while enchaining the apps' security. Its load balancing aspects can effectively balance traffic between servers, improving reliability and scalability.

When installed via apt, the default location for nginx is /etc/nginx/ the nginx.conf is mostly used for global server configuration and includes filed from the /etc/nginx/sites-enabled folder. This modular structure allows for easy management of multiple sites. Two folders to be aware of are the sites-enabled folder and the sites-available folders. You can think of the sites available as a staging place to test your site configurations, while the sites enabled is for live sites and apps. A common practice is to set up and test your configuration in the sites in the sites available, then when you're ready to go live and get an SSL cert, you link the file to the sites-enabled folder. You do that with:  
‍

```
ln -s /etc/nginx/sites-available/yoursitefile /etc/nginx/sites-enabled
```

Then reload nginx and double check nginx status with:  
‍

```
sudo systemctl reload nginx

sudo systemctl status nginx
```

Your site should be live now.

Below, I’ll show you some boilerplate Nginx site configurations. Be sure to look into your app or sites needs as these are just starting points. For static sites, this is a decent starting point.

Basic Static Website Configuration:

```
server {
    listen 80;
    listen [::]:80;
    server_name example.com www.example.com;
    root /var/www/example.com/html;
    index index.html index.htm;
    location / {
        try_files $uri $uri/ =404;
    }
    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

    # Logging
    access_log /var/log/nginx/example.com.access.log;
    error_log /var/log/nginx/example.com.error.log warn;

    # SSL configuration (uncomment after running Certbot)
    # listen 443 ssl http2;
    # listen [::]:443 ssl http2;
    # ssl_protocols TLSv1.2 TLSv1.3;
    # ssl_prefer_server_ciphers on;
    # ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;

    # Certbot will add its own SSL certificate paths
    # ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    # ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
}
```

Proxy Pass Configuration:

```
server {
    listen 80;
    listen [::]:80;
    server_name app.example.com;
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

    # Logging
    access_log /var/log/nginx/app.example.com.access.log;
    error_log /var/log/nginx/app.example.com.error.log warn;

    # SSL configuration (uncomment after running Certbot)
    # listen 443 ssl http2;
    # listen [::]:443 ssl http2;
    # ssl_protocols TLSv1.2 TLSv1.3;
    # ssl_prefer_server_ciphers on;
    # ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;

    # Certbot will add its own SSL certificate paths
    # ssl_certificate /etc/letsencrypt/live/app.example.com/fullchain.pem;
    # ssl_certificate_key /etc/letsencrypt/live/app.example.com/privkey.pem;
}
```

WebSocket Upgrade Configuration:

```
server {
    listen 80;
    listen [::]:80;
    server_name ws.example.com;
    location / {
        proxy_pass http://localhost:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

    # WebSocket timeout settings
    proxy_read_timeout 300s;
    proxy_send_timeout 300s;
    # Logging
    access_log /var/log/nginx/ws.example.com.access.log;
    error_log /var/log/nginx/ws.example.com.error.log warn;

    # SSL configuration (uncomment after running Certbot)
    # listen 443 ssl http2;
    # listen [::]:443 ssl http2;
    # ssl_protocols TLSv1.2 TLSv1.3;
    # ssl_prefer_server_ciphers on;
    # ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;

    # Certbot will add its own SSL certificate paths
    # ssl_certificate /etc/letsencrypt/live/ws.example.com/fullchain.pem;
    # ssl_certificate_key /etc/letsencrypt/live/ws.example.com/privkey.pem;
}
```

The basic configuration is for serving a simple static site. It specifies the domain name, listens on port 80 for both IPv4 and IPv6, sets the root directory for the site, configures error handling with try\_files, adds some basic headers that protect from common web vulnerabilities, sets up logging for access and errors and includes a section for SSL that is commented out. Most of the SSL config will be handled by certbot, but there are a few lines in there that add some SSL security that can be uncommented after certbot is ran.  
‍  
The proxy pass configuration is similar to the basic configuration, but instead of serving files directly, it proxies requests to a local application (in this case, running on port 3000).

The third configuration file is geared towards apps that need website connections, it's a lot like the proxy pass configuration with some changes to allow web sockets.

Ok, any bit about web servers is not really complete without talking about SSL. For casual use, certbot is a pleb's best friend. It's free, it is fast, and it fucking works. I use the python version of certbot. You can install that with:    
‍

```
sudo apt install certbot python3-certbot-nginx
```

Once it's installed you can simply run “certbot” in your terminal, this will detect the configs in your sites-enabled folder and ask what you want to do (renew, reissue, etc…). Follow the walk-through, certbot gives you It's pretty straight forward.  
‍  
So nowadays certbot when getting a new cert will set up auto-renew for you, so it's a sit-and-forget kinda task. But to make sure it worked you can run:

```
sudo systemctl status certbot.timer
```

if this is up and running, you should be good to go if you're using systemd.  
‍

**Quality Of Life Tools

**
---------------------------

On the topic of tools that make managing your system easier, I'm going to present some tools I use on my servers that I think make management just a bit nicer. Not going to do a deep dive on any tool. All of these are optional and in no particular order. A lot of these I found on the site [terminal trove](https://terminaltrove.com/), a great site to browse if you're a terminal junkie like me.

First tool, [Btop](https://terminaltrove.com/btop/) this is in my personal must haves list. Btop is a terminal monitor of resources. It shows you real time visuals of usage stats for your box’s CPU, RAM, disks, network and running possesses it's written in C++ and can be installed via most package managers.

For servers that have a lot of outside connections, i.e. a nostr relay, a tool like [Neoss](https://terminaltrove.com/neoss/) is helpful. Neoss aims to replace usual ss command for basic usage. It provides a list of in use TCP and UDP sockets with their respective stats. Its main advantage over SS raw output is its clear and simple TUI (terminal user interface) that allows you to sort, refresh and navigate what is connected to your machine. It's installed Via NPM, meaning you need JavaScript installed.

[GoAccess](https://github.com/allinurl/goaccess) is a terminal based log analyzer for web servers. It's great for a quick real time look at logs while in the terminal, but it can also generate real time HTML, JSON, and CSV reports. GoAccess can be installed via most package managers, works on all platforms.

Next on the list is [MC or “midnight commander”](https://terminaltrove.com/mc/) Its a powerful text based file manager with a two panel display and lots of features for manipulating files and directories. It's also cross-platform and can be installed via most package managers.

In the same thread of server file management is [NCDU](https://dev.yorhel.nl/ncdu). This one is in my must-have list. It is a disk usage analyzer that is designed to find space hogs. It's fast and very simple to use. It can be installed on most systems and package managers. Windows will need Linux subsystems installed to use it.

Hopefully you find some use out of these. The last topic I'd like to touch on is DNS it's a bit topic, so I'm not going to do a massive deep dive, but if you're self-hosting it helps to have some of the basics of DNS down. ing doesn’t work.

**DNS

**
---------

DNS or The Domain Name System is a core part of how the internet as we know it works. Love it or hate it, it's what we have to work with If you want to be accessible to the wider internet. (I dislike what it currently is it, but I’m not opening that can of worms here.) Basically, Think of DNS like a phone book. It’s what allows you to type duckduckgo.com instead of “52.250.42.157” every time you need to search the internet. It translates something easy for humans to remember into the information needed by computers to actually reach “duckduckgo.com”

If you're hosting on a VPS, the only thing you really need to know is to know how to point an A record at your server's IP after you decide on a domain to use. Pretty much all VPS hosts can give you a static IP, so that's mostly a set and forget type deal.

Hosting from home presents some challenges. One prominent one is (and a valid question that I often hear) not having a static IP address. Nowadays with the number of devices online needing IP addresses we do a lot of juggling, and most IP addresses are assigned dynamically unless you pay for it from your ISP.  But there is a solution. The answer to this is called Dynamic DNS or DDNS. This allows automatic updating of DNS servers every time an IP address changes. There are a mess of ways to set up dynamic DNS. You can host your own service or use a host. [Here is a link](https://dynamic.domains/dynamic-dns/providers-list/default.aspx) with some hosts and projects to check out.

In a nutshell, it works like so. You chose a provider or set up your own. You get a domain, install the client on your home router or server and the client periodically checks to see if the IP address has changed, if so it updates your DNS record for that domain.

**Docker

**
------------

I'm not gonna cover how to install docker here. It's best to follow [the official installation](https://docs.docker.com/engine/install/debian/) guide anyway. But I want to touch on a few things. First off, docker is useful as hell for testing new apps. But that's about as far as I take it. I personally do not like using docker all that much, and where possible run applications directly. Here are some pros and cons to keep in mind.

### **Docker Pros**

Consistency is a big one it can make things more constant between development, testing, and deploying if your system can run docker you can run most docker apps. It can help with isolation, reducing conflicts between apps. In some cases it can help with efficiency as it takes less resources than traditional VM’s. It can help with scaling as it's pretty easy to spin up more containers and the microservice architecture can be useful because you can break down an application into smaller manageable services, allowing for independent scaling of said services. Lastly the community is large, so the documentation is good, and community support is always helpful, plus there is a wide range of ready to go docker images for deployment.

### **Docker Cons**

I’ll start with overhead. While it's better than a traditional VM, it uses more resources than running something directly on the host, and I/O operations can be slower. The fact that docker shares the system's kernel means that a compromised app could affect the system. Persistent data is doable but adds a layer of complexity that can cause data loss with new users, it also makes backups more complex. Networking can also be more complex with docker, making it not as straightforward. It's also good to note that if you use UFW or firewalld for a firewall, docker bypasses those rules. Docker is only compatible with iptables. Also, while a well managed docker container can help manage server resources, an improperly manged on can be detrimental to resources as well. Containers can get too large, effecting disk size, and misconfiguration can use too many of your servers resources. It also adds extra layers of complexity when monitoring and debugging applications, especially across multiple containers.

At the end of the day, it's your system. But I wanted to lay out some pros and cons when it comes to using Docker. Moving on.

**Wrap Up

**
-------------

Well, that about does it for the basics of server setup and tools. There is a [a script that I wrote](https://git.sovbit.dev/Enki/sovran-scripts) that will do most of this for you. I wrote it to make my own server setup faster. You can get that here, it includes all of my must-haves and does some basic configuration. Tweak it to your own needs, and as always stay safe out there and ping me on nostr or simplex if you have questions or if I fucked something up in this post.
