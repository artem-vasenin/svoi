FROM node
LABEL authors="rusich"
WORKDIR /
COPY / .
RUN npm i -g pnpm && pnpm install
EXPOSE 8080
CMD ["pnpm", "run", "serve"]
