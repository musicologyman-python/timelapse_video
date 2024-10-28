#!/usr/bin/env python3

import argparse
from pathlib import Path

from lxml import etree

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=Path)
    args = parser.parse_args()

    

if __name__ == '__main__':
    main()
