#!/bin/bash
set -x 

here=$(dirname $0)
cd $here
. ~/config/jupyterhub.env

docker network inspect ${DOCKER_NETWORK_NAME} >/dev/null 2>&1 || docker network create ${DOCKER_NETWORK_NAME}

docker volume inspect ${DATA_VOLUME} >/dev/null 2>&1 || docker volume create --name ${DATA_VOLUME}

docker volume inspect ${OPT_VOLUME} >/dev/null 2>&1 || docker volume create --name ${OPT_VOLUME}

docker build --build-arg="JUPYTERHUB_VERSION=${JUPYTERHUB_VERSION}" -t "${CORE_IMAGE}" hub -f hub/Dockerfile.jupyterhub-core

cd notebook
docker build -t ${CREATE_VOLUME_IMAGE} . -f Dockerfile.create-volume 
docker build -t ${LOCAL_NOTEBOOK_IMAGE} . -f Dockerfile.notebook 

# Run bash so that the mount will copy the mount directory into the volume 
docker run -v "${OPT_VOLUME}:/opt" ${CREATE_VOLUME_IMAGE} /bin/bash 

echo "To start/stop the jupyterhub service, run docker-compose up/down"
