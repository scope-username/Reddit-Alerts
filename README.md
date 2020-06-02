# Reddit_Alerts
scrape reddit for deals and get an email alert using sendgrid

## Build docker image

docker build -t reddit-alerts-app .

## Run docker image

docker run -d --name reddit-alerts --restart unless-stopped reddit-alerts-app

## get logs docker image

docker logs -f reddit-alerts
