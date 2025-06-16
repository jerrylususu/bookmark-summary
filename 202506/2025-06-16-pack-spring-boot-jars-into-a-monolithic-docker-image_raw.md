Title: Pack Spring Boot JARs into a monolithic Docker image

URL Source: https://miao1007.github.io/f90ce500-08b5-11f0-b358-6fc945929be4/

Markdown Content:
Pack Spring Boot JARs into a monolithic Docker image

2025-06-15 / modified at 2025-06-15 / 1k words / 6 mins

In this article, we describe how we successfully packaged our 10+ Spring Boot JARs into an all-in-one Docker image with minimal size, which were originally deployed on cloud Kubernetes instances.

Why monolithic deployment?
--------------------------

There are plenty of software delivery methods: tarball archives, Linux installer packages, containers, or the Kubernetes Helm ecosystem. All deployments can be automated for Site Reliability Engineering (SRE) teams with reasonable effort. The key consideration is determining who should manage the operating systems and platforms, including Linux passwords, security patches, and Kubernetes clusters.

Despite deploying containers on cloud-managed Kubernetes being more advantageous—as each container is easy to scale horizontally (CGroup utilization, VM specs) and vertically (by increasing the ReplicaSet)—Kubernetes can be an overhead when deploying in private data centers. This includes purchasing commercial Kubernetes support or hiring Kubernetes administrators. As a result, our application is deployed in two ways:

*   **Cloud**: We manage all cloud virtual machines on Kubernetes clusters, delivering Software as a Service (SaaS) directly to users. Application updates and bug fixes are deployed quickly using blue-green deployments.

*   **Private Data Centers (IDCs)**: Each month, we select our stable cloud version, package the application into a single Docker image, and deploy it to the customer’s isolated server rooms. We are responsible for the application; the customer handles the rest.

The diagram below illustrates our product delivery to cloud and on-premise environments:

![Image 1: monoliths](https://miao1007.github.io/images/monoliths.svg)

Beyond simplified deployment, we also avoid premature optimization:

*   Instead of using distributed cache or configuration storage (such as Redis or etcd clusters), we optimize the PostgreSQL instance with more memory buffer. Global locks and key-value storage are managed through database transactions and the application’s memory cache.
*   Instead of using overlay networking (such as Consul or Istio), all networking routers and middleware are handled by a local Traefik instance.

With this monolithic deployment design, our product can be deployed on any machine with acceptable performance.

How to create a monolithic image?
---------------------------------

#### The backend

For [Spring Boot-based](http://spring.io/guides/gs/spring-boot-docker) Docker images, even a “Hello World” application JAR with JDK can exceed 300 MB. With dozens of JARs, the uncompressed image becomes too large to download efficiently.

However, Spring Boot images contain significant duplicate content. For example:

1

2

3

4

5 FROM openjdk:17

COPY target/app.jar app.jar

ENTRYPOINT ["java","-jar","/app.jar"]

To reuse third-party JARs inside `app.jar`, we first extract reusable libraries from the fat JAR using [Jib](https://github.com/GoogleContainerTools/jib), a container build tool developed by Google. The build process requires a custom `jib.yaml` script.

After separating the fat JAR into subdirectories, we merge third-party JARs into a unified location using hash-based symbolic links. The final layout:

After hashing dependencies into a shared directory, the monolithic application compresses to 1/8 the original size:

*   **Original JAR size**: JRE (140 MB) + libraries (130 MB) + application classes (2 MB) = 272 MiB
*   **10 JARs before compression**: 272 × 10 = 2,720 MB
*   **10 JARs after compression**: JRE (140 MB) + application classes (2 × 10 = 20 MB) + shared libraries (130 MB) = 290 MB

> Some shared libraries may be used by only one application, so the 130 MB might increase.

To maximize compression, manage third-party dependencies with a centralized SBOM (Software Bill of Materials) to unify versions and prevent conflicts (e.g., Guava 33.1 vs. 33.2 across applications).

#### The frontend

Frontend static files are served using Caddy or Nginx. Extract assets from your frontend Docker image:

#### Networking and routing

We use Traefik for networking, relying on its auth middleware for header-based authentication. While chosen for our cloud Kubernetes solution, Nginx is a valid alternative if preferred.

Include these components:

#### Process management

Standard Spring Boot images have a single entrypoint to start the JAR. For multiple processes, use [Supervisor](https://supervisord.org/) for process management (provisioning, restarting, shutdown):

Supervisor manages all processes at startup:

The final build
---------------

After completing all steps, we achieve this layout:

The final Dockerfile pseudocode:

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17 FROM jre:17

RUN apt-get install supervisor ...

COPY <binaries: caddy/traefik>

COPY <JAR dependencies (symbolic links created during build)>

COPY <etc configuration>

COPY <business classes>

COPY <frontend assets>

RUN <useradd>

EXPOSE 8080 8443

ENTRYPOINT <launch supervisor>

This produces a Docker image of approximately 500 MB.

Appendix
--------

#### Open source tools used

*   [Supervisor](https://supervisord.org/): Process management
*   [Traefik](https://traefik.io/): Application gateway
*   [Caddy](https://caddyserver.com/): Serves static frontend assets
*   [UPX](https://upx.github.io/): Compresses executable binaries (especially effective for Go applications like Traefik)
*   [Dive](https://github.com/wagoodman/dive): Docker image layer inspection
*   **Java ecosystem**:
    *   [Maven](https://maven.apache.org/): Manages Spring Boot applications and dependencies via centralized SBOM
    *   [Jib](https://github.com/GoogleContainerTools/jib): Separates application code from third-party libraries
    *   [Flyway](https://flywaydb.org/): Database schema management
