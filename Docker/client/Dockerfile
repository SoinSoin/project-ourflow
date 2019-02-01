FROM node:10.15.0-alpine
RUN npm install -g @vue/cli &&  npm install -g @vue/cli-init && npm install -g @vue/cli-service
WORKDIR /usr/src/ourflow/client/
COPY ourflow/client/. .
RUN npm install && npm cache clean --force
VOLUME /usr/src/ourflow/client/
EXPOSE 8080