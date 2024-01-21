#!/usr/bin/env python

#ring and pair file to heatmap

#python /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py input.txt

#python /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/DANCE_MaP_analysis/Spinach/Spinach_M2_DAGGER_pop_average-0-rings.txt


#python /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/DANCE_MaP_analysis/CPOX/CPOX_Li_plus_heme_pop_average-0-rings.txt

#python /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1N/TD1N_rings.txt

#python /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1N/TD1N_fit-3-allcorrs.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1_all_DAGGER_samples/TD1_all_rings_vs_control.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1_all_DAGGER_samples/TD1_all_rings_vs_KBH4.txt

#/home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1_all_DAGGER_samples/TD1_all_vs_control_pairs.txt-allcorrs.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1_all_DAGGER_samples/TD1_all_vs_control_pairs.txt-pairmap.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1_all_DAGGER_samples/TD1_all_vs_KBH4_pairs.txt-allcorrs.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1_all_DAGGER_samples/TD1_all_vs_KBH4_pairs.txt-pairmap.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1N/TD1N_pairmap.txt-allcorrs.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1N/TD1N_pairmap.txt-pairmap.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1_all_DAGGER_samples/TD1_all_fit_all_bases-0-rings.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1_all_DAGGER_samples/TD1_all_fit_all_bases-4-rings.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1_all_DAGGER_samples/TD1_all_TC_CT_filtered.txt

#python3 /home/maxim/maxim_py_programs/ring_pair_to_heatmap.py /home/maxim/Dagger_seq_data/in_vivo_experiments/AKT2_3UTR/SH_SY5Y_cells/Aligned_data/AKT2_DAGGER_CT_TC_filtered_rings.txt

import sys
import os

import numpy as np

def read_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    matrix_size = int(lines[0].split('\t')[0])
    matrix = np.zeros((matrix_size, matrix_size))

    for line in lines[2:]:
        data = line.split('\t')
        i, j, value, sign = int(data[0]), int(data[1]), float(data[2]), int(data[3])
        if sign >= 0:
            # Subtracting 1 to transform to 0-indexed
            matrix[i-1][j-1] = value
            matrix[j-1][i-1] = value

    return matrix

def write_data(matrix, file_path):
    with open(file_path.replace('.txt', '.heatmap.txt'), 'w') as f:
        for row in matrix:
            row_str = '\t'.join(str(val) for val in row)
            f.write(row_str + '\n')

def main():
    file_path = sys.argv[1]
    matrix = read_data(file_path)
    write_data(matrix, file_path)

if __name__ == "__main__":
    main()
