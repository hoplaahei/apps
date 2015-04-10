    use strict;
    use warnings;

    use FindBin;
    use lib "$FindBin::Bin";
    use MyServer;

    my $server = MyServer->new;
    $server->run;
