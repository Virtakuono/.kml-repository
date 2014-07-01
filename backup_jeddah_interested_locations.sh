#!/bin/bash

#
# A script to backup the .kml file that contains the relevant information at
# http://goo.gl/maps/mFxL3
#
# 

echo "Backing up Jeddah - Interested locations..."
echo ""

mv JeddahInterestedLocations.kml JeddahInterestedLocations_old.kml

wget -O JeddahInterestedLocations.kml "https://maps.google.com/maps/ms?dg=feature&ie=UTF8&authuser=0&msa=0&output=kml&msid=203555040976874160945.0004cf9d6a73b19256e5f"

echo ""
echo "Done."

echo ""
echo "Difference of the old and new version of the file:"
echo ""

diff JeddahInterestedLocations.kml JeddahInterestedLocations_old.kml

echo ""
echo "Commit and push if needed."
echo ""

 

