#!/usr/bin/env python
import numpy as np

sample_data = np.loadtxt(   # <1>
    "../DATA/columns_of_numbers.txt",
    skiprows=1,
    dtype=float
)

sample_data  /= 10  # <2>

file_name = 'save_data_float.txt'

np.savetxt(file_name, sample_data, delimiter=",", fmt="%5.2f")  # <3>

file_name = 'save_data_int.txt'

np.savetxt(file_name, sample_data, delimiter=",", fmt="%d")  # <4>
