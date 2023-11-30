FROM node

RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime\
    && mkdir app

WORKDIR /app
COPY . .

RUN npm i

VOLUME [ "/app/logfile" ]

CMD [ "src/index.ts" ]
ENTRYPOINT [ "npx", "ts-node" ]