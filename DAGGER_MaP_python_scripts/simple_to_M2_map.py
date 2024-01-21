#!/usr/bin/env python3


#python simple_to_M2_map.py input_fasta.fasta input_simple.simple output.txt





import sys
import argparse
from Bio import SeqIO

def validate_input(line):
    columns = line.strip().split('\t')
    return len(columns) == 3

def filter_bitvectors(bitvectors, fasta_length):
    return [bitvector for bitvector in bitvectors if len(bitvector) == fasta_length]

def count_commutations(bitvectors):
    commutations = [[0 for _ in range(len(bitvectors[0]))] for _ in range(len(bitvectors[0]))]
    for bitvector in bitvectors:
        for i in range(len(bitvector)):
            if bitvector[i] == '1':
                for j in range(i+1, len(bitvector)):
                    if bitvector[j] == '1':
                        commutations[i][j] += 1
                        commutations[j][i] += 1
    return commutations

def main():
    parser = argparse.ArgumentParser(description='Count commutations in bitvectors.')
    parser.add_argument('fasta_file', help='Input FASTA file.')
    parser.add_argument('simple_file', help='Input .simple file with bitvectors.')
    parser.add_argument('output_file', help='Output file to store the results.')
    args = parser.parse_args()

    with open(args.fasta_file, 'r') as f:
        fasta_record = SeqIO.read(f, 'fasta')
        fasta_length = len(fasta_record.seq)

    with open(args.simple_file, 'r') as f:
        lines = [line.strip().split('\t')[2] for line in f if validate_input(line)]

    bitvectors = filter_bitvectors(lines, fasta_length)
    commutations = count_commutations(bitvectors)

    with open(args.output_file, 'w') as f:
        f.write(f'Total number of bitvectors read in: {len(bitvectors)}\n\n')
        for i, row in enumerate(commutations):
            f.write(f'{fasta_record.seq[i]}{i+1}: ')
            for j, col in enumerate(row):
                f.write(f'{col} ' if j != i else '0 ')
            f.write('\n')

if __name__ == '__main__':
    main()
