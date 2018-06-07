#!/bin/bash
cd {{ run_dir }}
. {{ jukebox_env }} 
docker-compose up
