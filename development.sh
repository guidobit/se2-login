#!/bin/sh

# This runs the container in development mode
docker run -it -v $(pwd -LP):/app se2-login:latest /bin/sh