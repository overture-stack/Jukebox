#!/bin/bash
#set -x 

here=$(dirname $0)
cd $here
. .env

docker network inspect ${DOCKER_NETWORK_NAME} >/dev/null 2>&1 || docker network create ${DOCKER_NETWORK_NAME}

docker volume inspect ${DATA_VOLUME} >/dev/null 2>&1 || docker volume create --name ${DATA_VOLUME}

docker volume inspect ${OPT_VOLUME} >/dev/null 2>&1 || docker volume create --name ${OPT_VOLUME}

docker build --build-arg="JUPYTERHUB_VERSION=${JUPYTERHUB_VERSION}" -t jupyterhub-core hub -f hub/Dockerfile.jupyterhub-core

cd notebook
docker build -t create-volume . -f Dockerfile.create-volume  
docker build -t ${LOCAL_NOTEBOOK_IMAGE} . -f Dockerfile.notebook 

# Just running a shell with the volume mounted copies the mounted directory to
docker run -v "${OPT_VOLUME}:/opt" create-volume /bin/bash 


echo "To start/stop the jupyterhub service, run docker-compose up/down"
