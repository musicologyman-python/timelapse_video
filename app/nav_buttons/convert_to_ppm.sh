#!/bin/bash

for f in *.svg; do
	magick $f -resize 107% ${f%%.svg}.ppm
done
