# Puppet manifest to fix a bug in wp-setings.php

file { '/var/www/html/wp-settings.php':
  ensure => 'file',
  content => 'Your file content goes here', 
  mode => '0644',
}

exec { 'fix wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  require => File['/var/www/html/wp-settings.php'],
}
