# solves many open files bug
exec { 'user-hard-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}
exec { 'user-soft-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}
