#!/usr/bin/perl
use warnings;
use strict;

use List::Util qw/product/;


sub ways {
  my $time = shift;
  my $goal = shift;
  my $ways = 0;
  for my $i (1..$time) {
    my $distance = $i * ($time - $i);
    if ($distance > $goal) {
      $ways++;
    }
  }
  return $ways;
}

my @times;
my @distances;
my @ways_to_win;

while (<>) {
  chomp;
  /^Time:/ && (@times = /(\d+)/g);
  /^Distance:/ && (@distances = /(\d+)/g);
}

for my $i (0..$#times) {
  $ways_to_win[$i] = ways($times[$i], $distances[$i]);
}

print product(@ways_to_win), "\n";
