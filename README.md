# TensorFlow Docker Environment

This repository provides a Docker-based Python environment for running TensorFlow. The main advantage of this setup is that you don't need to install a Python environment on your local machine. Instead, you can use Docker and the `tensorflow/tensorflow:latest-jupyter` container.

## Getting Started

1. Install Docker on your machine.
2. Clone this repository.
3. Build the Docker image by running `docker build -t my-jupyter-env .` in the terminal.
4. Start the Docker container by running `docker run -p 8888:8888 my-jupyter-env`.

After running these steps, you'll have a Jupyter notebook server running in a Docker container. This server includes a Python environment with TensorFlow installed. You can access the server at `localhost:8888` in your web browser.

This setup makes it easy to start working with TensorFlow, without the need to manage Python environments on your local machine.