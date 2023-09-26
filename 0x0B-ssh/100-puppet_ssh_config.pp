# Define the SSH client configuration

file { '~/.ssh/config':
  ensure  => present,
  content => "\
Host 100.25.191.149
	PasswordAuthentication no
	IdentityFile ~/.ssh/school
",
}
