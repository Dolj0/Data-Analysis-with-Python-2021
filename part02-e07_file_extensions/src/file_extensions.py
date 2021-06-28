#!/usr/bin/env python3

import re

def file_extensions(filename):

    initial_list = []
    file_type_list = []
    
    regExpression = r'([^\.]*$)'
    substring_test ='.'
    
    

    with open(filename, 'r') as f:
        return_dict = {}
        no_file_type = []
        for line in f:
            if not '.' in line:
                no_file_type.append(line.split("\n", 1)[0])
            else:
                initial_list.append(line.split("\n", 1)[0])

                extension = re.search(regExpression, line).groups()
                extension_text = extension[0].split("\n", 1)
                file_type_list.append(extension_text[0])

        return_dict = {i : [] for i in file_type_list}

        for j in initial_list:
            for item in file_type_list:
                substring = item
                fullstring = j
                if re.search(substring, fullstring):
                    if fullstring not in return_dict[substring]: 
                        return_dict[substring].append(fullstring)

        return (no_file_type, return_dict)

def main():
    no_file_type, return_dict = file_extensions('src/filenames.txt')
    print(f'{len(no_file_type)} files with no extension')
    for key, value in return_dict.items():
        print(f'{key} {len(value)}')

if __name__ == "__main__":
    main()
