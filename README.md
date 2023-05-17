# CI-CD-for-chess-data-pipeline

This repo uses Flask, watches for POST requests, and uses a self-signed certificate in an AWS EC2 instance to set up CI/CD for the `chess-data-pipline` repo.

A webhook from the `chess-data-pipeline` repo is required, and the above CI/CD setup uses a clone of this repo in a Ubuntu EC2 instance. The webhook is set to accept a self-signed certificate in the EC2 instance and to use HTTPS, which is allowed by the inbound rules for this EC2 instance's security group.

The virtual environment used by this repo:

(1)  Python's `venv` is used.

(2)  The virtual environment is stored in the above EC2 instance.

(3)  The virtual environment is stored outside of this repo.

(4)  The `requirements.txt` file in this repo gives all the dependencies for this virtual environment.
