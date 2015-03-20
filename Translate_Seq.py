#!/usr/bin/python
"""This function takes a FASTA file input and translates each sequence to a Protein"""
__author__ = 'Robert Cooper (rdcooper408@gmail.com)'
__version__ = '0.0.1'
###from 18.1.3 in biopython tutorial

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def translate_seq(input_file, output_file, input_file_type = "fasta", output_file_type = "fasta"):

    def make_protein_record(nuc_record):
        """Returns a new SeqRecord with the translated sequence (default table)."""
        return SeqRecord(seq = nuc_record.seq.translate(to_stop=True), \
            id = "trans_" + nuc_record.id, \
            description = "translation of CDS, using default table")
        
    proteins = (make_protein_record(nuc_rec) for nuc_rec in \
        SeqIO.parse(input_file, input_file_type))
    
    SeqIO.write(proteins, output_file, output_file_type)