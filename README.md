# Frame Rate Increaser
Web app for increasing frame rate of a video

## How to launch this app?

For this you will need [docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/)

1. Clone this repository
2. Go into project directory
3. Fill `.env` file like `.env.template`. Change ports and timeone if needed
4. Build docker containers with `docker-compose build`
5. Run containers as daemons with `docker-compose up -d`

## After launch
After launch you will be able to open web interface on `http://0.0.0.0:8080`
