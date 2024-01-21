#!/usr/bin/env python3


#How to use:
#1: create secondary structure drawing in RNA2D drawer
#2: select all bases with corresponding reacitivity data that you want to color and turn the outline on for these bases. The color of the outline does not matter.
#3: this file as a .rnacanvas file
#4: format the reactivity profile file in the same format as the example file
#5:run this script on that .rnacanvas with a reactivity profile
#python color_reactivities_RNA2D_drawer.py /path/to/your/reactivity_data.txt /path/to/your/test.rnacanvas /path/to/your/modified.rnacanvas


#set color transitions from grey to yellow to red by adjusting the following paramaters:
#--yellow-transition 0.5 --red-transition 1.0

#example:

#/Users/maximoleynikov/Desktop/python_scripts/color_reactivities_RNA2D_drawer.py /Users/maximoleynikov/Desktop/Spinach_M2_DAGGER_DANCE-reactivities_edited.normalized.txt /Users/maximoleynikov/Desktop/spinach_4TS2_secondary_structure.rnacanvas /Users/maximoleynikov/Desktop/spinach_M2_dagger_mut_rates.rnacanvas --yellow-transition 0.5 --red-transition 1.0

import argparse
import json
import re

def parse_reactivity_file(filename):
    reactivity_scores = []
    max_score = 0
    with open(filename, 'r') as file:
        next(file)  # skip header line
        for line in file:
            _, _, raw = line.strip().split('\t')
            score = float(raw)
            reactivity_scores.append(score)
            max_score = max(max_score, score)
    return reactivity_scores, max_score

def parse_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def score_to_color(score, yellow_transition, red_transition):
    if score == 0:
        return '#ffffff'  # white

    # Ensure the score is in the range [0, 1]
    score = max(0, min(1, score))

    if score < yellow_transition:
        # Gray to Yellow transition
        factor = score / yellow_transition  # rescale to [0, 1]
        red = green = int(128 + factor * (255 - 128))
        blue = int(128 * (1 - factor))
    elif score < red_transition:
        # Yellow to Red transition
        factor = (score - yellow_transition) / (red_transition - yellow_transition)  # rescale to [0, 1]
        red = 255
        green = int(255 * (1 - factor))
        blue = 0
    else:
        # Maximum reactivity, fully red
        red, green, blue = 255, 0, 0

    # Convert to hexadecimal
    color = '#{:02x}{:02x}{:02x}'.format(red, green, blue)

    return color


def replace_fill_color(svg, circle_id, color):
    return re.sub(f'(?<=id="{circle_id}" ).*?(?= fill-opacity)', f'stroke="{color}" stroke-width="1" stroke-opacity="1" fill="{color}"', svg)

def update_base_colors(json_data, reactivity_scores, max_score, yellow_transition, red_transition):
    svg = json_data["drawing"]["svg"]

    for i, base in enumerate(json_data["drawing"]["sequences"][0]["bases"]):
        if "outline" in base and base["outline"]["className"] == "CircleBaseOutline":
            score = reactivity_scores[i] / max_score  # normalize score
            color = score_to_color(score, yellow_transition, red_transition)
            svg = replace_fill_color(svg, base["outline"]["circleId"], color)
    json_data["drawing"]["svg"] = svg

def save_json_file(json_data, filename):
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=2)

def main():
    parser = argparse.ArgumentParser(description='Update colors of bases in .rnacanvas file based on reactivity scores.')
    parser.add_argument('reactivity_file', help='Path to the reactivity data file')
    parser.add_argument('json_file', help='Path to the .rnacanvas file')
    parser.add_argument('output_file', help='Path to save the modified .rnacanvas file')
    parser.add_argument('--yellow-transition', type=float, default=0.5, help='Score value where the color starts transitioning to yellow.')
    parser.add_argument('--red-transition', type=float, default=1.0, help='Score value where the color starts transitioning to red.')


    args = parser.parse_args()

    reactivity_scores, max_reactivity_score = parse_reactivity_file(args.reactivity_file)
    json_data = parse_json_file(args.json_file)

    update_base_colors(json_data, reactivity_scores, max_reactivity_score, args.yellow_transition, args.red_transition)

    save_json_file(json_data, args.output_file)

if __name__ == "__main__":
    main()
