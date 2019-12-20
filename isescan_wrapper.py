#!/usr/bin/env python3 
"""
Wrapper for isescan program. 

Works if the isescan program is set up to be executed on the command line via a
call to 'isescan'

"""
import argparse, os, sys
import pdb
import subprocess
import shutil

parser = argparse.ArgumentParser()

parser.add_argument("seqfile_path", type=str, help="a fasta file to process")


args = parser.parse_args()

seqfile_path = args.seqfile_path

result = subprocess.run(['isescan', seqfile_path, 'proteome', 'hmm'], stdout=subprocess.PIPE)

print(result.stdout.decode('utf-8'))

seqfile_parts = seqfile_path.split('/')
seqfile =  seqfile_parts[-1]
prediction_dir = os.path.join('prediction', seqfile_parts[-2])

base_filename = os.path.join(prediction_dir, seqfile)

# here we copy all the generated files to the top level so the plugin can see them

shutil.copy("{}.sum".format(base_filename),"file.sum")
shutil.copy("{}.raw".format(base_filename),"file.raw")
shutil.copy("{}.gff".format(base_filename),"file.gff")
shutil.copy("{}.is.fna".format(base_filename),"file.is.fna")
shutil.copy("{}.orf.fna".format(base_filename),"file.orf.fna")
shutil.copy("{}.orf.faa".format(base_filename),"file.orf.faa")

 

