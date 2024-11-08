#!/bin/bash

for f in *.svg; do
	magick $f -resize "64x64" ${f%%.svg}.jpg
done

