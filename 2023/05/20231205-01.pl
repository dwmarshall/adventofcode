#!/usr/bin/perl

use warnings;
use strict;

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

sub get_from_map {
  my $mapref = shift;
  my $value = shift;
  for my $map (@$mapref) {
    if ($map->[1] <= $value && $value <= $map->[1] + $map->[2]) {
      return $map->[0] + $value - $map->[1];
    }
  }
  return $value;
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

for my $seed (@seeds) {
  print "Seed $seed, ";
  my $soil = get_from_map($seed_to_soil, $seed);
  print "soil $soil, ";
  my $fertilizer = get_from_map($soil_to_fertilizer, $soil);
  print "fertilizer $fertilizer, ";
  my $water = get_from_map($fertilizer_to_water, $fertilizer);
  print "water $water, ";
  my $light = get_from_map($water_to_light, $water);
  print "light $light, ";
  my $temperature = get_from_map($light_to_temperature, $light);
  print "temperature $temperature, ";
  my $humidity = get_from_map($temperature_to_humidity, $temperature);
  print "humidity $humidity, ";
  my $location = get_from_map($humidity_to_location, $humidity);
  print "location $location\n";
  push @locations, $location;
}

print min(@locations), "\n";
