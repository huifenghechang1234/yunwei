node puppetagent {

file { 'helloworld':

    path => '/etc/helloworld.txt',
    owner  => 'root',
    group  => 'root',
    mode   => '655',
    content => "hello world from puppet!\n",
    }

}
