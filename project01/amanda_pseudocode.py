from pprint import pprint


# read_file()

    # initialize empty dict
    # open file
    # loop through lines of file
        # call parse_line
        # if list not empty
            # call update_dictionary
    # return dictionary


# parse_line()
    """Takes string and returns a list."""
    # initialize empty list

    ## assuming AS_EXAC present
    # if as_exac:
        # extract AF_EXAC
        # if not significant
           # continue
        # else
            # parse CDN - own function?
            # separate things by pipe into separate list elements
            # drop list elements that are not_specified or not_provided
            # replace initial list with new list (list may be empty)

     ## AF_EXAC not present
    # else:
        # skip line, return None or return empty list

    # return list


# update_dictionary()
    """Takes in dictionary and list and returns a dictionary."""
    # loop over elements in list
        # if key exists in dictionary
            # add one to value
        # else
            # initialize key with value of 1

    # return dictionary

if __name__ == "__main__":
    #pprint(read_file("clinvar_20190923_short.vcf"))