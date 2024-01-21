#!/usr/bin/env python3





#python simple_to_bit.py input.mut.simple input.fasta
#python simple_to_bit.py /home/maxim/smStructure_seq/test_conversion_data/pUG_test.mut.simple /home/maxim/smStructure_seq/test_conversion_data/pUG_SC.fa

#python simple_to_bit.py /home/maxim/DanceMapper/DanceMap_data/DMS_footprinting/DM7_8_9_comb_Modified_spinach_SC_parsed.mut.simple /home/maxim/DanceMapper/DanceMap_data/Fasta_templates/spinach_SC.fa

#python simple_to_bit.py /home/maxim/DanceMapper/Add_riboswitch/DMS_mode_aligned/wt_0_A_dms_mode_Modified_addWTfull_parsed.simple /home/maxim/DanceMapper/Add_riboswitch/GSE182552_alignment_sequences/add_wt.fa


import sys
from Bio import SeqIO

def read_fasta_file(fasta_file):
    with open(fasta_file, "r") as f:
        seq_record = list(SeqIO.parse(f, "fasta"))[0]
        return len(seq_record.seq)

def process_file(input_file, fasta_file):
    fasta_length = read_fasta_file(fasta_file)

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
