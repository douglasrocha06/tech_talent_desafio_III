FROM mysql:8.0

ARG ROOT_PASSWORD=1234
ENV MYSQL_ROOT_PASSWORD=${ROOT_PASSWORD}

ARG SETUP_DATABASE=api_clientes
ENV MYSQL_DATABASE=${SETUP_DATABASE}

ARG SETUP_REMOTE_USERNAME=remote
ARG SETUP_REMOVE_PASSWORD=1234

COPY docker_container/base_de_dados/script.sql /docker-entrypoint-initdb.d/script.sql

RUN echo "CREATE USER '${SETUP_REMOTE_USERNAME}'@'%' IDENTIFIED BY '${SETUP_REMOVE_PASSWORD}';GRANT ALL PRIVILEGES ON *.* TO '${SETUP_REMOTE_USERNAME}'@'%' WITH GRANT OPTION;" > /docker-entrypoint-initdb.d/_grant_remote.sql
EXPOSE 3306
CMD ["mysqld"]