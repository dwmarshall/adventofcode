#!/usr/bin/perl

use warnings;
use strict;

my $total = 0;

while (<>) {
    chomp;
    s/^Card\s+(\d+):\s+//;
    my $card = $1;
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
    if ($matches == 0) {
        # print "Card $card: No matches\n";
    } else {
        # print "Card $card is worth ", 2 ** ($matches - 1), "\n";
        $total += 2 ** ($matches - 1);
    }
}

print "Total: $total\n";
