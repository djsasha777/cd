#!/bin/bash
if [ "$(docker ps -q -f name=wordpress-5.7.0-php8.0-fpm)" ]; then docker-compose down && docker system prune; fi