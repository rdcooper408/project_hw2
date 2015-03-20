#!/usr/bin/python
"""This function takes a BLAST output xml file and parses it"""
__author__ = 'Robert Cooper (rdcooper408@gmail.com)'
__version__ = '0.0.1'


### for this i need to write a script that parses the xml file 
### into a format with all sequences on one line



def rdc_text_parse(parse_file, output_file):

    # this is the basic import and dict setup
    import re
    parse_file_obj = open(parse_file, "r")
    pf = parse_file_obj.readlines()
    contig_ID = None
    out = open(output_file, "w")
    head = 'Contig_ID' + "\t" + 'Hit_num' + "\t" + 'GenID' + "\t" + 'SwissProtID' + "\t" + 'E-value' + "\n"
    out.write(head)
	
    # here i set up the search patterns
    # this works much better re.compile
    # also i needed to add a wildcard for the indents in the beg. of line
    pat1 = re.compile(r"\s*<Iteration_query-def>(\w*\d*)", re.I)
    pat2 = re.compile(r"\s*<Hit_num>(\d*)<", re.I)
    pat3 = re.compile(r"\s*<Hit_id>gi\|(\d*)\|sp\|(\w+\.\w+)\|*", re.I)
    pat4 = re.compile(r"\s*<Hsp_evalue>(.*)</Hsp_evalue>", re.I)
    
    for lines in pf:
        contig_ID_search = pat1.match(str(lines))
        if contig_ID_search:
                contig_ID = contig_ID_search.group(1)
                    
        Hit_num_search = pat2.match(str(lines))
        if Hit_num_search:
            Hit_num = Hit_num_search.group(1)

        ID_search = pat3.match(str(lines))
        if ID_search:
            ID = ID_search.group(1)
            SP = ID_search.group(2)
            all = contig_ID + "\t" + Hit_num + "\t" + ID + "\t" + SP + "\t"
            out.write(all)
        
        ### here i am writing an if statement so that the function only prints 1 E-value
        Eval_search = pat4.match(str(lines))
        if Eval_search:
            Eval = Eval_search.group(1)
            Evalw = Eval + "\n"
            out.write(Evalw)
              
    out.close()
    print "Parsing finished successfully. You rock buddy!"
