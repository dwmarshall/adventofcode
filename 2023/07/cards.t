use warnings;
use strict;

use lib '.';

use Test::More;

BEGIN { use_ok 'Cards' };

is(Cards::compare('32T3K', '32T3K'), 0);
is(Cards::compare('32T3K', '32T3Q'), -1);
is(Cards::compare('32T3Q', '32T3K'), 1);
is(Cards::compare('32T3K', 'T55J5'), 1);
is(Cards::compare('KK677', 'KTJJT'), -1);
is(Cards::compare('KTJJT', 'T55J5'), 1);

# two pair
is(Cards::compare('22668', '22759'), -1);

# three of a kind vs full house
is(Cards::compare('33322', '33345'), -1);

my @hands = qw(32T3K T55J5 KK677 KTJJT QQQJA);

my @sorted = sort { Cards::compare($b, $a) } @hands;

is_deeply(\@sorted, [qw(32T3K KTJJT KK677 T55J5 QQQJA)]);

done_testing();
