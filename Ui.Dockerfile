# syntax=docker/dockerfile:1

# From https://jsramblings.com/dockerizing-a-react-app/
# -From https://nodejs.org/en/docs/guides/nodejs-docker-webapp/-

FROM node:16-alpine 

WORKDIR /app
COPY ./frontend .

RUN npm ci 
RUN npm run build

ENV NODE_ENV production
EXPOSE 3000

CMD [ "npx", "serve", "build" ]