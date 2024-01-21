#!/usr/bin/env python

#Normalizes DAGGER MaP data after DANCE MaP clustering

#to use this python program:
#First edit the dance MaP clustering output file to only have 4 columns as in the example file
#then use this script

#python /home/maxim/maxim_py_programs/normalize_DAGGER_DANCE.py input.txt

#python /home/maxim/maxim_py_programs/normalize_DAGGER_DANCE.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/DANCE_MaP_analysis/pUG/pUG_DANCE-reactivities_edited.txt

#python /home/maxim/maxim_py_programs/normalize_DAGGER_DANCE.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/DANCE_MaP_analysis/Spinach/Spinach_M2_DAGGER_DANCE-reactivities_edited.txt


import pandas as pd
import numpy as np
import os

def calculate_normalization_factors(input_file):
    data = pd.read_csv(input_file, sep='\t', skiprows=2, names=['Nt', 'Seq', 'nReact', 'Raw'])
    nucleotides = ['A', 'C', 'G', 'U']

    for nuc in nucleotides:
        subset = data[(data['Seq'] == nuc) & (data['Raw'].notna()) & (data['Raw'] != 'nan')]
        subset['Raw'] = subset['Raw'].astype(float)

        nf1_subset = subset
        nf2_subset = subset[subset['Raw'] > 0.001]  # Ignore if raw mutation rate is less than or equal to 0.001

        nf1 = nf1_subset['Raw'].quantile(np.arange(0.9, 0.95, 0.01)).mean()
        nf2 = nf2_subset['Raw'].quantile(0.75)

        print(f"Nucleotide: {nuc}, Normalization Factor 1: {nf1}, Normalization Factor 2: {nf2}")

        # Determine which normalization factor is larger
        normalization_factor = nf1 if nf1 > nf2 else nf2
        data.loc[(data['Seq'] == nuc), 'Normalization_Factor'] = normalization_factor

        # Divide raw reactivity by normalization factor
        data.loc[(data['Seq'] == nuc), 'Normalized_Raw'] = subset['Raw'] / normalization_factor

    # Determine output file path
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.normalized.txt"

    # Write to new file
    data.to_csv(output_file, sep='\t', index=False)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <input file>")
        sys.exit(1)

    input_file = sys.argv[1]
    calculate_normalization_factors(input_file)
