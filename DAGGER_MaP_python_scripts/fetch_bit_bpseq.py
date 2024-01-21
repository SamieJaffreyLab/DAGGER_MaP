#!/usr/bin/env python3

#python /home/maxim/maxim_py_programs/fetch_bit_bpseq.py /home/maxim/smStructure_seq/TH_R15_data/minus_aciclovir/sizer.bpseq /home/maxim/smStructure_seq/TH_R15_data/minus_aciclovir/bit_7940.bpseq ">bit_7940"


import sys

def read_bpseq_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def extract_data_for_row_name(data, row_name):
    extracted_data = []
    found_row = False
    for line in data:
        if line.startswith('>'):
            #print(f"Row name in file: {line.strip()}")  # Debug line
            if found_row:
                break
            if line.strip() == row_name:
                found_row = True
                print(f"Found user-specified row name: {row_name}")  # Debug line
        elif found_row:
            extracted_data.append(line)
    return extracted_data
def write_extracted_data_to_file(output_file_path, extracted_data):
    with open(output_file_path, 'w') as output_file:
        for line in extracted_data:
            output_file.write(line)

if __name__ == "__main__":
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    user_specified_row_name = sys.argv[3]

    bpseq_data = read_bpseq_file(input_file_path)
    extracted_data = extract_data_for_row_name(bpseq_data, user_specified_row_name)
    print(f"Extracted data: {extracted_data}")  # Debug line
    write_extracted_data_to_file(output_file_path, extracted_data)
