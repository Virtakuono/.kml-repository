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

echo "Backing up Jeddah Shopping..."
echo ""

mv JeddahShopping.kml JeddahShopping_old.kml

wget -O JeddahShopping.kml "https://maps.google.com/maps/ms?ie=UTF8&t=h&dg=feature&authuser=0&msa=0&output=kml&msid=203537519255214459478.0004863c2f62b04789ee3"

echo ""
echo "Done."

echo ""
echo "Difference of the old and new version of the file:"
echo ""

diff JeddahShopping.kml JeddahShopping_old.kml

echo "Backing up Thuwal map by Claire..."
echo ""

mv Thuwal.kml Thuwal_old.kml

wget -O Thuwal.kml "https://maps.google.com/maps/ms?hl=en&ie=UTF8&oe=UTF8&dg=feature&authuser=0&msa=0&output=kml&msid=216110785410091998621.0004a4de8ab547c2ca385"

echo ""
echo "Done."

echo ""
echo "Difference of the old and new version of the file:"
echo ""

diff Thuwal.kml Thuwal_old.kml


echo ""
echo "Commit and push if needed."
echo ""



