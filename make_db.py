#!/usr/bin/python
"""This function takes a FASTA file input and creates a searchable/ BLASTable database"""
__author__ = 'Robert Cooper (rdcooper408@gmail.com)'
__version__ = '0.0.1'


def make_db(input_file, output_file, db_type = "prot"):
    makeblastdb -in input_file -dbtype db_type -out output_file
    