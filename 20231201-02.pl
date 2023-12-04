#!/usr/bin/perl

use warnings;
use strict;

my %digits = qw(one 1 two 2 three 3 four 4 five 5 six 6 seven 7 eight 8 nine 9);
my $regex = "\\d|" . join "|", keys %digits;
sub line_value {
  my $line = shift;
  my ($first_digit) = $line =~ /($regex)/;
  my ($second_digit) = $line =~ /.*($regex)/;
  return ($digits{$first_digit} // $first_digit) * 10 + ($digits{$second_digit} // $second_digit);
}

my $total = 0;
while (<>) {
  chomp;
  # print "$_: ", line_value($_), "\n";
  $total += line_value($_);
}
print "$total\n";
