# server

## Project setup
```
$ conda create -n personal_website python=3.10
$ conda activate personal_website
$ pip install -r requirements.txt
```
```angular2html
$ pip install gunicorn
$ gunicorn -D -w 1 -b 0.0.0.0:5000 app:app
```