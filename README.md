
# Pickup point selection widget

Web widget for selecting a delivery service branch created as part of a bachelor's thesis at FIM UHK.


## Tech Stack

**Client:** React, Bootstrap, React Leafler, Apollo Client

**Server:** Django, Graphene

**Microservice:** Node, Express, mapbox/supercluster

**Database:** MariaDB


## Demo
 [Demo e-shop](https://demo.ltrk.dev/)

 [widget page](https://widget.ltrk.dev/)

 (accessible from UHK network)

## Installation

Install with docker

```bash
  git clone https://github.com/lukastrkan/pickup-point-selection-widget
  cc pickup-point-selection-widget
  cp .env.example .env
  #edit your .env file
  docker compose up -d
```
    
Note: only Django dev server for now
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG` true/false

`SECRET_KEY` Secret key for Django - you can use `base64 /dev/urandom | head -c50`

`ALLOWED_HOSTS` Domains you will use - widget.example.com,widget.example.org

`CSRF_TRUSTED_ORIGINS` Domains + scheme - https://widget.example.com,https://widget.example.org

`CORS_ALLOWED_ORIGINS` Domains + scheme - https://widget.example.com,https://widget.example.org

`DB_NAME` self explanatory

`DB_USER` self explanatory

`DB_PASSWORD` self explanatory

`DB_HOST` self explanatory

`DB_PORT` self explanatory

`BALIKOBOT_USERNAME` Your https://www.balikobot.cz/ username

`BALIKOBOT_PASSWORD` Your https://www.balikobot.cz/ password

`ZASILKOVNA_API_KEY` Your https://www.zasilkovna.cz/ API key

