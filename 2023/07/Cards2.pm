use strict;
use warnings;

package Cards2;

use List::Util qw/max/;

use constant RANKS => 'J23456789TQKA';

sub compare {
  my $this_a = shift;
  my $this_b = shift;

  if ($this_a eq $this_b) {
    return 0;
  }

  if ($this_a eq 'JJJJJ') {
    return 1;
  } elsif ($this_b eq 'JJJJJ') {
    return -1;
  }

  # How many different labels are there?
  my %a_labels;
  $a_labels{$_}++ for split //, $this_a;
  my %b_labels;
  $b_labels{$_}++ for split //, $this_b;

  # move the jokers to the highest label's count
  if ($a_labels{'J'}) {
    my $jokers = delete $a_labels{'J'};
    my @ranks = sort { $a_labels{$b} <=> $a_labels{$a} } keys %a_labels;
    $a_labels{$ranks[0]} += $jokers;
  }
  if ($b_labels{'J'}) {
    my $jokers = delete $b_labels{'J'};
    my @ranks = sort { $b_labels{$b} <=> $b_labels{$a} } keys %b_labels;
    $b_labels{$ranks[0]} += $jokers;
  }

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
  my @a_labels = split //, $this_a;
  my @b_labels = split //, $this_b;

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
