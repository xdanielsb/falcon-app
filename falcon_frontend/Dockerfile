FROM node:20-alpine AS npm-ci
WORKDIR /usr/src/app
# Run your commands
COPY . .
ENV NX_DAEMON=false
RUN rm -r .nx && rm -r .angular && npx nx reset && npx nx build --verbose
COPY . .
EXPOSE 4200
RUN npm install -g serve
## Set the default command to serve the build output
CMD ["serve", "-s", "dist/falcon_frontend/browser", "-l", "tcp://0.0.0.0:4200"]
