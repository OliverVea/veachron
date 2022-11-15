# Introduction
veachron is a web application which can be used for timing anything that can make http requests.

The project is described on my [personal project page](https://olivervea.github.io/posts/veachron/), which describes installation, configuration and usage of the application.

This readme.md describes how to install and use the source code of the application.

# Installation

Firstly, clone the repository:

```bash
git clone https://github.com/OliverVea/veachron.git
```

Navigate to the directory:

```bash
cd veachron
```

Use the `docker-compose.yaml` file to spin up the application:

```bash
docker compose up --build
```

The `--build` flag can be omitted to use prebuilt images from Docker Hub.

# Usage

After spinning up the application, it can be reaced at [http://ui.localhost](http://ui.localhost) for the UI and [http://api.localhost](http://api.localhost) for the API.