#! /bin/bash
######################## Blasting in the command terminal #########################
	# this commands builds a file directory and then downloads a huge database of 
	# rna reference sequence. I do not recommend doing this because it takes ~4 hours
	
	#here you extract the ncbi zipped file that creates a directory with executable files
	tar zxvpf ncbi-blast-2.2.30+-x64-linux.tar.gz
	
	#This puts the folder into the path for BASH to find when executing
    export PATH=”$PATH:$HOME/ncbi-blast-2.2.30+/bin”
    
    #this returns the path that you just created so that you can test that you created you
    echo $PATH
    
    #this creates a directory that you can download BLAST-able sequences into
    mkdir ./ncbi-blast-2.2.30+/db
    
    #this sets up the directory you made to be a BLAST-able DataBase
    export BLASTDB=”$HOME/ncbi-blast-2.2.30+/db”
    
    #this connects to the server
    ftp ftp.ncbi.nlm.nih.gov
    
    #name is anonymous for anonymous log on
    name= anonymous
    
    #i put my email in as a password
    password= rdcooper408@gmail.com

	#This sets which working directory i want to download the database to
	cd blast/db
	
	#this sets the main directory
	bin
	
	#download all of the RNA reference sequences
	update_blastdb.pl refseq_rna

