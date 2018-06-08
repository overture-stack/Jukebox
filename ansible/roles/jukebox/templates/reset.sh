#!/bin/sh
cd {{ run_dir }}
docker-compose down
docker rmi {{ notebook_image }}
docker-compose up
