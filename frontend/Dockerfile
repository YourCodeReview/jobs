# Step 1: Build the Vue.js app
FROM node:latest as build-stage
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build


# Step 2: Serve the Vue.js app using Nginx
FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy SSL certificates
COPY certs/cert.pem /etc/nginx/cert.pem
COPY certs/privkey.pem /etc/nginx/privkey.pem

COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]
