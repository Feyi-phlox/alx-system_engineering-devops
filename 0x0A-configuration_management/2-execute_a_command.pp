# Puppet manifest to kill a process named "killmenow"

exec { 'kill_killmenow':
  command => 'pkill -9 killmenow',
  provider => 'shell'
}
