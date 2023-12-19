use strict;
use warnings;

package Ranges;


sub map_range {
  my $rangeref = shift;
  my $mapref = shift;

  if (ref $rangeref->[0] eq 'ARRAY') {
    my @result = ();
    for my $range (@$rangeref) {
      my $mapped_range = map_range($range, $mapref);
      push @result, @$mapped_range;
    }
    return \@result;
  }

  my $start_range = $rangeref->[0];
  my $range_count = $rangeref->[1];

  for my $map (@$mapref) {
    my ($map_dest, $map_start, $map_count) = @$map;
    # case 0: range is within map range
    if ($start_range >= $map_start && $start_range + $range_count <= $map_start + $map_count) {
      return [[$map_dest + $start_range - $map_start, $range_count]];
    }
    # case 1: range is before map range
    if ($start_range + $range_count - 1 < $map_start) {
      next;
    } elsif ($start_range + 1 > $map_start + $map_count) {
      # case 2: range is after map range
      next;
    } else {
      # Divide input into up to three parts: before, within, after
      my @result = ();
      if ($start_range < $map_start) {
        my $before_count = $map_start - $start_range;
        my @before = ($start_range, $before_count);
        push @result, @{map_range(\@before, $mapref)};
        $start_range = $map_start;
        $range_count -= $before_count;
      }
      if ($start_range + $range_count > $map_start + $map_count) {
        my $after_count = $start_range + $range_count - $map_start - $map_count;
        my @after = ($start_range + $range_count - $after_count, $after_count);
        push @result, @{map_range(\@after, $mapref)};
        $range_count -= $after_count;
      }
      # we're left with a case in which the range is within the map range
      push @result, [$map_dest + $start_range - $map_start, $range_count];
      return \@result;
    }
  }
  # no maps matched, return the original range
  return [$rangeref];
}

1;
