# Meetup Manager

A simple tool for communities to manage their events and automating basic tasks for organizers:

- Creating the meetup event using the selected proposals
- Publishing the event
- Announcing the event on social media platforms or other channels, such as:
  - Facebook
  - Twitter
  - LinkedIn
  - WhatsApp
  - Telegram
  - Mailing list
  - ...
  - etc.

Check out the [Wiki](https://github.com/HydPy/meetup-manager/wiki) for more details about the project, features, future plans and database design

## Running the app locally

You need to have Docker installed to run the app locally

To build the image and run the services, run the command on the terminal:

```$ docker-compose up --build -d```

This command will build the docker image on your local system using the Dockerfile and other configuration specified.

And finally launch all services defined in the `docker-compose.yml` file, create its own network, etc.

The Django application is running on a Gunicorn application server and NGINX web server as the reverse proxy.

After running the above command, in the browser go to: `http://localhost`

`NOTE:` If the `meetup-manager` container keeps on going down and error in the logs show permission denied for the
`wait-for-it.sh` utility, please run the below command from src directory

```$ chmod +x wait-for-it.sh```
