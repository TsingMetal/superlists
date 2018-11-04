Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:
  
    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com
* replace USER with the current user

## Systemd server

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging-my-domain.com
* replace USER with the current user
* e.g.: 
```
cat ./deploy_tools/nginx.template.conf \
    | sed "s/DOMAIN/192.168.1.111/g" \
    | sed "s/USER/$(whoami)/g" \
    | sudo tee /etc/nginx/sites-available/superlists.ottg.eu
```

## Folder structure
Assume we have a user account at /home/username

/home/username
|-- sites
    |-- DOMAIN1
         |-- .env
         |-- db.sqlite3
         |-- manage.py etc
         |-- static
         |-- virtualenv
    |-- DOMAIN2
         |-- .env
         |-- db.sqlite3
         |-- etc
