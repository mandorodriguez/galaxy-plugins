#!/bin/env python3
"""
Wrapper for isescan program. 

Works if the isescan program is set up to be executed on the command line via a
call to 'isescan'

"""
import argparse, os, sys
import pdb
import subprocess
import shutil
import glob

parser = argparse.ArgumentParser()

parser.add_argument("seqfile_path", type=str, help="a fasta file to process")


args = parser.parse_args()

seqfile_path = args.seqfile_path

result = subprocess.run(['/home/galaxy/bin/isescan', '--seqfile', seqfile_path, '--output', 'prediction'], stdout=subprocess.PIPE)

print(result.stdout.decode('utf-8'))

#seqfile_parts = seqfile_path.split('/')
#seqfile =  seqfile_parts[-1]

seqfile = os.path.split(seqfile_path)[-1]
prediction_dir = os.path.join('prediction', seqfile)
base_filename = os.path.join('prediction', seqfile)


# here we copy all the generated files to the top level so the plugin can see them

files = glob.glob("./prediction/**",recursive=True)

for f in files:
    print("Found output file {}".format(f))

    if f.endswith(".sum"):
        shutil.copy(f,"file.sum")
    elif f.endswith(".raw"):
        shutil.copy(f,"file.raw")
    elif f.endswith(".gff"):

        if 'proteome' in f:
            shutil.copy(f,"proteome.gff")
        else:
            shutil.copy(f,"file.gff")
    elif f.endswith(".out"):

        if 'proteome' in f:
            shutil.copy(f,"proteome.out")
        else:
            shutil.copy(f,"file.out")

    elif f.endswith(".is.fna"):
        shutil.copy(f,"file.is.fna")
    elif f.endswith(".orf.fna"):
        shutil.copy(f,"file.orf.fna")
    elif f.endswith(".orf.faa"):
        shutil.copy(f,"file.orf.faa")
        
for f in os.listdir():
    if 'file' in f:
        print("Produced output file: {}".format(f))


print("ISEscan wrapper done...")



 

