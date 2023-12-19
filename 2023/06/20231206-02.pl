#!/usr/bin/perl
use warnings;
use strict;


sub ways {
  my $time = shift;
  my $goal = shift;
  my $ways = 0;
  for my $i (1..$time) {
    my $distance = $i * ($time - $i);
    if ($distance > $goal) {
      $ways++;
    }
  }
  return $ways;
}

my $time;
my $distance;
my $ways_to_win;

while (<>) {
  chomp;
  /^Time:/ && ($time = $_);
  /^Distance:/ && ($distance = $_);
}

$time =~ tr/0-9//cd; print "time: $time\n";
$distance =~ tr/0-9//cd; print "distance: $distance\n";

print ways($time, $distance), "\n"
