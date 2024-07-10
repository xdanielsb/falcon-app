FROM node:20-alpine AS npm-ci
WORKDIR /usr/src/app
RUN ls .
# Run your commands
COPY . .
ENV NX_DAEMON=false
RUN npm install
RUN npm install -g @nrwl/cli@15.9.7
RUN npm install -g nx@19.3.2
RUN rm -r .nx
RUN rm -r .angular
RUN npx nx reset
RUN npx nx build --verbose
COPY . .
EXPOSE 4200
RUN npm install -g serve
## Set the default command to serve the build output
CMD ["serve", "-s", "dist/falcon_frontend/browser", "-l", "tcp://0.0.0.0:4200"]
