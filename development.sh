#!/bin/sh

# This runs the container in development mode
docker run -it -v $(pwd -LP):/app -p 80:5000 se2-login:latest /bin/sh