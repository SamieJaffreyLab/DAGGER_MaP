#!/usr/bin/env python3

#to run the program, first make sure you change the location of the following python scripts:
#sizer_to_BPSEQ.py
#fetch_bit_bpseq.py
#location of contrafold program

#given K means clusters from DaVinci, we need to retrieve their structures by extracting their bit information from the sizer.tab file and then refolding them with ContraFold

## When this python script is run from the scripts folder it creates two new folders in the directory you are in when the program is run called folded and posteriors output.
#This is where the folded files are

#The script has to be run with 3 clusters at a time. If only 1 or two clusters, then choose a random bit for cluster 3. If more than 3 clusters, run the program twice to extract the correct structures

#python /home/maxim/maxim_py_programs/fetch_DaVinci_folded.py --size_file /home/maxim/smStructure_seq/DM7_data/DM7_rG4_folded/sizer2.tab --fasta_file /home/maxim/DanceMapper/DanceMap_data/Fasta_templates/rG4_constrained/spinach_SC_rG4_constrained.fa --out_file /home/maxim/smStructure_seq/DM7_data/DM7_rG4_folded/sizer_cluster2.bpseq --cluster_1_name bit_3041 --cluster_2_name bit_164 --cluster_3_name bit_1


import sys
import os
import argparse
import subprocess

def handler():
    """
    Get command line inputs
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size_file", type=str, )  # required=True)
    parser.add_argument("-f", "--fasta_file", type=str, )  # , required=True)
    parser.add_argument("-o", "--out_file", type=str, )  # , required=True)
    parser.add_argument("-1", "--cluster_1_name", type=str, )  # , required=True)
    parser.add_argument("-2", "--cluster_2_name", type=str, )  # , required=True)
    parser.add_argument("-3", "--cluster_3_name", type=str, )  # , required=True)

    parser.set_defaults(bit_file='sizer.tab',
                        fasta_file='cool6.fasta',
                        cluster_1_name='bit_1',
                        cluster_2_name='bit_2',
                        cluster_3_name='bit_3')

    return parser.parse_args()

if __name__ == "__main__":
    args = handler()

    os.makedirs('folded', exist_ok=True)
    os.makedirs('posteriors_output', exist_ok=True)

    # Convert size file to BSEQ encoded file
    subprocess.run(["python", "/home/maxim/maxim_py_programs/sizer_to_BPSEQ.py", args.size_file, args.fasta_file, args.out_file])

    # Fetch BPSEQ file for cluster 1
    subprocess.run(["python", "/home/maxim/maxim_py_programs/fetch_bit_bpseq.py", args.out_file, args.out_file + args.cluster_1_name, ">" + args.cluster_1_name])

    # Fetch BPSEQ file for cluster 2
    subprocess.run(["python", "/home/maxim/maxim_py_programs/fetch_bit_bpseq.py", args.out_file, args.out_file + args.cluster_2_name, ">" + args.cluster_2_name])

    # Fetch BPSEQ file for cluster 3
    subprocess.run(["python", "/home/maxim/maxim_py_programs/fetch_bit_bpseq.py", args.out_file, args.out_file + args.cluster_3_name, ">" + args.cluster_3_name])

    constraint_1 = args.out_file + args.cluster_1_name
    constraint_2 = args.out_file + args.cluster_2_name
    constraint_3 = args.out_file + args.cluster_3_name

    # Fold cluster 1
    result = subprocess.run(["/home/maxim/contrafold/src/contrafold", "predict", "--constraints", constraint_1, '--parens', 'folded/' + args.cluster_1_name + '.fold', '--posteriors', '0.0', 'posteriors_output/' + args.cluster_1_name + '.txt'], capture_output=True, text=True)
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

    # Fold cluster 2
    result = subprocess.run(["/home/maxim/contrafold/src/contrafold", "predict", "--constraints", constraint_2, '--parens', 'folded/' + args.cluster_2_name + '.fold', '--posteriors', '0.0', 'posteriors_output/' + args.cluster_2_name + '.txt'], capture_output=True, text=True)
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

    # Fold cluster 3
    result = subprocess.run(["/home/maxim/contrafold/src/contrafold", "predict", "--constraints", constraint_3, '--parens', 'folded/' + args.cluster_3_name + '.fold', '--posteriors', '0.0', 'posteriors_output/' + args.cluster_3_name + '.txt'], capture_output=True, text=True)
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
