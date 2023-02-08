#!/bin/bash

export PATH=$PATH
source activate personal_website
cd server
killall -9 gunicorn
gunicorn -D -w 4 -b 0.0.0.0:5000 app:app
