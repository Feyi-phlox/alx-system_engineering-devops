# creating a custom HTTP header response with Puppet.
exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/nginx-html':
  ensure  => 'directory',
  require => Package['nginx'],
}

file { '/var/www/nginx-html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/var/www/nginx-html/404.html':
  ensure  => present,
  content => 'Ceci n\est pas une page',
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/nginx-html;
    index index.html index.html;
    add_header X-Served-By ${hostname};

    location /redirect_me {
      return 301 http://www.stackoverflow.com;
    }

    error_page 404 /404.html;
    location /404 {
        internal;
    }
  }",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
