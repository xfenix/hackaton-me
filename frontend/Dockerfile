FROM node:latest as builder

WORKDIR /srv/www/
COPY . .
RUN npm install
RUN npm run build


FROM nginx:latest
WORKDIR /srv/www/
USER nginx
COPY --from=builder /srv/www/dist/. /srv/www/
COPY nginx.conf /etc/nginx/
CMD ["nginx", "-g", "daemon off;"]
