#!/usr/bin/env python3

"""
This script copies the content of the NPY file
in the clipboard in a CSV.
This is intended to be pasted into a spreadsheet program.

If multiple files are selected, they will all be copied one
below the other, with a blank line separating them.
"""

import sys
import io
print("Python version:",sys.version)
print("Python interpreter:",sys.executable)
try:
    import numpy as np
    import time
    import pyperclip
    import csv

except ImportError as error:
    print(error)
    input("Press any key to exit")
    exit()


s = io.StringIO()
csvWriter = csv.writer(s)

for i in range(1,len(sys.argv)):
    file = sys.argv[i]
    A = np.load(file)
    if( A.ndim == 1):
        A = A.reshape([A.size,1])
    csvWriter.writerows(A)
    if i != len(sys.argv):
        csvWriter.writerows(' ')
pyperclip.copy(s.getvalue())

if sys.platform.startswith('linux'):
    input("Hit Enter to quit ...")
