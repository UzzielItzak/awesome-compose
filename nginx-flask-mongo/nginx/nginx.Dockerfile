FROM nginx

COPY nginx.conf /tmp/nginx.conf

ENV FLASK_SERVER_ADDR=flask-backend:9090

CMD ["/bin/bash", "-c", "envsubst < /tmp/nginx.conf > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]