# manifest that kills a process named killmenow.
# 
# Requirements:
# 
# Must use the exec Puppet resource
# Must use pkill
exec {'kills killmenow process':
  command => '/usr/bin/pkill -x killmenow',
}
