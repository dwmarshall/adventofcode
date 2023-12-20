use strict;
use warnings;

package Cards;

use List::Util qw/max/;

use constant RANKS => '23456789TJQKA';

sub compare {
  my $a = shift;
  my $b = shift;

  if ($a eq $b) {
    return 0;
  }

  # How many different labels are there?
  my %a_labels;
  $a_labels{$_}++ for split //, $a;
  my %b_labels;
  $b_labels{$_}++ for split //, $b;

  my $max_a = max(values %a_labels);
  my $max_b = max(values %b_labels);
  if ($max_a != $max_b) {
    return $max_b <=> $max_a;
  }

  # we might have a full house vs three of a kind
  if ($max_a == 3) {
    my $a_distinct = keys %a_labels;
    my $b_distinct = keys %b_labels;
    if ($a_distinct != $b_distinct) {
      return $a_distinct <=> $b_distinct;
    }
  }

  # we might have one pair vs two pair
  if ($max_a == 2) {
    # how many pairs do we have?
    my $a_pairs = grep { $a_labels{$_} == 2 } keys %a_labels;
    my $b_pairs = grep { $b_labels{$_} == 2 } keys %b_labels;
    if ($a_pairs != $b_pairs) {
      return $b_pairs <=> $a_pairs;
    }
  }


  # Compare the labels
  my @a_labels = split //, $a;
  my @b_labels = split //, $b;

  for my $i (0..$#a_labels) {
    if ($a_labels[$i] ne $b_labels[$i]) {
      return compare_labels($a_labels[$i], $b_labels[$i]);
    }
  }

  sub compare_labels {
    my $a = shift;
    my $b = shift;

    return index(RANKS(), $b) <=> index(RANKS(), $a);
  }

}

1;
