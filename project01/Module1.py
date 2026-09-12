"""
Expectations

You are expected to:
    Copy the template code below into your program
    Download and move the clinvar_20190923_short.vcf to the same folder as your program
    Within the program:
        Write a function called parse_line that:
            Takes a string as an argument
            Extract the AF_EXAC data to determine the rarity of the variant
                If AF_EXAC is not present, skip the line
                If the variant is rare (value for the AF_EXAC key < 0.0001)
                    return a list of associated diseases in CLNDN
                        Do not count the diseases that are:
                            not_specified
                            not_provided
                If the variant is not rare:
                    return an empty list
        Write another function called read_file that:
            Takes a string as an argument representing the file to be opened
            Open the file
            Read the file line by line.
                Note: You are expected to do this one line at a time.
                      The reasoning is that if the file is sufficiently large, you may not have the memory available to hold it.
                      So, do not use readlines()!
            Passes the line to parse_line
            Use a dictionary to count the results given by parse_line to keep a running tally (or count) of the number of times a specific disease is observed
            return that dictionary
        print the results from read_file when it is complete

"""


"""
Project specific information

The given data (clinvar_20190923_short.vcf) is a specialized form of the VCF file. 
As such, there are some additional details to consider when parsing for this assignment. 
You will be expected to consider two (2) special types of keys:

    The AF_EXAC key that describes the allele frequencies from the ExAC database
        ##INFO=<ID=AF_EXAC,Number=1,Type=Float,Description="allele frequencies from ExAC">;
        The data included are floating point numbers
    
    The CLNDN key that gives all the names of diseases the given variant is associated with
        ##INFO=<ID=CLNDN,Number=.,Type=String,Description="ClinVar's preferred disease name for the concept specified by disease identifiers in CLNDISDB">;
        The data are strings. However, if there are multiple diseases associated with a given variant, 
           the diseases are pipe (|) separated (there are 178 instances of this case)

"""

# template code

#!/usr/bin/env python
from pprint import pprint

# Modify this function signature and fill in the details
def parse_line() # if we want it to take a string as an argument, would we do "-> str" ?


    ----------------------

    #All this is brainstorming

    header_lines = sum(1 for line in f if line.startswith("#")) # This line was taken directly from google
    if line.startswith('parameter'): # would this be '#' since header lines start with that?
        continue
    else
        header_lines = in_fh.readline().strip().split('\t') #this was taken from BINF 6200
        info_field = cols[7]  # Column 8 is INFO # This line was taken directly from google

    extract vals from INFO

    # below is found in the header of clinvar
   # AF_EXAC key: ##INFO=<ID=AF_EXAC,Number=1,Type=Float,Description="allele frequencies from ExAC">;
    # CLNDN key: ##INFO=<ID=CLNDN,Number=.,Type=String,Description="ClinVar's preferred disease name for the concept specified by disease identifiers in CLNDISDB">;

    if AF_EXAC is not present, skip
        # would it be better to do if AF_EXAC is present, continue?
    else:
        # note: we can fact-check # of AF_EXAC
        # note 2: CLNDN is what has "not_specified or "not_provided"
        if significance of AF_EXAC < 0.0001
            print list of CLNDN disease names
                specify that some disease names are piped " | "



        else:
            return list()


pass


# Modify this function signature and fill in the details
def read_file()

    ----------------------
    # more brainstorming

    with open('../../clinvar_20190923_short.vcf', 'r') as f:  #taken from BINF6200 lec3
#    for line in f

create dictionary
i+1 # tally for parselines count of each disease mentioned
# so I believe it would be print("f {variable representing disease name} : {tally}) and this would be for each disease

print(f"")readfile results


   ----------------------


    pass


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
