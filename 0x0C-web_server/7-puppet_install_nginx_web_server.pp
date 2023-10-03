# configuring my server with Puppet
# install and configure an Nginx server using Puppet instead of Bash
# include resources in your manifest to perform a 301 redirect when querying /redirect_me.
# configures nginx to serve a simple page and a 404 page
# and to redirect /redirect_me to www.google.com
$nginx = 'nginx'

package { $nginx:
  ensure   => installed,
  provider => 'apt',
}

service { $nginx:
  ensure  => running,
  enable  => true,
  require => Package[$nginx],
}

file { '/var/www/nginx-html':
  ensure  => 'directory',
  require => Package[$nginx],
}

file { '/var/www/nginx-html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/var/www/nginx-html/404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page',
}

file {
  '/etc/nginx/sites-available/default':
    ensure  => present,
    content => "server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/nginx-html;
      index index.html index.htm;

      location /redirect_me {
        return 301 http://www.google.com;
      }

      error_page 404 /404.html;
      location /404 {
          internal;
      }
    }",
    require => Package[$nginx],
    notify  => Service[$nginx],
}
