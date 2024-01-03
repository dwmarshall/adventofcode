#!/usr/bin/perl
use warnings;
use strict;

sub hash {
  my $input = shift;

  my $current_value = 0;

  for my $i (split //, $input) {
    $current_value += ord($i);
    $current_value *= 17;
    $current_value %= 256;
  }
  $current_value;
}

my $string = <>;
chomp $string;

my $total = 0;
for my $key (split /,/,$string) {
  $total += hash($key);
}

print "$total\n";
