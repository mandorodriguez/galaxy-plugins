#!/usr/bin/env python3

import os, sys
import pdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help="A file with the annotations and deletions.")

args = parser.parse_args()

ad_file = args.file


with open(ad_file,'r') as adf:

    table_lines = adf.readlines()


min_indx = 4
max_indx = 5

header = table_lines[0].split('\t')

#if len(header) == 38:
#    header = header[0:3] + ["minimum","maximum"] + header[4:]
header = table_lines[0]

min_num_column_indx = 1
max_num_column_indx = 2

max_vals = []
min_vals = []

#-------------------------------------------------------------------

def collect_groups(val_list):

    groups = []
    this_group = []
    last = None
    for i,mx in enumerate(val_list):

        if last is None:
            last = mx

        if mx > last+1:
            if len(this_group) > 2:
                print("appending {} items".format(len(this_group)))
            groups.append(this_group)
            this_group = []
        
        this_group.append(mx)
        last = mx

    return groups

#-----------------------------------------------------------------

# Going to collect the lists as numbers first.
for index,line in enumerate(table_lines[1:]):

    line_parts = line.split('\t')

    max_vals.append(int(line_parts[max_num_column_indx]))
    min_vals.append(int(line_parts[min_num_column_indx]))



# groups = []
# this_group = []
# last = None
# for i,mx in enumerate(max_vals):

#     if last is None:
#         last = mx

#     if mx > last+1:
#         groups.append(this_group)
#         this_group = []
        
#     this_group.append(mx)
#     last = mx

print("Collecting max groups\n")
max_groups = collect_groups(max_vals)
print("\n\nCollecting min groups\n")
min_groups = collect_groups(min_vals)



# consolidate the arrays
max_list = []
for this_group in max_groups:
    this_max = max(this_group)
    for k in this_group:
        max_list.append(this_max)


min_list = []
for this_group in min_groups:
    this_min = min(this_group)
    for k in this_group:
        min_list.append(this_min)



num = 0
output_file = "max-min-annotations-deletions.tsv"
with open(output_file,"w") as of:

    of.write(header)
    
    for index,line in enumerate(table_lines[1:]):
        num += 1

        try:
            line_parts = line.rstrip().split('\t')
            #pdb.set_trace()
            new_string = line_parts[0:4] + [ str(min_list[index]), str(max_list[index]) ] + line_parts[6:]
            #pdb.set_trace()
            of.write("{}\n".format("\t".join(new_string)))
        except IndexError:
            pass

print("output file in {}".format(output_file))
