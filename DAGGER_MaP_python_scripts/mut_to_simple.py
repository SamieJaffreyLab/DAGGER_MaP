#!/usr/bin/env python
#
#
#
#
#
#
#
#

import sys

# Get the name of the input file and the output file from the command line arguments
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
#
# Open the input file and the output file
#with open(input_file_name, "r") as input_file:
#    with open(output_file_name, "w") as output_file:
#        for line in input_file:
            # Split the line into columns using the tab character as a separator
#            columns = line.strip().split("\t")

            # Extract the desired columns
#            selected_columns = [columns[2], columns[3], columns[8]]

            # Write the selected columns to the output file, separated by a tab character
#            output_file.write("\t".join(selected_columns) + "\n")

with open(input_file_name, "r") as input_file:
    with open(output_file_name, "w") as output_file:
        for line in input_file:
            columns = line.strip().split("\t")
            if len(columns) >= 9:
                selected_columns = [columns[2], columns[3], columns[8]]
                output_file.write("\t".join(selected_columns) + "\n")


#command line:
# Go to cd /home/maxim/M2seq

#type the following command:
#python mut_to_simple.py inputfile_name_and_location inputfile_name_and_location_with.txt.simple at the end

#for M2 pUG Dagger map
#python mut_to_simple.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/pUG/pUG_M2_Dagger_v2.1.5_Modified_pUG_SC_parsed.mut /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/pUG/pUG_M2_Dagger_v2.1.5_Modified_pUG_SC_parsed.mut.simple


#for M2g4seq2:
#python mut_to_simple.py /home/maxim/DanceMapper/DanceMap_data/Spinach_M2_G4/M2_G4_seq2_Modified_spinach_SC_parsed.mut /home/maxim/DanceMapper/DanceMap_data/Spinach_M2_G4/M2_G4_seq2_Modified_spinach_SC_parsed.txt.simple





#For ADD riboswitch
#python mut_to_simple.py /home/maxim/DanceMapper/DanceMap_data/Spinach_M2_G4/M2_G4_seq2_Modified_spinach_SC_parsed.mut /home/maxim/DanceMapper/DanceMap_data/Spinach_M2_G4/M2_G4_seq2_Modified_spinach_SC_parsed.txt.simple

#python mut_to_simple.py /home/maxim/DanceMapper/DanceMap_data/DMS_footprinting/DM7_8_9_comb_Modified_spinach_SC_parsed.mut /home/maxim/DanceMapper/DanceMap_data/DMS_footprinting/DM7_8_9_comb_Modified_spinach_SC_parsed.mut.simple

#FOR M2 Dagger seq
#python mut_to_simple.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_Dagger_Modified_spinach_SC_parsed.mut /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_Dagger_Modified_spinach_SC_parsed.mut.simple

#python mut_to_simple.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_Dagger_v2.1.5_min0_Modified_spinach_SC_parsed.mut /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_Dagger_v2.1.5_min0_Modified_spinach_SC_parsed.mut.simple


#python mut_to_simple.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_DMS_MaP_Modified_spinach_SC_parsed.mut /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_DMS_MaP_Modified_spinach_SC_parsed.mut.simple



#python mut_to_simple.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_DMS_MaP_min0_Modified_spinach_SC_parsed.mut /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_DMS_MaP_min0_Modified_spinach_SC_parsed.mut.simple

#python mut_to_simple.py /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_Dagger_v2.2_min-_Modified_spinach_SC_parsed.mut /home/maxim/Dagger_seq_data/M2_Dagger_seq_experiment_1/Spinach/Spinach_M2_Dagger_v2.2_min-_Modified_spinach_SC_parsed.mut.simple


#for HMOX1 3UTR dagger
#python mut_to_simple.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1I/TD1I_vs_control_Modified_HMOX1_parsed.mut /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1I/TD1I_vs_control_Modified_HMOX1_parsed.mut.simple

#for HMOX1 3UTR DMS map
#python mut_to_simple.py /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1N/TD1N_vs_control_Modified_HMOX1_parsed.mut /home/maxim/PacBio_data/TD1_experiment_data/processed_data/TD1N/TD1N_vs_control_Modified_HMOX1_parsed.mut.simple

#python mut_to_simple.py /home/maxim/RNA_probing_datasets/mTOR_5UTR_SC/mTOR_5UTR_TGIRT_K_Modified_mTOR_5UTR_parsed.mut /home/maxim/RNA_probing_datasets/mTOR_5UTR_SC/mTOR_5UTR_TGIRT_K_Modified_mTOR_5UTR_parsed.mut.simple

#python mut_to_simple.py /home/maxim/RNA_probing_datasets/mTOR_5UTR_SC/mTOR_5UTR_TGIRT_Li_Modified_mTOR_5UTR_parsed.mut /home/maxim/RNA_probing_datasets/mTOR_5UTR_SC/mTOR_5UTR_TGIRT_Li_Modified_mTOR_5UTR_parsed.mut.simple
