### for this i need to write a script that parses the xml file 
### into a format with all sequences on one line



def rdc_blast_parse(parse_file, output_file):

    # this is the basic import and dict setup
    import re
    parse_file_obj = open(parse_file, "r")
    pf = parse_file_obj.readlines()
    Seq = {}
    Prot = {}
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
            if contig_ID:
                Seq[contig_ID] = Prot #this writes the complete Prot dict before starting new contig
                contig_ID = contig_ID_search.group(1)     
                Seq[contig_ID] = "NA" #this builds the contig ID into Seq dict with placeholder
                Prot = {} #this resets the protein dictionary
            else:
                contig_ID = contig_ID_search.group(1)     
                Seq[contig_ID] = "NA" #this builds the contig ID into Seq dict with placeholder
                Prot = {} #this resets the protein dictionary
        Hit_num_search = pat2.match(str(lines))
        if Hit_num_search:
            Hit_num = Hit_num_search.group(1)
            Prot[Hit_num] = "NA" #this builds the Hit number into protein dict with placeholder

        ID_search = pat3.match(str(lines))
        if ID_search:
            ID = ID_search.group(1)
            SP = ID_search.group(2)
            Prot[Hit_num] = [ID, SP]
            all = contig_ID + "\t" + Hit_num + "\t" + ID + "\t" + SP + "\t"
            out.write(all)
        
        ### here i am writing an if statement so that the function only print 1 E-value
        Eval_search = pat4.match(str(lines))
        if Eval_search:
            if len(Prot[Hit_num]) < 3:
                Eval = Eval_search.group(1)
                Evalw = Eval + "\n"
                Prot[Hit_num].append(Eval)
                out.write(Evalw)
              
    return Seq
    out.close()
    print "Parsing finished successfully. You rock buddy!"