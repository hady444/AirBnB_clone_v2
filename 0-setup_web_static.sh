#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "
<!DOCTYPE HTML>
<html>
<head>
</head>
<body>
Holeborton School
</body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu /data
sudo chgrp -R ubuntu /data

echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By \$HOSTNAME;
        root /var/www/html;
        index index.html index.htm;

        location /hbnb_static {
                alias /data/web_static/current;
                index index.html index.htm;
        }

        location /redirect_me {
            return 301 https://www.youtube.com/@ALXAfrica;
        }

        error_page 404 /error_404.html;
        location = /error_404.html {
          root /var/www/html;
          internal;
        }
}
" > /etc/nginx/sites-available/default
sudo systemctl restart nginx
