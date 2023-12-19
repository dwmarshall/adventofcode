use warnings;
use strict;

use lib '.';

use Test::More;

BEGIN { use_ok('Ranges') };

sub test_map_range_before {
  my $range = [0, 5];
  my $map = [[10, 20, 30]];
  my $result = Ranges::map_range($range, $map);
  is_deeply($result, [[0, 5]]);
}

sub test_map_range_before_overlap {
  my $range = [10, 20];
  my $map = [[25, 12, 30]];
  my $result = Ranges::map_range($range, $map);
  is_deeply($result, [[10, 2], [25, 18]]);
}

sub test_map_range_after {
  my $range = [40, 5];
  my $map = [[10, 20, 10]];
  my $result = Ranges::map_range($range, $map);
  is_deeply($result, [[40, 5]]);
}

sub test_map_range_after_overlap {
  my $range = [35, 10];
  my $map = [[10, 20, 20]];
  my $result = Ranges::map_range($range, $map);
  is_deeply($result, [[40, 5], [25, 5]]);
}

sub test_map_range_within {
  my $range = [15, 5];
  my $map = [[25, 10, 10]];
  my $result = Ranges::map_range($range, $map);
  is_deeply($result, [[30, 5]]);
}

sub test_map_range_spanning {
  my $range = [10, 40];
  my $map = [[5, 20, 10]];
  my $result = Ranges::map_range($range, $map);
  is_deeply($result, [[10, 10], [30, 20], [5, 10]]);
}

sub test_multiple_ranges {
  my $ranges = [[10, 20], [30, 40]];
  my $map = [[0, 12, 2]];
  # check in pieces
  my $first = Ranges::map_range([10, 2], $map);
  is_deeply($first, [[10, 2]]);
  my $second = Ranges::map_range([12, 18], $map);
  is_deeply($second, [[14, 16], [0, 2]]);
  my $third = Ranges::map_range([30, 40], $map);
  is_deeply($third, [[30, 40]]);
  my $result = Ranges::map_range($ranges, $map);
  is_deeply($result, [[10, 2], [14, 16], [0, 2], [30, 40]]);
}

sub test_multiple_maps {
  my $range = [15, 5];
  my $map = [[5, 10, 1], [35, 10, 10]];
  my $result = Ranges::map_range($range, $map);
  is_deeply($result, [[40, 5]]);
}

test_map_range_before();
test_map_range_before_overlap();
test_map_range_after();
test_map_range_after_overlap();
test_map_range_within();
test_map_range_spanning();
test_multiple_ranges();
test_multiple_maps();
done_testing;
