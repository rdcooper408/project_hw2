#!/usr/bin/python
"""This function takes a FASTA file input and BLASTs against a downloaded database"""
__author__ = 'Robert Cooper (rdcooper408@gmail.com)'
__version__ = '0.0.1'


def BLASTX_db(input_sequence, output_file, database):
     blastx -query input_sequence -db database -out output_file -outfmt 5 -evalue 0.0001 -gapopen 11 -gapextend 1 -word_size 3 -matrix BLOSUM62 -num_alignments 20 -num_threads 4
    