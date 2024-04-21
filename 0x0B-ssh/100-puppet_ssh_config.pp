# set up your client SSH configuration file so that you can connect to a server without typing a password.
# 
# Requirements:
# 
# Your SSH client configuration must be configured to use the private key ~/.ssh/school
# Your SSH client configuration must be configured to refuse to authenticate using a password
include stdlib

 file_line { 'remove_password_authentication':
      ensure => present,
      path   => '~/etc/ssh/ssh_config',
      line   => '   PasswordAuthentication no',
      match  => '   PasswordAuthentication (yes|no)',
    }

file_line { 'use_school_private_key':
      ensure            => present,
      path              => '~/etc/ssh/ssh_config',
      line              => '  IdentityFile ~/.ssh/school', 
      match             => '  IdentityFile ~*',
    }
