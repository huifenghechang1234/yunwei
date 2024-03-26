node puppetagent {
file { 'test.sh':
 path => '/etc/test.sh',
 owner  => 'root',
 group  => 'root',
 mode   => '655',
 source => 'puppet:///modules/test/test.sh',
 }
exec { 'execute ':
 command => 'bash /etc/test.sh',
 require => File['test.sh'],
 path => ["/bin/"],
}
}
