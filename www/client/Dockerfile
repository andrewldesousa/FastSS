FROM node:10.16.0-alpine

WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json

RUN npm install

EXPOSE 3000
CMD ["npm", "run", "start"]