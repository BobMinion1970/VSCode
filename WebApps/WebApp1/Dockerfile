FROM node:lts-alpine
# copy source code to docker image 
WORKDIR /app
COPY . . 
# install dependencies by using npm install 
RUN npm install 
# provide port for tools
EXPOSE 3000
# define start commando by using npm start
CMD npm start
