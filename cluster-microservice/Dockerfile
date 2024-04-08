FROM node:lts-alpine
WORKDIR /app
COPY package.json .
COPY package-lock.json .
COPY server.mjs .
RUN npm install

EXPOSE 5000

CMD ["node", "server.js"]