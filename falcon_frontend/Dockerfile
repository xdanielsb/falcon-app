FROM node:20-alpine AS npm-ci
WORKDIR /usr/src/app
# Run your commands
COPY . .
ENV NX_DAEMON=false
RUN npm install && npm install -g @nrwl/cli@15.9.7 && npm install -g nx@19.3.2
RUN rm -r .nx && rm -r .angular
RUN npx nx reset && npx nx build --verbose
COPY . .
EXPOSE 4200
RUN npm install -g serve
## Set the default command to serve the build output
CMD ["serve", "-s", "dist/falcon_frontend/browser", "-l", "tcp://localhost:4200"]
