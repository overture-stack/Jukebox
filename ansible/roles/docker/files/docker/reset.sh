#!/bin/sh
. ~/config/jupyterhub.env
docker-compose down
docker rmi ${DOCKER_NOTEBOOK_IMAGE}
docker-compose up
