#!/usr/bin/env python3

#python M2_Map_to_Zscores.py input.txt output.txt

import sys
import argparse
import numpy as np

def read_input_file(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        num_bitvectors = int(lines[0].split()[-1])
        commutation_matrix = [list(map(float, line.strip().split()[1:])) for line in lines[2:]]
    return num_bitvectors, commutation_matrix

def normalize_rows(commutation_matrix):
    normalized_matrix = []
    for row in commutation_matrix:
        row_sum = sum(row)
        if row_sum != 0:
            normalized_matrix.append([value / row_sum for value in row])
        else:
            normalized_matrix.append(row)
    return normalized_matrix

def calculate_z_scores(normalized_matrix):
    means = np.mean(normalized_matrix, axis=0)
    std_devs = np.std(normalized_matrix, axis=0)

    z_scores = []
    for row in normalized_matrix:
        z_scores.append([(value - mean) / std_dev if std_dev != 0 else 0 for value, mean, std_dev in zip(row, means, std_devs)])

    return z_scores

def write_output_file(output_file, num_bitvectors, z_scores):
    with open(output_file, 'w') as f:
        f.write(f'Total number of bitvectors read in: {num_bitvectors}\n\n')
        for row in z_scores:
            for z_score in row:
                f.write(f'{z_score:.2f} ')
            f.write('\n')

def main():
    parser = argparse.ArgumentParser(description='Normalize rows and calculate Z-scores for bitvector positions.')
    parser.add_argument('input_file', help='Input file from the previous script.')
    parser.add_argument('output_file', help='Output file to store the results.')
    args = parser.parse_args()

    num_bitvectors, commutation_matrix = read_input_file(args.input_file)
    normalized_matrix = normalize_rows(commutation_matrix)
    z_scores = calculate_z_scores(normalized_matrix)
    write_output_file(args.output_file, num_bitvectors, z_scores)

if __name__ == '__main__':
    main()
