#!/usr/bin/perl

use warnings;
use strict;

sub line_value {
  my $line = shift;
  my ($first_digit) = $line =~ /^\D*(\d)/;
  my ($second_digit) = $line =~ /(\d)\D*$/;
  return $first_digit * 10 + $second_digit;
}

my $total = 0;
while (<>) {
  chomp;
  # print "$_: ", line_value($_), "\n";
  $total += line_value($_);
}
print "$total\n";
