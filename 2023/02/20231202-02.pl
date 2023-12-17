#!/usr/bin/perl

use warnings;
use strict;

my $total = 0;
while (<>) {
    chomp;
    my ($game) = /^Game (\d+): /;
    my %minimums = (blue => 0, green => 0, red => 0);
    my @subgames = split /\;/;
    for my $subgame (@subgames) {
      if ($subgame =~ /(\d+) blue/) {
        $minimums{blue} = $1 if $1 > $minimums{blue};
      }
      if ($subgame =~ /(\d+) green/) {
        $minimums{green} = $1 if $1 > $minimums{green};
      }
      if ($subgame =~ /(\d+) red/) {
        $minimums{red} = $1 if $1 > $minimums{red};
      }
    }
    $total += $minimums{blue} * $minimums{green} * $minimums{red};
}

print "$total\n";
