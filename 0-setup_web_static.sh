#!/usr/bin/env bash
# Prepare the web servers.

sudo apt-get -y install nginx > /dev/null

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

echo "<html><body>Hello, World!</body></html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

config_content="
    location /hbnb_static {
        alias /data/web_static/current/;
    }
"
sudo sed -i "38i$config_content" /etc/nginx/sites-available/default

sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

sudo service nginx restart
