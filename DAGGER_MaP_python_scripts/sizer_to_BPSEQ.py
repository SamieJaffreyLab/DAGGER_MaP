#!/usr/bin/env python3

#converts sizer.tab file into BPSEQ containting file for quick retrieval of BPSEQ contraints after Kmeans clustering

#python /home/maxim/maxim_py_programs/sizer_to_BPSEQ.py /home/maxim/smStructure_seq/TH_R15_data/minus_aciclovir/sizer.tab /home/maxim/smStructure_seq/TH_R15_data/minus_aciclovir/TH_R15_SC.fa /home/maxim/smStructure_seq/TH_R15_data/minus_aciclovir/sizer.bpseq




import sys

def read_data_file(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip().split('\t') for line in file.readlines()]
    return data

def process_data(data):
    processed_data = []
    for row in data:
        new_row = [row[0], int(row[1])]
        processed_row = [0 if x == "1" else -1 for x in row[2]]
        new_row.append(processed_row)
        processed_data.append(new_row)
    return processed_data

def create_bpseq_data(sequence, processed_data):
    bpseq_data = []
    for row in processed_data:
        seq_bpseq = []
        for i, value in enumerate(row[2]):
            seq_bpseq.append([i + 1, sequence[i], value])
        bpseq_data.append(seq_bpseq)
    return bpseq_data

def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        sequence = ''.join([line.strip() for line in file.readlines() if not line.startswith('>')])
    return sequence

def write_output_file(output_file_path, row_names, bpseq_data):
    with open(output_file_path, 'w') as output_file:
        for row_name, seq_bpseq in zip(row_names, bpseq_data):
            output_file.write(f">{row_name}\n")
            for bpseq_row in seq_bpseq:
                output_file.write(f"{bpseq_row[0]}\t{bpseq_row[1].lower()}\t{bpseq_row[2]}\n")


if __name__ == "__main__":
    input_data_file = sys.argv[1]
    input_fasta_file = sys.argv[2]
    output_file_path = sys.argv[3]

    data = read_data_file(input_data_file)
    sequence = read_fasta_file(input_fasta_file)
    processed_data = process_data(data)
    bpseq_data = create_bpseq_data(sequence, processed_data)

    row_names = [row[0] for row in data]
    write_output_file(output_file_path, row_names, bpseq_data)
