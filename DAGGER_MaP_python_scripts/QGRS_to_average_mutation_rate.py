#!/usr/bin/env python3

import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Function to extract the positions of lowercase g's in a sequence
def extract_lowercase_g_positions(sequence, start_position):
    return [start_position + i for i, char in enumerate(sequence) if char == 'g']

# Function to calculate the average mutation rate for given positions of lowercase 'g's in a sequence
def calculate_average_mutation_rate_for_sequence(g_positions, reactivity_df):
    mutation_rates = reactivity_df[reactivity_df['Nucleotide'].isin(g_positions)]['Modified_rate']
    return mutation_rates.mean() if not mutation_rates.empty else None

# Read the HTML file
html_file_path = '/path/to/your/html/file.html'  # Replace with your file path
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')
tables = soup.find_all('table')

# Process the QGRS sequences from the HTML table
def process_qgrs_sequences(table):
    sequences = []
    for row in table.find_all('tr')[1:]:  # Skipping the header row
        cells = row.find_all('td')
        qgrs_cell = cells[2]  # QGRS column
        sequence = ''
        for part in qgrs_cell:
            if part.name == 'u':  # Underlined text
                sequence += part.get_text().lower()  # Convert underlined Gs to lowercase
            else:
                sequence += str(part)  # Non-underlined text
        sequences.append(sequence)
    return sequences

# Extract and process sequences
processed_sequences = process_qgrs_sequences(tables[0])

# Adjust positions by adding 80
position_values = [int(row.find('td').get_text()) + 80 for row in tables[0].find_all('tr')[1:]]
adjusted_sequences = [{"position": pos, "sequence": seq} for pos, seq in zip(position_values, processed_sequences)]

# Load the chemical reactivity data
reactivity_file = '/path/to/your/reactivity/data.txt'  # Replace with your file path
reactivity_df = pd.read_csv(reactivity_file, sep='\t')

# Calculate average mutation rates
all_lowercase_g_positions = [extract_lowercase_g_positions(seq_data['sequence'], seq_data['position']) for seq_data in adjusted_sequences]
all_average_mutation_rates = [calculate_average_mutation_rate_for_sequence(g_pos, reactivity_df) for g_pos in all_lowercase_g_positions]

# Add the average mutation rate to the data
for seq_data, avg_rate in zip(adjusted_sequences, all_average_mutation_rates):
    seq_data["average_mutation_rate"] = avg_rate

# Convert to DataFrame and export to Excel
export_df = pd.DataFrame(adjusted_sequences)
output_file_path = '/path/to/output/file.xlsx'  # Replace with your desired output path
export_df.to_excel(output_file_path, index=False)
