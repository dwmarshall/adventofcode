#!/usr/bin/perl

use warnings;
use strict;

use constant RED => 12;
use constant GREEN => 13;
use constant BLUE => 14;

my $total = 0;
while (<>) {
    chomp;
    my ($game) = /^Game (\d+): /;
    my $possible = 1;
    my @subgames = split /\;/;
    for my $subgame (@subgames) {
      if ($subgame =~ /(\d+) blue/) {
        $possible = 0 if $1 > BLUE;
      }
      if ($subgame =~ /(\d+) green/) {
        $possible = 0 if $1 > GREEN;
      }
      if ($subgame =~ /(\d+) red/) {
        $possible = 0 if $1 > RED;
      }
    }
    $total += $game if $possible;
}

print "$total\n";
