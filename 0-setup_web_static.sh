#!/usr/bin/env bash
# Prepare the web servers.

# Install Nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

# Create fake HTML content
echo "<html><body>Hello, World!</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_content="
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
"
sudo sed -i "s,server_name _;, $config_content," /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
