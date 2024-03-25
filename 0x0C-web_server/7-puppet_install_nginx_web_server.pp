# Define package, service, and file resources for Nginx installation and configuration
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => '<!DOCTYPE html>
              <html>
              <head>
              <title>Hello World!</title>
              </head>
              <body>
              <h1>Hello World!</h1>
              </body>
              </html>',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define a custom template for Nginx configuration
# This template will include the redirect configuration for /redirect_me
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define the template for the Nginx configuration file
# This template includes both the standard Nginx configuration and the redirect configuration
# for /redirect_me
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define a template for the Nginx configuration
# This template includes both the standard Nginx configuration and the redirect configuration
# for /redirect_me
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}
