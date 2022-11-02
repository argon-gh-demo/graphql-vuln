FROM node:14-alpine
WORKDIR /node/app

COPY package.json .
RUN yarn

COPY src ./src
COPY tsconfig.json .

CMD [ "node", "build/index.js"]
