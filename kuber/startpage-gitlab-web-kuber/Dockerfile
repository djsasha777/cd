FROM nginx:1.23.1-alpine
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /var/www/html/
EXPOSE 80
