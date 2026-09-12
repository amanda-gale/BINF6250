from pprint import pprint


def read_file(filename):

    # initialize empty dict
    i = 1
    # open file
    with open(filename, 'r') as f:
        for line in f:
            if i < 50:
                parse_line(line)
                i += 1

    # loop through lines of file
        # call parse_line
        # if list not empty
            # call update_dictionary
    # return dictionary


def parse_line(this_line):
    """Takes string and returns a list."""

    print(this_line.strip())
    # initialize empty list
    clndn_list = []
    # if line starts with INFO, skip
    if not this_line.startswith('#'):
        # search for af_exac
        af_start = this_line.find('AF_EXAC=')
        if af_start != -1:
            print("AF_EXAC entry found")
            # extract AF_EXAC
            this_line = this_line[af_start:]
            af_end = this_line.find(';')
            print("AF_EXAC string:", this_line[0:af_end])
            af_value = float(this_line[0:af_end].split('=')[1])
            print("AF_EXAC value:", af_value)
            # check significance
            if af_value >= 0.0001:
                print("AF value not rare.\n")
                pass
            else:
                print("Rare AF value found!\n")
                # parse CDN - own function?
                # separate things by pipe into separate list elements
                # drop list elements that are not_specified or not_provided
                # replace initial list with new list (list may be empty)
        else:
            print('Skipping line, not an AF_EXEC entry.\n')

        # AF_EXAC not present
    else:
        print("Skipping line, not a legitimate entry.\n")
        # skip line, return None or return empty list

    return clndn_list


# update_dictionary()
    """Takes in dictionary and list and returns a dictionary."""
    # loop over elements in list
        # if key exists in dictionary
            # add one to value
        # else
            # initialize key with value of 1

    # return dictionary

if __name__ == "__main__":
    print(read_file("clinvar_20190923_short.vcf"))
    #pprint(read_file("clinvar_20190923_short.vcf"))

