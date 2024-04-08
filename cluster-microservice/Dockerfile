FROM node:lts-alpine
WORKDIR /app
COPY package.json .
COPY package-lock.json .
COPY server.js .
RUN npm install

EXPOSE 5000

CMD ["node", "server.js"]