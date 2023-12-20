#!/usr/bin/perl
use warnings;
use strict;

use List::Util qw/all/;
use Math::BigInt;

sub compute_period {
  my $position = shift;
  my $mapref = shift;
  my $route = shift;

  my @route = split //, $route;
  my $count = 0;
  while ($position !~ /..Z/) {
    my $way = $route[$count++ % @route] eq 'L' ? 0 : 1;
    $position = $mapref->{$position}[$way];
  }
  return $count;
}

chomp(my $route = <>);
my @route = split //, $route;

my %map;

while (<>) {
    chomp;
    if (/([0-9A-Z]{3}) = \(([0-9A-Z]{3}), ([0-9A-Z]{3})\)/) {
        $map{$1} = [$2, $3];
    }
}

my @current = grep { $_ =~ /..A/ } keys %map;

my @periods = map { compute_period($_, \%map, $route) } @current;

my $steps = Math::BigInt::blcm(@periods);
print "$steps\n";
