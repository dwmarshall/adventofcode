#!/usr/bin/perl

use warnings;
use strict;

my $total = 0;
my @input;

my %gears;

sub adjacent_gears {
  my $line_number = shift;
  my $start_column = shift;
  my $adjacent_start = $start_column == 0 ? 0 : $start_column - 1;
  my $end_column = shift;
  my $adjacent_end = $end_column == length($input[$line_number]) - 1 ? $end_column : $end_column + 1;
  my @gears;
  if ($start_column > 0 && substr($input[$line_number], $adjacent_start, 1) eq '*') {
    push @gears, "$line_number,$adjacent_start";
  }
  if ($end_column < length($input[$line_number]) - 1 && substr($input[$line_number], $adjacent_end, 1) eq '*') {
    push @gears, "$line_number,$adjacent_end";
  }
  if ($line_number > 0) {
    my $previous_line = $input[$line_number - 1];
    my $substring = substr($previous_line, $adjacent_start, $adjacent_end - $adjacent_start + 1);
    for my $i (0 .. length($substring) - 1) {
      if (substr($substring, $i, 1) eq '*') {
        push @gears, ($line_number - 1) . "," . ($adjacent_start + $i);
      }
    }
  }
  if ($line_number < $#input) {
    my $next_line = $input[$line_number + 1];
    my $substring = substr($next_line, $adjacent_start, $adjacent_end - $adjacent_start + 1);
    for my $i (0 .. length($substring) - 1) {
      if (substr($substring, $i, 1) eq '*') {
        push @gears, ($line_number + 1) . "," . ($adjacent_start + $i);
      }
    }
  }
  return @gears;
}

while (<>) {
  chomp;
  push @input, $_;
}

foreach my $line_number (0 .. $#input) {
  my $line = $input[$line_number];
  while ($line =~ /(\d+)/g) {
    my $digits = $1;
    my $start_column = pos($line) - length($digits);
    my $end_column = pos($line) - 1;
    foreach my $gear (adjacent_gears($line_number, $start_column, $end_column)) {
      push @{$gears{$gear}}, $digits;
    }
  }
}

for my $gear (keys %gears) {
  my @values = @{$gears{$gear}};
  if ($#values == 1) {
    print "Qualifying gear: $gear\n";
    $total += $values[0] * $values[1];
  }
}
print "$total\n";
