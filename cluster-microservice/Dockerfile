FROM node:lts-alpine

LABEL org.opencontainers.image.source=https://github.com/lukastrkan/cluster-microservice
LABEL org.opencontainers.image.description="mapbox/supercluster microservice"
LABEL org.opencontainers.image.licenses=MIT

WORKDIR /app
COPY package.json .
COPY package-lock.json .
COPY server.js .
RUN npm install

EXPOSE 5000

CMD ["node", "server.js"]