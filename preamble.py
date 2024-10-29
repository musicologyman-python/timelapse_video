'''
Utility script to be run at the beginning of a bpython session. Provides
namespace import for tkinter and quick access to documentation comments
through the docit function
'''
import inspect
import tkinter as tk

from toolz.functoolz import compose_left

# Create the docit function
docit = compose_left(inspect.getdoc, print)

