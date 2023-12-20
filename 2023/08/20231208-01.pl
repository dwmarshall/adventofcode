#!/usr/bin/perl
use warnings;
use strict;

chomp(my $route = <>);
my @route = split //, $route;

my %map;

while (<>) {
    chomp;
    if (/([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)/) {
        $map{$1} = [$2, $3];
    }
}

my $steps = 0;
my $current = 'AAA';

while ($current ne 'ZZZ') {
  my $direction = $route[$steps % @route];
  if ($direction eq 'L') {
    $current = $map{$current}[0];
  } elsif ($direction eq 'R') {
    $current = $map{$current}[1];
  }
  $steps++;
}

print $steps, "\n";
