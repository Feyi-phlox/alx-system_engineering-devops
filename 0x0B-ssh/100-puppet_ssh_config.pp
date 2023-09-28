# setting  up your client SSH configuration file
# so that you can connect to a server without typing a password

file { 'etc/ssh/ssh_config':
  ensure  => file,
  content => "PasswordAuthentication no\n",
  replace => true,
}

file { 'etc/ssh/ssh_config':
  ensure  => file,
  line    => "IdentityFile ~/.ssh/school\n",
  replace => true,
}
