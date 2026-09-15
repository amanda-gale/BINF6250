#!/usr/bin/env python

"""
This script parses data from a specialized ClinVar VCF file. The AF_EXAC key describes the allele frequencies
and the CLNDN key gives the names of the diseases associated with it. The goal is to identify rare variants
and tally the diseases linked to them. A variant is considered rare if its AF_EXAC value is below 0.0001.
For each rare variant, the program extracts its associated diseases from CLNDN, splitting multiple diseases
apart where needed and excluding placeholder values that don't represent real diagnoses. The program reads
the file one line at a time and tallies each disease into a running dictionary, printing the final counts once
the file is done.
"""

from pprint import pprint


def parse_line(this_line: str) -> list:
    """
    Accepts a line from a vcf file as input then evaluates it for relevance and the presence
    of an AF_EXAC ID, then parses and returns a list of diseases associated with the CLNDN info.
    Returns an empty list if no diseases are found.

    :param this_line: The line from the vcf file
    :return: list of CLNDN info or empty list
    """

    print(this_line.strip())
    clndn_list = []   # list to track clndn

    # if line starts with #, skip
    if not this_line.startswith('#'):
        # search for AF_EXAC
        af_start = this_line.find('AF_EXAC=')

        if af_start != -1:    # find function returns -1 if string match not found
            print("AF_EXAC entry found")
            # extract AF_EXAC
            afexac_line = this_line[af_start:]
            af_end = afexac_line.find(';')
            ##print("AF_EXAC string:", afexac_line[0:af_end])
            af_value = float(afexac_line[0:af_end].split('=')[1])
            print("AF_EXAC value:", af_value)

            # check af_exac significance
            if af_value >= 0.0001:
                print("AF value not rare.\n")
                pass
            else:
                print("Rare AF value found!")
                clndn_start = this_line.find("CLNDN=")
                clndn_line = this_line[clndn_start:]
                # extract clndnd string
                clndn_end = clndn_line.find(';')
                ##print("CLNDN string:", clndn_line[0:clndn_end])
                clndn_value = clndn_line[0:clndn_end].split('=')[1]
                # separate elements by pipe into separate list elements
                if '|' in clndn_value:
                    print("Pipe found:", clndn_value)
                clndn_list = clndn_value.split('|')
                # drop list elements that are not_specified or not_provided
                clean_diseases = []
                for disease in clndn_list:
                    if disease != "not_specified" and disease != "not_provided":
                        clean_diseases.append(disease)
                clndn_list = list(set(clean_diseases))   # remove potential duplicates
                print(f"CLNDN list: {clndn_list}")

        # AF_EXAC not present
        else:
            print('Skipping line, not an AF_EXAC entry.\n')

    # line starts with #
    else:
        print("Skipping line, not a legitimate entry.\n")

    return clndn_list


def update_dictionary(clndn_dict: dict, clndn_list: list) -> dict:
    """
    Updates the CLNDN disease counter dictionary with the CLNDN info parsed
    from a given line in the vcf file.

    :param clndn_dict: The CLNDN disease counter dictionary
    :param clndn_list: The list of CLNDN diseases from an AF_EXAC line in the vcf file
    :return: The updated CLNDN disease counter dictionary
    """

    for disease in clndn_list:
        if disease in clndn_dict:   # if disease exists in dictionary
            clndn_dict[disease] += 1   # add to counter
        else:    # if disease does not exist yet
            clndn_dict[disease] = 1    # initialize counter

    return clndn_dict


def read_file(filename: str) -> dict:
    """
    Accept the name of a VCF file as input then passes each line of the file to a parsing function,
    the output of which (unless empty) is sent to a dictionary updating function to keep track of
    disease counts. Returns the final disease count dictionary once every line in the file has been
    evaluated.

    :param filename: the name of a vcf file
    :return: A dictionary tracking all CLNDN disease counts from the entire vcf file
    """
    clndn_dict = {}

    with open(filename, 'r') as f:
        for line in f:
            clndn_list = parse_line(line)   # parse the lines of the file for disease
            if clndn_list:   # if disease list not empty, update dict
                print("Diseases associated with variant. Updating Dictionary.\n")
                update_dictionary(clndn_dict, clndn_list)

    print("Final disease count:")
    return clndn_dict


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))

