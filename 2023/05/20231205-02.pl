#!/usr/bin/perl

use warnings;
use strict;

use lib '.';
use Ranges;
use List::Util qw/min/;

sub extract_map {
  my $linesref = shift;
  my $map_name = shift;
  my @map;
  my $line = 0;
  $line++ until $linesref->[$line] =~ /^$map_name/;
  while (defined $linesref->[$line] && $linesref->[++$line] =~ /(\d+)\s+(\d+)\s+(\d+)/) {
    push @map, [$1, $2, $3];
  }
  return \@map;
}


my @lines = <STDIN>;

my $line = 0;
my @seeds;

$line++ until $lines[$line] =~ /^seeds:\s+(.*)/;
@seeds = split /\D+/, $1;

my $seed_to_soil = extract_map(\@lines, 'seed-to-soil');
my $soil_to_fertilizer = extract_map(\@lines, 'soil-to-fertilizer');
my $fertilizer_to_water = extract_map(\@lines, 'fertilizer-to-water');
my $water_to_light = extract_map(\@lines, 'water-to-light');
my $light_to_temperature = extract_map(\@lines, 'light-to-temperature');
my $temperature_to_humidity = extract_map(\@lines, 'temperature-to-humidity');
my $humidity_to_location = extract_map(\@lines, 'humidity-to-location');

my @locations;

my $seed_count = 0;
while (@seeds) {
  my @seed_range = splice @seeds, 0, 2;
  $seed_count++;
  my $soil = Ranges::map_range(\@seed_range, $seed_to_soil);
  # print "soil $soil, ";
  my $fertilizer = Ranges::map_range($soil, $soil_to_fertilizer);
  # print "fertilizer $fertilizer, ";
  my $water = Ranges::map_range($fertilizer, $fertilizer_to_water);
  # print "water $water, ";
  my $light = Ranges::map_range($water, $water_to_light);
  # print "light $light, ";
  my $temperature = Ranges::map_range($light, $light_to_temperature);
  # print "temperature $temperature, ";
  my $humidity = Ranges::map_range($temperature, $temperature_to_humidity);
  # print "humidity $humidity, ";
  my $location = Ranges::map_range($humidity, $humidity_to_location);
  # print "location $location\n";
  push @locations, @$location;
}

print min(map { $_->[0] } @locations), "\n";
