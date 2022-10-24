# Puppet script for configuring nginx webserver and adding http custom header.
exec { 'command':
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
