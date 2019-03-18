#!/bin/sh
cd {{ run_dir }}
docker-compose down
docker rmi {{ notebook_image }}
docker rmi {{ jupyterhub_image }}
./build_hub
./build_notebook
docker-compose up
