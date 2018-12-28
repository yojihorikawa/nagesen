# ベースイメージを指定
# 今回は LTS の 8.9.4 にする
# alpine は 軽量の linux OS
FROM node:10.13.0-alpine

# node.js の環境変数を定義する
# 本番環境では production
ENV NODE_ENV=development

# 雛形を生成するのに必要なパッケージのインストール
RUN apk add --update alpine-sdk

#ethereum-jsでpythonが必要
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN apk add --update python-dev build-base jpeg-dev zlib-dev freetype-dev libjpeg-turbo-dev libpng-dev

# 日本語フォント追加（wordcloud文字化け対応）
RUN apk update \
  && apk add --no-cache curl fontconfig \
  && curl -O https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
  && mkdir -p /usr/share/fonts/NotoSansCJKjp \
  && unzip NotoSansCJKjp-hinted.zip -d /usr/share/fonts/NotoSansCJKjp/ \
  && rm NotoSansCJKjp-hinted.zip \
  && fc-cache -fv

RUN npm -g uninstall yarn
RUN npm -g install yarn

RUN git config --global url."https://".insteadOf git://

RUN yarn
RUN yarn global add express-generator@4.16.0
RUN yarn global add ts-node
RUN yarn global add nodemon
#これが無いとweb3がインストールされない。
RUN yarn global add node-gyp
RUN yarn add express
RUN yarn add mongodb
RUN yarn add mongoose
RUN yarn add body-parser
RUN yarn add moment
#python2.7でないとビルドできない。
RUN yarn add web3
RUN yarn add ethereumjs-tx
RUN yarn global add typescript

RUN yarn global add truffle



# ディレクトリを作成
WORKDIR /src

RUN yarn install



# ポート3000番を開放する
EXPOSE 3001
