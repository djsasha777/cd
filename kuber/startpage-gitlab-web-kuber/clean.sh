#!/bin/bash
if [ "$(docker ps -q -f name=startpage)" ]; then docker-compose down && docker system prune; fi