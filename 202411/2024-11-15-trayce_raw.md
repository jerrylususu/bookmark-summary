Title: "The network tab for Docker containers."

URL Source: https://trayce.dev/

Markdown Content:
How does it work?
-----------------

The [TrayceAgent](https://github.com/evanrolfe/trayce_agent/) container runs along side your existing containers. The agent uses eBPF probes to intercept network requests and send them back to the GUI to be displayed.

Protocols Supported:

*   HTTP
*   HTTPS (for Go and OpenSSL-based languages like Python, Ruby etc.)

Coming soon:

*   Websockets
*   GRPC
*   MySQL & Postgres
*   MongoDB
*   Redis
*   Kafka

  

Who is it for?
--------------

Trayce is intended for anyone wanting to see whats going on inside their **local** Docker containers: backend developers, QA engineers, testers etc.
