#!/usr/bin/perl
use warnings;
use strict;

use lib '.';
use Cards2;

my %hands;

while (<>) {
  chomp;
  my ($hand, $value) = split / /;
  $hands{$hand} = $value;
}

my @sorted = sort { Cards2::compare($b, $a) } keys %hands;

local $" = "\n";
print "@sorted\n";

my $total = 0;
for my $i (0..$#sorted) {
  $total += ($i + 1) * $hands{$sorted[$i]};
}
print "$total\n";
