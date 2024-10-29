#!/bin/bash

for f in *.svg; do
	magick $f -resize 160% ${f%%.svg}.png
done
