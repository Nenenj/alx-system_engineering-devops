exec { 'killmenow_process':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin', # Add additional paths as needed
  onlyif      => 'pgrep -f killmenow',
  refreshonly => true,
}
