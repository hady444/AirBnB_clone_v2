#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo '
<!DOCTYPE HTML>
<head>
</head>
<body>
Holeborton School
</body>
</html>
' > /data/web_static/releases/test/index.html
link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"

ln -sf "$target_path" "$link_path"
sudo chown -R ubuntu /data
sudo chgrp -R ubuntu /data

echo "
listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
" > /etc/nginx/sites-available/default
#server {
	#listen 80 default_server;
	#listen [::]:80 default_server;
	#add_header X-Served-By $HOSTNAME;
	#root /var/www/html;
	#index index.html index.htm index.nginx-debian.html;

	#location /hbnb_static {
        #	alias /data/web_static/current;
        #	index index.html index.htm;
	#}
	#rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        #error_page 404 /error_404.html;
#}

sudo systemctl restart nginx
