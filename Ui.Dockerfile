# syntax=docker/dockerfile:1

# From https://jsramblings.com/dockerizing-a-react-app/

FROM node:16-alpine 

WORKDIR /app
COPY ./frontend .

RUN npm ci 
RUN npm run build

EXPOSE 3000

CMD [ "npx", "serve", "build" ]