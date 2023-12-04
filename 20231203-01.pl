#!/usr/bin/perl

use warnings;
use strict;

my $total = 0;
my @input;

sub is_symbol_adjacent {
  my $line_number = shift;
  my $start_column = shift;
  my $adjacent_start = $start_column == 0 ? 0 : $start_column - 1;
  my $end_column = shift;
  my $adjacent_end = $end_column == length($input[$line_number]) - 1 ? $end_column : $end_column + 1;
  if ($start_column > 0 && substr($input[$line_number], $adjacent_start, 1) ne '.') {
    return 1;
  }
  if ($end_column < length($input[$line_number]) - 1 && substr($input[$line_number], $adjacent_end, 1) ne '.') {
    return 1;
  }
  if ($line_number > 0) {
    my $previous_line = $input[$line_number - 1];
    # print "checking slice: ", substr($previous_line, $adjacent_start, $adjacent_end - $adjacent_start + 1), "\n";
    if (substr($previous_line, $adjacent_start, $adjacent_end - $adjacent_start + 1) =~ /[^\.0-9]/) {
      return 1;
    }
  }
  if ($line_number < $#input) {
    my $next_line = $input[$line_number + 1];
    if (substr($next_line, $adjacent_start, $adjacent_end - $adjacent_start + 1) =~ /[^\.0-9]/) {
      return 1;
    }
  }
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
    if (is_symbol_adjacent($line_number, $start_column, $end_column)) {
      # print "Found adjacent symbols on line $line_number, columns $start_column to $end_column\n";
      $total += $digits;
    }
  }
}

print "$total\n";
