#!/usr/bin/env python

import csv
import os
import sys
import argparse

def header_map(header, reqs, show_extra=False):
    """ Return a mapped list of header names to column indices.
        Only found headers will be part of the return map.
    """
    import re
    # Non alphanumeric class with space and some punctuation
    pattern = re.compile('[^a-zA-Z0-9_\ \/#?-]+')
    nml_header = [pattern.sub('', x.lower()).strip() for x in header]
    # Map each required column to an index value in the header
    # Return list
    h = {}
    for col in reqs:
        if type(col) is list:
            for col_name in col:
                if col_name in nml_header:
                    # Map the index to the first column name given regardless of which column name is actually used
                    h[col[0]] = nml_header.index(col_name)
                elif show_extra:
                    print col
        else:
            if col in nml_header:
                h[col] = nml_header.index(col)
            elif show_extra:
                print col
    return h
    
def main():
	parser = argparse.ArgumentParser(description="Extract given fields from csv and output in the same order.")
	parser.add_argument("in_file", type=str, help="file to extract from")
	parser.add_argument("fields", metavar="field", type=str, nargs="+", help="list of fields to extract")
	parser.add_argument("--del", default=",")
	
	args = parser.parse_args()
	
	file = args.in_file
	fields = args.fields
	delimiter = args.del
	
	with open(file, 'rb') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=delimiter)
	    header = csv_reader.next()
	    h = header_map(header, fields)
	    
	    print(",".join(fields))
	    
	    for row in csv_reader:
	        tmp_list = []
	        
	        for f in fields:
	            tmp_list.append( row[h[f]] )
	        
	        print(",".join(tmp_list))
	    
	
	
if __name__ == "__main__":
	main()
    
