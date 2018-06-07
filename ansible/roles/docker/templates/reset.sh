#!/bin/sh
cd {{ run_dir }}
. {{ jukebox_env }}
docker-compose down
docker rmi ${DOCKER_NOTEBOOK_IMAGE}
docker-compose up
