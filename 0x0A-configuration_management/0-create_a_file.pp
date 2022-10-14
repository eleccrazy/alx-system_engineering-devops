# This puppet file creates a file called school in /tmp folder

file {'/tmp/school':
ensure  => 'present',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
