#!/bin/bash

echo "Downloading google docs sheet" 

echo "Backing up Jeddah - Interested locations..."

wget -q -O JeddahPOIs.ods "https://docs.google.com/spreadsheets/d/1-34A8wdzOaiz36Mnx74PbDsaRGTcCZP92rPLV9aP3fM/export?hl=en&exportFormat=ods" 

mv JeddahInterestedLocations.kml JeddahInterestedLocations_old.kml

wget -q -O JeddahInterestedLocations.kml "https://maps.google.com/maps/ms?dg=feature&ie=UTF8&authuser=0&msa=0&output=kml&msid=203555040976874160945.0004cf9d6a73b19256e5f"

echo "Done."

echo "Difference of the old and new version of the file:"

diff JeddahInterestedLocations.kml JeddahInterestedLocations_old.kml

echo "Backing up Jeddah Shopping..."

mv JeddahShopping.kml JeddahShopping_old.kml

wget -q -O JeddahShopping.kml "https://maps.google.com/maps/ms?ie=UTF8&t=h&dg=feature&authuser=0&msa=0&output=kml&msid=203537519255214459478.0004863c2f62b04789ee3"

echo "Done."

echo "Difference of the old and new version of the file:"

diff JeddahShopping.kml JeddahShopping_old.kml

echo "Backing up Thuwal map by Claire..."

mv Thuwal.kml Thuwal_old.kml

wget -q -O Thuwal.kml "https://maps.google.com/maps/ms?hl=en&ie=UTF8&oe=UTF8&dg=feature&authuser=0&msa=0&output=kml&msid=216110785410091998621.0004a4de8ab547c2ca385"

echo "Done."

echo "Difference of the old and new version of the file:"

diff Thuwal.kml Thuwal_old.kml

echo "Commit and push if needed."



