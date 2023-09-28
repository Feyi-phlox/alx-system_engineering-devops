# setting  up your client SSH configuration file
# so that you can connect to a server without typing a password

file_line { 'turn password auth off':
  ensure => present,
  path   => 'etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
file_line { 'declare identity file':
  ensure => present,
  path   => 'etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
