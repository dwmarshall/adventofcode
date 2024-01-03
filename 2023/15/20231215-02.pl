#!/usr/bin/perl
use warnings;
use strict;

use List::MoreUtils qw(firstidx);

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

my @hashmap;

my $total = 0;

for my $command (split /,/,$string) {
  my ($label) = $command =~ /(\w+)/;
  my $bucket = hash($label);
  my $index = firstidx { $_->[0] eq $label } @{$hashmap[$bucket]};
  if ($command =~ /=(\d+)/) {
    if ($index != -1) {
      $hashmap[$bucket][$index][1] = $1;
    } else {
      push @{$hashmap[$bucket]}, [$label, $1];
    }
  } else {
    if ($index != -1) {
      splice @{$hashmap[$bucket]}, $index, 1;
    }
  }
}

for (my $bucket = 0; $bucket < @hashmap; $bucket++) {
  next unless defined $hashmap[$bucket];
  next if @{$hashmap[$bucket]} == 0;
  my $subtotal = 0;
  for (my $i = 0; $i < @{$hashmap[$bucket]}; $i++) {
    $subtotal += ($bucket + 1) * ($i + 1) * $hashmap[$bucket][$i][1];
  }
  $total += $subtotal;
}

print "$total\n";
