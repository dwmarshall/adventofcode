#!/usr/bin/perl

use warnings;
use strict;

use List::Util qw(sum);

my @cards;

while (<>) {
    chomp;
    s/^Card\s+(\d+):\s+//;
    my $card = $1;
    $cards[$card]++;
    my ($winning_numbers, $these_numbers) = split /\|\s*/;
    my @numbers;
    foreach my $winner (split /\s+/, $winning_numbers) {
        $numbers[$winner] = 1;
    }
    my $matches = 0;
    foreach my $number (split /\s+/, $these_numbers) {
        if ($numbers[$number]) {
            $matches++;
        }
    }
    if ($matches > 0) {
        for (my $i = 1; $i <= $matches; $i++) {
            $cards[$card + $i] += $cards[$card];
        }
    }
}

print "Total: ", sum(grep { defined } @cards), "\n";
