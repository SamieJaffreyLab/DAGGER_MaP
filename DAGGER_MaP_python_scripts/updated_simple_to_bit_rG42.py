#!/usr/bin/env python3


#all lower case letters in the fasta file will have their bits inverted in the bitvector. This signals to folding software that sequencing reads in which these bases are not mutated will be flagged as single stranded because they are likely engaged in tertiary interactions and reads in which these positions are mutated are flagged as availible for base pairing.

#All uppercase Gs in the fasta will be set to unpaired as N7 reactivity does not correlate with base pairedness

#This could probably be modified to include other bases but we need the A,C,U reactivity to establish base pairing constraints / single standed regions


#python process_mut_simple.py input.mut.simple input.fasta
#python simple_to_bit.py /home/maxim/smStructure_seq/test_conversion_data/pUG_test.mut.simple /home/maxim/smStructure_seq/test_conversion_data/pUG_SC.fa

#python simple_to_bit_wcase.py /home/maxim/smStructure_seq/test_conversion_data/pUG_test.mut.simple /home/maxim/smStructure_seq/test_conversion_data/pUG_SC.fa

#python simple_to_bit_rG4.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1I/TD1I_vs_control_Modified_HMOX1_parsed.mut.simple /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1I/HMOX1_3UTR_rG4.fa



import sys
from Bio import SeqIO


def pad_mutation_string(left_pos, right_pos, mutation_str, sequence_length):
    zeros_prefix = "0" * left_pos
    zeros_suffix = "0" * (sequence_length - right_pos - 1)
    return zeros_prefix + mutation_str + zeros_suffix

def read_fasta_file(fasta_file):
    with open(fasta_file, "r") as f:
        seq_record = list(SeqIO.parse(f, "fasta"))[0]
        return str(seq_record.seq)

def set_lowercase_bitvectors(fasta_sequence, bitvector):
    new_bitvector = list(bitvector)
    for i, char in enumerate(fasta_sequence):
        if char.islower():
            new_bitvector[i] = '0' if new_bitvector[i] == '1' else '1'
    return ''.join(new_bitvector)

def set_capital_G_bits_zero(fasta_sequence, bitvector):
    new_bitvector = list(bitvector)
    for i, char in enumerate(fasta_sequence):
        if char == 'G':
            new_bitvector[i] = '0'
    return ''.join(new_bitvector)

def process_file(input_file, fasta_file):
    fasta_sequence = read_fasta_file(fasta_file)
    fasta_length = len(fasta_sequence)

        # Pad the mutation strings as necessary
    bitvector = pad_mutation_string(int(data[0]), int(data[1]), bitvector, fasta_length)


    with open(input_file, "r") as f:
        lines = f.readlines()

    total_bitvectors = 0
    filtered_lines = []
    for line in lines:
        data = line.strip().split("\t")

        if len(data) != 3:
            continue

        total_bitvectors += 1
        bitvector = data[2]

        if len(bitvector) != fasta_length:
            continue

        if sum(map(int, bitvector)) < 2:
            continue

        bitvector = set_lowercase_bitvectors(fasta_sequence, bitvector)
        bitvector = set_capital_G_bits_zero(fasta_sequence, bitvector)

        filtered_lines.append(bitvector)

    print(f"Total bitvectors read: {total_bitvectors}")
    print(f"Bitvectors remaining after filtering: {len(filtered_lines)}")
    return filtered_lines

def write_output_file(output_file, filtered_bitvectors):
    with open(output_file, "w") as f:
        for i, bitvector in enumerate(filtered_bitvectors):
            f.write(f"bitvector_{i}\t")
            f.write("\t".join(bitvector))
            f.write("\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <reference_fasta_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    fasta_file = sys.argv[2]
    output_file = input_file.replace(".simple", ".bit")

    filtered_bitvectors = process_file(input_file, fasta_file)
    write_output_file(output_file, filtered_bitvectors)
