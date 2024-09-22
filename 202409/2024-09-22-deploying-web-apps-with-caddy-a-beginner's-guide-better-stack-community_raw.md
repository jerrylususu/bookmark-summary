Title: Deploying Web Apps with Caddy: A Beginner's Guide | Better Stack Community

URL Source: https://betterstack.com/community/guides/web-servers/caddy/

Markdown Content:
[Caddy](https://caddyserver.com/) is an open-source web server written in Go and built with the aim of simplifying the process of running and deploying web applications by offering a rich set of features and a unique and simplified approach to web server configuration, setting it apart from predecessors such as Apache or Nginx.

With its automatic HTTPS setup and easy-to-use Caddyfile configuration, the need to learn another sophisticated configuration language or deal with complicated TLS certificate management is eliminated. Additionally, Caddy's built-in support for [HTTP/3](https://www.cloudflare.com/learning/performance/what-is-http3/) makes it a highly efficient and future-proof choice for deploying web applications.

Caddy has zero runtime dependencies, ensuring easy installation and operation across various platforms with a minimal footprint. It can handle reverse proxying with load balancing, caching, circuit breaking, and health checks. Additionally, it provides plugin support for extending its functionality even further.

These features make Caddy a robust, enterprise-ready web server suitable for developers of all levels. Whether you're a beginner or an experienced developer, Caddy provides a seamless and hassle-free experience, allowing you to focus on developing your application rather than managing your server.

In this article, we will explore some of the most popular features that Caddy has to offer, such as serving static files and proxying specific requests to internal application backends. We will also delve further into its ability to handle HTTPS automatically and discuss its potential integrations with observability tools for log management and uptime monitoring.

Let's dive right in.

Prerequisites
-------------

*   Basic command-line skills.
*   A recent version of [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your system.
*   Current user configured to [manage Docker as non-root](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) to avoid having to prefix `docker` commands with `sudo`.
*   Git installed on your system (`apt install git`) for cloning the repositories containing example code.
*   Tree installed on your system (`apt install tree`) for easier listing of directory contents.
*   (Optional) A domain name for following along the HTTPS setup examples.

Step 1 — Running Caddy server with Docker
-----------------------------------------

The easiest way to get started with Caddy server is by using the [official Docker image](https://hub.docker.com/_/caddy) and running Caddy as a Docker container. This ensures a seamless installation process that is also quite simple to reproduce across different systems.

To begin, execute the following command:

```
docker run --rm -p 80:80 caddy
```

Caddy will become accessible as soon as you see the following message in your terminal:

```
{"level":"info","ts":1699614997.5182397,"msg":"serving initial configuration"}
```

You can then open `http://localhost` in your browser, and you should see the default "Caddy works!" page, indicating that it is up and ready to handle web traffic:

This is all it takes to get started.

The `docker run` command you executed started a new Docker container running Caddy. It also mapped port 80 on your local machine to port 80 in the container so the server can become accessible from your browser at `http://localhost`.

The `--rm` flag instructed the Docker engine to remove the container once you're done working with it, just to help keep your system clean while experimenting with all the different configuration settings that you are about to explore.

I intentionally omitted the `-d` flag in the command to leave the container running in foreground mode, so that it is easier for you to examine the logs emitted upon startup, as they carry valuable information for understanding how the default Docker image is organized.

Let's have a look at the logs. The very first line says:

```
{"level":"info","ts":1699254136.4679956,"msg":"using provided configuration","config_file":"/etc/caddy/Caddyfile","config_adapter":"caddyfile"}
```

This indicates that the Caddy server instance running inside the container loads its configuration from whatever file is mounted at `/etc/caddy/Caddyfile`. The image ships with a default `Caddyfile` containing the minimum configuration settings needed to get things going. To customize it, you can mount a custom configuration file at `/etc/caddy/Caddyfile`, overriding the default one.

A couple of lines below, you can see:

```
{"level":"warn","ts":1699254136.4689212,"logger":"http.auto_https","msg":"server is listening only on the HTTP port, so no automatic HTTPS will be applied to this server","server_name":"srv0","http_port":80}
```

This indicates the supplied `Caddyfile` does not enable HTTPS by default. Therefore, you have to tweak the configuration to enable TLS, as you will see in a moment.

Finally, there are the messages:

```
{"level":"info","ts":1699254136.4690306,"logger":"tls","msg":"cleaning storage unit","description":"FileStorage:/data/caddy"}
```

```
{"level":"info","ts":1699254136.4692078,"msg":"autosaved config (load with --resume flag)","file":"/config/caddy/autosave.json"}
```

These reveal that Caddy stores runtime data like TLS certificates, private keys, and OCSP staples in the `/data` folder and keeps its most recent configuration state in the `/config` folder inside the running container.

Such data is not meant to be ephemeral, so I highly recommend that you use mounted volumes for these folders to avoid losing your configuration or having to reissue SSL certificates every time the container restarts.

Putting all of these together, we can conclude that there is no need to modify the original Docker image to tailor the Caddy container to your specific needs.

It can all be done at runtime by crafting the right set of `docker` commands for starting the container. Since issuing individual `docker` commands can prove to be laborious and error-prone, it is preferable to use a tool such as Docker Compose to streamline this process.

Hit `Ctrl+C` to stop the Caddy container and return to the command prompt. You should see something like:

```
^C{"level":"info","ts":1699609912.4189968,"msg":"shutting down","signal":"SIGINT"}
{"level":"warn","ts":1699609912.419042,"msg":"exiting; byeee!! 👋","signal":"SIGINT"}
{"level":"info","ts":1699609912.419472,"logger":"http","msg":"servers shutting down with eternal grace period"}
{"level":"info","ts":1699609912.4202948,"logger":"admin","msg":"stopped previous server","address":"localhost:2019"}
{"level":"info","ts":1699609912.4203057,"msg":"shutdown complete","signal":"SIGINT","exit_code":0}
```

Let's quickly create a new folder and `cd` into it to draft a `docker-compose.yml` and a custom `Caddyfile`:

```
mkdir caddy-tutorial && cd caddy-tutorial
```

Create a new `Caddyfile` with the following contents:

```
:80 {
    root * /usr/share/caddy
    file_server
}
```

This configuration instructs Caddy to look up the `/usr/share/caddy` folder inside the Docker container for an `index.html` file and serve this file over HTTP.

Create the following dummy `index.html` file:

```
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>Hello, Caddy!</title>
</head>
<body>
    <p>Hello, Caddy!</p>
</body>
</html>
```

The idea is to mount this file into `/usr/share/caddy` to display its contents when opening `http://localhost` from a browser.

Finally, create a `docker-compose.yml`:

docker-compose.yml

Copied!

```
version: '3'

name: caddy-tutorial

services:
  caddy:
    container_name: caddy
    image: caddy
    restart: always
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - caddy-config:/config
      - caddy-data:/data
      - ./Caddyfile:/etc/caddy/Caddyfile
      - ./index.html:/usr/share/caddy/index.html

volumes:
  caddy-config:
  caddy-data:
```

This file is slightly longer than the others, but its contents are straightforward. It defines two persistent volumes named `caddy-config` and `caddy-data`, mounting them to the `/config` and `/data` folders inside the Caddy container to persist the state of your web server.

Furthermore, it mounts the `Caddyfile` and the `index.html` you just created to their appropriate locations inside the container. Lastly, it exposes ports `80` and `443` to enable access to your web server on `localhost` through HTTP and HTTPS respectively.

List the contents of your current folder:

If everything is correct, you should see the following files:

```
total 12
-rw-rw-r-- 1 marin marin 164 Nov 10 13:03 Caddyfile
-rw-rw-r-- 1 marin marin 302 Nov 10 13:05 docker-compose.yml
-rw-rw-r-- 1 marin marin 188 Nov 10 13:04 index.html
```

You can now go ahead and start the Caddy container through Docker Compose:

```
[+] Running 1/1
 ✔ Container caddy-tutorial-caddy-1  Started
```

Now open `http://localhost` again and you should see "Hello, Caddy!":

If, for some reason, you see an error message when running `docker compose up` instead, make sure that there aren't any other running applications already using ports 80 or 443:

```
Error response from daemon: driver failed programming external connectivity on endpoint caddy (b555101cb58677dc7e017d23747f326a978a6ea920955d3131432d700a5e843f): Bind for 0.0.0.0:80 failed: port is already allocated
```

At this point, everything should be working correctly, and you can shut down the Caddy container before continuing further:

```
[+] Running 2/2
 ✔ Container caddy-tutorial-caddy-1  Removed    0.4s
 ✔ Network caddy-tutorial_default    Removed    0.4s
```

Step 2 — Setting up HTTPS with Caddy
------------------------------------

One of the coolest features that Caddy has to offer is its ability to automatically provision and renew TLS certificates for you after a small initial setup. This renders obsolete the need to remember complicated commands or go through a lengthy verification process for obtaining and installing certificates.

By declaring your domain name inside your `Caddyfile`, Caddy takes over and does all the provisioning work for you automatically.

You need to own a domain name to see how this works in practice. Throughout this article, we will refer to the domain name that you own as `<your_domain_name>`. To follow along with the examples below, ensure to replace `<your_domain_name>` with the actual domain that you own (e.g., `example.com`).

Point `<your_domain_name>` to the machine that your Caddy container is running on, ensuring that there are no firewalls blocking traffic on ports 80 and 443 (e.g., if you are behind a router, make sure that ports 80 and 443 are open and traffic is forwarded properly to your machine).

To verify that this is the case, start the Caddy server and try accessing it through your domain name:

Assuming your DNS and networking settings are correct, you should see the "Hello, Caddy!" page when typing in `<your_domain_name>` in your browser:

Before you can proceed with setting up the certificate, it is worth noting the state of the `/data` folder inside the Caddy container. Issue the following command to list its contents:

```
docker container exec caddy ls -l /data/caddy
```

You can see that the `/data/caddy` folder is currently empty. This will change soon when the TLS certificate gets provisioned.

Go ahead and stop the container:

Then modify the `Caddyfile` as follows:

```
<your_domain_name> {
    root * /usr/share/caddy
    file_server
}
```

Here, you are simply replacing the `:80` binding with the full name of your domain. You can now restart the Caddy container, but this time omit the `-d` flag to observe the logs emitted by the certificate provisioning process.

After the server initializes, you will see the following set of messages indicating that a new certificate has been provisioned:

```
caddy  | {"level":"info","ts":1699618884.7067113,"logger":"tls.obtain","msg":"acquiring lock","identifier":"<your_domain_name>"}
caddy  | {"level":"info","ts":1699618884.7076728,"logger":"tls.obtain","msg":"lock acquired","identifier":"<your_domain_name>"}
caddy  | {"level":"info","ts":1699618884.707749,"logger":"tls.obtain","msg":"obtaining certificate","identifier":"<your_domain_name>"}
caddy  | {"level":"info","ts":1699618884.7086315,"logger":"http","msg":"waiting on internal rate limiter","identifiers":["<your_domain_name>"],"ca":"https://acme-v02.api.letsencrypt.org/directory","account":""}
caddy  | {"level":"info","ts":1699618884.7086391,"logger":"http","msg":"done waiting on internal rate limiter","identifiers":["<your_domain_name>"],"ca":"https://acme-v02.api.letsencrypt.org/directory","account":""}
caddy  | {"level":"info","ts":1699618885.8201177,"logger":"http.acme_client","msg":"authorization finalized","identifier":"<your_domain_name>","authz_status":"valid"}
caddy  | {"level":"info","ts":1699618885.8201704,"logger":"http.acme_client","msg":"validations succeeded; finalizing order","order":"https://acme-v02.api.letsencrypt.org/acme/order/1406393766/221214636416"}
caddy  | {"level":"info","ts":1699618886.933485,"logger":"http.acme_client","msg":"successfully downloaded available certificate chains","count":2,"first_url":"https://acme-v02.api.letsencrypt.org/acme/cert/0439041a395e765fd31f5cd2b7d1e92fe056"}
caddy  | {"level":"info","ts":1699618886.9343963,"logger":"tls.obtain","msg":"certificate obtained successfully","identifier":"<your_domain_name>"}
caddy  | {"level":"info","ts":1699618886.9346375,"logger":"tls.obtain","msg":"releasing lock","identifier":"<your_domain_name>"}
```

Now, if you try to open `<your_domain_name>` in a browser, you should see the "Hello, Caddy!" page loaded successfully over HTTPS:

Here, your Caddy instance contacted the Let's Encrypt certificate authority, obtained a new certificate, and installed it on the web server.

Before you power down the container, open a new terminal and check the contents of the `/data/caddy` folder in the container once again.

```
docker container exec caddy ls -l /data/caddy
```

```
total 16
drwx------  3 root  root    4096 Nov 10 12:20 acme
drwx------  3 root  root    4096 Nov 10 12:21 certificates
drwx------  2 root  root    4096 Nov 10 12:21 locks
drwx------  2 root  root    4096 Nov 10 12:21 ocsp
```

As you can see, the folder is no longer empty. It contains all the necessary files for serving, provisioning, and renewing certificates.

Apart from provisioning new certificates, Caddy also runs an automated certificate renewal process in the background, eliminating the need to manually renew certificates or worry about expiration dates.

As long as Caddy is up and running, a renewal is triggered for each certificate as soon as it passes about 2/3 of its lifetime. Caddy automatically fetches, installs, and enables the new certificate without stopping to serve requests, so it incurs no downtime for your clients.

Whenever a TLS certificate is installed, Caddy also takes care to redirect all HTTP traffic to the HTTPS endpoint automatically for you, ensuring that all communications between the client and the server are secure by default.

Step 3 — Using Caddy as a static file server
--------------------------------------------

One of the most common use cases for Caddy is as a static file server, and more precisely, as a web server for hosting single-page applications created with frameworks such as React, Vue, or Angular.

You already mounted a dummy `index.html` into the `/usr/share/caddy` folder of your Caddy container, so technically, you're already using Caddy as a static file server.

However, SPA frameworks usually ship with an internal routing component, allowing for client-side navigation within the application. To properly serve these applications, you will most certainly need to configure Caddy to redirect all incoming requests to a main `index.html` file, allowing the SPA router to take over and handle the routing internally.

To illustrate this, let's use a basic [example React application](https://github.com/betterstack-community/caddy-react-app).

Clone the application from GitHub and change into the project directory:

```
git clone https://github.com/betterstack-community/caddy-react-app.git
```

You already have Docker installed, so to avoid downloading any additional dependencies related to Node.js, you can build the application with Docker using the following one-liner:

```
docker run -it --rm -v .:/workdir --workdir /workdir --user $(id -u):$(id -g) node:20 /bin/bash -c "npm install && npm run build"
```

This command mounts the contents of the `caddy-react-app` directory inside a Docker container running the latest LTS version of Node.js, retaining the current user and group permissions. It then issues `npm install` followed by a `npm run build` inside the container to build the application.

If everything goes okay, you should see an output similar to:

```
dist/index.html                   0.41 kB │ gzip:   0.28 kB
dist/assets/index-1eb968c3.css  232.27 kB │ gzip:  31.10 kB
dist/assets/index-1a72bdb1.js   410.87 kB │ gzip: 127.99 kB
✓ built in 2.48s
```

This indicates that the application was built successfully and compiled assets were placed inside the `/dist` folder.

Copy the contents of the `dist` folder to the `caddy-tutorial` folder that you created earlier:

```
cp -r dist/ <your_caddy_tutorial_folder>
```

Now move into your `caddy-tutorial` folder and list its contents:

```
cd <your_caddy_tutorial_folder> && tree
```

If everything is okay, you should see a similar output:

```
.
├── Caddyfile
├── dist
│   ├── assets
│   │   ├── index-1a72bdb1.js
│   │   └── index-1eb968c3.css
│   └── index.html
├── docker-compose.yml
└── index.html

2 directories, 6 files
```

It's now time to modify your `Caddyfile` and mount the contents of the `dist` folder in place of the `index.html` that you had mounted before. To do this, change the last line in your `volumes` declaration from `./index.html:/usr/share/caddy/index.html` to `./dist:/usr/share/caddy`.

The updated `docker-compose.yml` file should now look like this:

docker-compose.yml

Copied!

```
version: '3'

name: caddy-tutorial

services:
  caddy:
    container_name: caddy
    image: caddy
    restart: always
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - caddy-config:/config
      - caddy-data:/data
      - ./Caddyfile:/etc/caddy/Caddyfile
      - ./dist:/usr/share/caddy

volumes:
  caddy-config:
  caddy-data:
```

Now start Caddy:

When you open up `<your_domain_name>` in a browser, you should see the example React application loaded up:

When you click around and navigate to one of the internal pages, it may appear that routing already works correctly, as the URI changes and the corresponding page is loaded accordingly:

However, try hitting the refresh button or typing in `<your_domain_name>/about` directly in the address bar of your browser, and you will notice the following:

What happened? The React Router gave you the illusion that separate requests were being made to the web server. In reality, the routing only occurs on the client side, so when you refresh or directly type in a URL, Caddy doesn't recognize the route and returns a 404 error.

This is precisely why you must redirect all incoming requests to the main `index.html` file of the application. To do this, open up your `Caddyfile` and add a `try_files` directive as follows:

```
:80 {
    root * /usr/share/caddy
    file_server
    try_files {path} /index.html
}
```

The `try_files` directive instructs Caddy to rewrite all request URIs to the application's main `index.html`:

Now restart Caddy:

Refresh the error page, or type `<your_domain_name>/about` directly in your browser's address bar. This time, the page will be displayed properly and no error will be returned:

Finally, try typing in the address of a page that doesn't exist. For example `<your_domain_name>/foo`. Since all request URIs redirect to `index.html` this will let the React application invoke its internal 404 handler and display a user-friendly not found page:

That's all that it takes to prepare Caddy for serving the front-end of your single-page applications.

Step 4 — Setting up request logging with Caddy
----------------------------------------------

In the previous example, you successfully navigated through the example React application, yet at one point, you also encountered an unexpected "404 Not Found" error. Let's check the logs from the Caddy container to see if there are any messages indicating this error:

Surprisingly, not only are there no messages indicating an error, but there are also no messages suggesting that any requests were made at all:

```
caddy  | {"level":"info","ts":1699964271.9924734,"msg":"autosaved config (load with --resume flag)","file":"/config/caddy/autosave.json"}
caddy  | {"level":"info","ts":1699964271.9926255,"msg":"serving initial configuration"}
caddy  | {"level":"info","ts":1699964271.994773,"logger":"tls.cache.maintenance","msg":"started background certificate maintenance","cache":"0xc0004b6780"}
caddy  | {"level":"info","ts":1699964271.994943,"logger":"tls","msg":"cleaning storage unit","description":"FileStorage:/data/caddy"}
caddy  | {"level":"info","ts":1699964271.9964683,"logger":"tls","msg":"finished cleaning storage units"}
```

The reason behind this is that the default Caddy configuration doesn't activate logging out of the box. To enable logging, add the line `output stdout` to your `Caddyfile`. This instruction tells Caddy to log all incoming requests to the standard output.

Your `Caddyfile` should then become:

```
<your_domain_name> {
  root * /usr/share/caddy
  file_server
  try_files {path} /index.html
  log {
    output stdout
  }
}
```

Save the file and restart the Caddy container:

Now, tail the Caddy logs by issuing:

Open `<your_domain_name>` in a browser, and you will start seeing the request logs appearing in your terminal:

```
caddy  | {"level":"info","ts":1699966070.0058851,"logger":"http.log.access.log0","msg":"handled request","request":{"remote_ip":"62.73.122.237","remote_port":"54834","client_ip":"62.73.122.237","proto":"HTTP/2.0","method":"GET","host":"<your_domain_name>","uri":"/assets/index-1eb968c3.css","headers":{"If-None-Match":["\"s444rz4z7z\""],"If-Modified-Since":["Tue, 14 Nov 2023 12:16:47 GMT"],"Sec-Gpc":["1"],"Sec-Fetch-Dest":["style"],"User-Agent":["Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"],"Sec-Ch-Ua-Platform":["\"Linux\""],"Sec-Ch-Ua-Mobile":["?0"],"Accept-Encoding":["gzip, deflate, br"],"Sec-Ch-Ua":["\"Brave\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\""],"Accept":["text/css,*/*;q=0.1"],"Accept-Language":["en-US,en;q=0.8"],"Sec-Fetch-Site":["same-origin"],"Sec-Fetch-Mode":["no-cors"],"Referer":["https://<your_domain_name>/"]},"tls":{"resumed":false,"version":772,"cipher_suite":4865,"proto":"h2","server_name":"<your_domain_name>"}},"bytes_read":0,"user_id":"","duration":0.000236047,"size":0,"status":304,"resp_headers":{"Server":["Caddy"],"Alt-Svc":["h3=\":443\"; ma=2592000"],"Etag":["\"s444rz4z7z\""]}}
```

Naturally, there are better options than viewing logs from the terminal. It's far from optimal—analyzing large amounts of data can be time-consuming and difficult, and it's easy to miss identifying patterns and anomalies that should be a cause for concern. As a result, many organizations prefer to use specialized log management tools that provide a more intuitive and efficient way to track and analyze logs.

One possible solution is [Better Stack](https://betterstack.com/logs). Sending your Caddy logs to Better Stack is quite easy to configure using [Vector](https://betterstack.com/community/guides/logging/vector-explained/) as a log forwarder. To explore this, you can add Vector to your Docker Compose stack, supplying a configuration file that instructs it to ingest the logs that it collects into Better Stack.

[Sign up](https://logs.betterstack.com/users/sign-up) for a free Better Stack account and navigate to the [Logs & Metrics dashboard](https://logs.betterstack.com/dashboard). Then, from the menu on the left, choose **Sources** and click on **Connect source**:

Specify `Caddy` as the name and `Vector` as the platform, then click **Create source**:

A page appears showing the details of your newly created source. Go ahead and copy the source token:

Using the supplied source token, create a new file called `vector.yaml` inside your `caddy-tutorial` folder with the following contents:

```
sources:
  caddy:
    type: "docker_logs"

sinks:
  better_stack:
    type: "http"
    method: "post"
    inputs: ["caddy"]
    uri: "https://in.logs.betterstack.com/"
    encoding:
      codec: "json"
    auth:
      strategy: "bearer"
      token: "<your_source_token>"

```

This configuration file instructs Vector to monitor the logs emitted from the `caddy` container and to ingest them into Better Stack over HTTP. You can now add Vector to your Docker Compose stack.

To do this, use the [timberio/vector](https://hub.docker.com/r/timberio/vector) image on Docker Hub, as suggested by the [Install Vector on Docker](https://vector.dev/docs/setup/installation/platforms/docker/) guide from the official documentation. You can use the Alpine version of the image to save some bandwidth.

You need to take the `vector.yaml` file you just created and mount it into the container, replacing the default `/etc/vector/vector.yaml` file provided. You also need to mount the local Docker socket inside the container. This is necessary, because Vector needs to issue commands against the local `docker` daemon to be able to detect the containers that it is instructed to monitor and tail their logs.

Please bear in mind that mounting the Docker socket into the container is not appropriate for production use but is still a convenient way to get started locally in order to explore Vector.

In a production setting, you would want to [protect the Docker daemon socket](https://docs.docker.com/engine/security/protect-access/) and have the `vector` container communicate with it over either SSH or HTTPS. You could also just install Vector directly on the host machine instead of running it as a container.

**Learn more**: [14 Best Docker Security Practices You Should Know](https://betterstack.com/community/guides/scaling-docker/docker-security-best-practices/)

The full fragment reads:

```
vector:
  container_name: vector
  image: timberio/vector:0.34.0-alpine
  restart: always
  volumes:
    - ./vector.yaml:/etc/vector/vector.yaml
    - /var/run/docker.sock:/var/run/docker.sock:ro
```

With that, your final `docker-compose.yml` becomes:

docker-compose.yaml

Copied!

```
version: '3'

name: caddy-tutorial

services:
  caddy:
    container_name: caddy
    image: caddy
    restart: always
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - caddy-config:/config
      - caddy-data:/data
      - ./Caddyfile:/etc/caddy/Caddyfile
      - ./dist:/usr/share/caddy
  vector:
    container_name: vector
    image: timberio/vector:0.34.0-alpine
    restart: always
    volumes:
      - ./vector.yaml:/etc/vector/vector.yaml
      - /var/run/docker.sock:/var/run/docker.sock:ro

volumes:
  caddy-config:
  caddy-data:
```

Start your Vector container by typing:

You should see a similar output:

```
[+] Running 2/2
✔ Container vector  Started
✔ Container caddy   Running
```

Navigate back to your browser, access `<your_domain_name>` and refresh the homepage a couple of times.

Soon, you will see new logs arriving in **Live Tail**:

The integration works; however, the entries appearing in Live Tail are quite difficult to understand in their current form. It would be helpful if there's a way to format the entries for better clarity. Luckily, Better Stack provides this opportunity.

Let's go ahead and tweak the log formatting a little bit to improve the readability of the incoming log entries.

If you expand one of the logged messages, you'll see a JSON structure similar to:

Diving into the `message` property of the presented JSON structure reveals a lot of useful information that you can use to make your Live Tail dashboard more expressive:

Navigate to **Settings** from the main view:

A form appears listing the current configuration of the Live Tail view:

You can modify the columns in the following way, and you will see a lot of additional information appearing in the main view as a result:

As you can see, by customizing the Live Tail columns, the output became a lot easier to read and comprehend.

You can tweak this further as much as you like until you achieve the level of detail that fully meets your requirements.

Step 5 — Using Caddy as a reverse proxy
---------------------------------------

In addition to serving static files, Caddy can also be used as a reverse proxy allowing you to route incoming requests to different backend servers based on the URI paths or hostnames of the incoming HTTP requests. This is ideal for exposing the backend API powering your SPA front-end for example.

For this example, you can use the following [sample Node.js application](https://github.com/betterstack-community/caddy-node-app):

`cd` into your `caddy-tutorial` folder and clone the application from GitHub:

```
git clone https://github.com/betterstack-community/caddy-node-app.git backend
```

The folder `<your_caddy_tutorial_folder>` should now have the following contents:

```
.
├── Caddyfile
├── dist
│   ├── assets
│   │   ├── index-1a72bdb1.js
│   │   └── index-1eb968c3.css
│   └── index.html
├── docker-compose.yml
├── index.html
├── backend
│   ├── index.js
│   ├── package.json
│   └── package-lock.json
└── vector.yaml
```

You must specify another service in your Docker Compose stack to serve the example backend application. The following fragment should suffice for that purpose:

```
backend:
  container_name: backend
  image: node:20-alpine
  restart: always
  working_dir: /home/node/app
  volumes:
    - ./backend:/home/node/app
  command: "npm start"
```

It defines a new `backend` service that uses the official `node:20` image (the current LTS version of Node.js at the time of this writing) in its Alpine variant (to save some bandwidth). It then mounts the sample application that you cloned inside the container running that image, and then starts it by calling `npm start`.

The entire `docker-compose.yml` at this point becomes:

docker-compose.yml

Copied!

```
version: '3'

name: caddy-tutorial

services:
  caddy:
    container_name: caddy
    image: caddy
    restart: always
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - caddy-config:/config
      - caddy-data:/data
      - ./Caddyfile:/etc/caddy/Caddyfile
      - ./dist:/usr/share/caddy
  vector:
    container_name: vector
    image: timberio/vector:0.34.0-alpine
    restart: always
    volumes:
      - ./vector.yaml:/etc/vector/vector.yaml
      - /var/run/docker.sock:/var/run/docker.sock:ro
  backend:
    container_name: backend
    image: node:20-alpine
    restart: always
    working_dir: /home/node/app
    volumes:
      - ./backend:/home/node/app
    command: "npm start"

volumes:
  caddy-config:
  caddy-data:
```

Your `docker-compose.yml` is now fully prepared for running the sample Node.js application, but if you call `docker compose up` now, you will realize that Caddy is unaware of the newly deployed `backend` service and is unable to route requests to it. To address this issue, you have to apply some slight modifications to your `Caddyfile`.

First, the existing configuration needs to be wrapped inside a `handle` block as follows:

```
handle {
  root * /usr/share/caddy
  file_server
  try_files {path} /index.html
}
```

The `handle` directive allows you to add different path matchers to your `Caddyfile`. This is useful when you want to apply specific rules or settings to different paths within your application.

For example, you can have a primary set of rules for the root path, instructing Caddy to serve your front-end application. Then, you can define another set of rules for a specific path, such as `/api`, to instruct Caddy to serve the backend. You can use a `handle_path` directive for that purpose.

Since a client may accidentally request `<your_domain_name>/api` instead of `<your_domain_name>/api/` you may want to utilize a `redir` directive for instructing Caddy to route such requests to your backend right before defining your `/api` path handler. Otherwise, such requests would be routed to the front-end, and this is very likely something undesirable.

The final `Caddyfile` becomes:

```
<your_domain_name> {
  redir /api /api/

  handle_path /api/* {
    reverse_proxy backend:3000
  }

  handle {
    root * /usr/share/caddy
    file_server
    try_files {path} /index.html
  }

  log {
    output stdout
  }
}
```

With all of these changes in place, you can go ahead and restart your services:

```
[+] Restarting 3/3
 ✔ Container vector   Started   2.0s
 ✔ Container backend  Started   11.0s
 ✔ Container caddy    Started   2.0s
```

The updated `Caddyfile` still allows you to access your main front-end app through `<your_domain_name>`, but if you try opening `<your_domain_name>/api/hello` in a browser, you will now see the following page:

With that, you have successfully configured Caddy to work not only as a static file server, but also as a reverse proxy for forwarding API requests to a custom backend.

Step 6 — Monitoring your Caddy server
-------------------------------------

With your Caddy server up and running, it's always a good idea to configure uptime monitoring to ensure that everything is in good working order.

Let's use [Uptime](https://betterstack.com/uptime) for that purpose. Log into your Better Stack account and navigate to the **Monitors** page in Uptime and click **Create Monitor**:

Input `<your_domain_name>` into the presented form:

Click **Create Monitor** and wait a few seconds for the monitor to become available:

Navigate back to `<your_caddy_tutorial_folder>` and type in:

After a few moments, Uptime detects that your server is no longer responding and reports an incident:

Now issue the following command once again:

After a few moments, Uptime detects that your server is up again and starts validating its recovery:

As the subsequent [health checks](https://betterstack.com/community/guides/monitoring/health-checks/) complete successfully, Uptime starts reporting that your server has recovered successfully:

This has your front-end covered, but remember that you configured Caddy to proxy all `/api/*` requests to a custom Node.js backend. Your current monitor won't detect any downtime in your backend, as the URL it monitors (`<your_domain_name>`) is served by the static file server in Caddy, and not by the reverse proxy.

Go ahead and create another monitor for `<your_domain_name>/api/hello`:

Now, issue the following command:

```
docker compose stop backend
```

```
[+] Stopping 1/1
 ✔ Container backend    Stopped   10.4s
```

After a few moments, Uptime starts reporting that your back-end is unavailable, while your front-end still shows to be in good working order:

That's about as easy as it gets to configure monitoring for your Caddy server with Uptime.

Final thoughts
--------------

This article provided you with a comprehensive understanding of Caddy, its unique features, and how it distinguishes itself from other web servers.

You learned the intricacies of operating Caddy in a Docker environment and you mastered its use for automatic TLS handling, serving static files, and functioning as a reverse proxy for directing requests to custom backends.

Additionally, you gained insights into leveraging Caddy's logging capabilities and integrating these logs with Better Stack for more efficient analysis, and you set up Uptime monitoring to ensure the continual operation of your web applications.

Equipped with this knowledge, you're now ready to proficiently manage and deploy your web applications using Caddy, with a solid foundation to explore its more advanced functionalities and configurations.

For further exploration, consider diving into the [official Caddy documentation](https://caddyserver.com/docs/), engaging with the [Caddy community forum](https://caddy.community/), and examining the extensive list of [available plugins](https://caddyserver.com/download).

Thanks for reading!
