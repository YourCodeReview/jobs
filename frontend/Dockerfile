FROM node:latest as build-stage
WORKDIR /app
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build


# Step 2: Serve the Vue.js app using Nginx
FROM nginx:alpine
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]