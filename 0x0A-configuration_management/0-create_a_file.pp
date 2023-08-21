# Puppet manifest creates a file at /tmp
file { '/tmp/school':
    ensure  => 'present',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}
