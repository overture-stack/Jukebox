#!/bin/bash
cd {{ home }}/docker
. ~/config/jupyterhub.env
docker-compose up
