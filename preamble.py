#!/usr/bin/env python3
import inspect
import tkinter as tk

from toolz.functoolz import compose_left

docit = compose_left(inspect.getdoc, print)

