#!/bin/sh
. ~/config/jupyterhub.env
docker-compose down
docker rmi jupyterhub-docker
docker-compose up
