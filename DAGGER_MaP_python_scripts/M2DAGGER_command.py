#!/usr/bin/env python

#edit the python scripts to have the proper directiory and location for this script to work

import sys
import os

# Check if the correct number of arguments were provided
if len(sys.argv) != 3:
    print("Please provide two arguments: .fa file and .mut file")
    sys.exit()

# Get the input files
fa_file = sys.argv[1]
mut_file = sys.argv[2]

# Create output filenames
simple_file = os.path.splitext(mut_file)[0] + ".simple"
m2map_file = os.path.splitext(mut_file)[0] + ".simple.M2MAP.txt"
zscores_file = os.path.splitext(mut_file)[0] + ".simple.M2MAP.Zscores.txt"

# Execute mut_to_simple.py
mut_to_simple_cmd = "python /home/maxim/maxim_py_programs/mut_to_simple.py {} {}".format(mut_file, simple_file)
os.system(mut_to_simple_cmd)

# Execute simple_to_M2_map.py
simple_to_m2map_cmd = "python3 /home/maxim/maxim_py_programs/simple_to_M2_map.py {} {} {}".format(fa_file, simple_file, m2map_file)
os.system(simple_to_m2map_cmd)

# Execute M2_Map_to_Zscores.py
m2map_to_zscores_cmd = "python3 /home/maxim/maxim_py_programs/M2_Map_to_Zscores.py {} {}".format(m2map_file, zscores_file)
os.system(m2map_to_zscores_cmd)
