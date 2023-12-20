#!/usr/bin/perl
use warnings;
use strict;

use List::Util qw(all);

sub next_value {
  my $aryref = shift;

  my @arrays = ($aryref);
  do {
    my @new_array;
    for my $i (0 .. $#{$arrays[-1]} - 1) {
      $new_array[$i] = $arrays[-1][$i + 1] - $arrays[-1][$i];
    }
    push @arrays, \@new_array;
  } until (all { $_ == 0 } @{$arrays[-1]});

  # Now add new items to the arrays
  for (my $i = $#arrays; $i >= 0; $i--) {
    unshift @{$arrays[$i - 1]}, $arrays[$i - 1][0] - $arrays[$i][0]
  }
  return $arrays[0][0];
}

my $sum = 0;
while (<>) {
  chomp;
  my @numbers = split / /;
  $sum += next_value(\@numbers);
}
print "$sum\n";
