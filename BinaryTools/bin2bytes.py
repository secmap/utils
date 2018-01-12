#!/usr/bin/env python3

import pefile
import sys
import os

def usage():
    print('Usage: bin2bytes.py binary_filename output_filename')


def last_section(section):
    return section.next_section_virtual_address is None

def bin2bytes(sourcefile, targetfile):
    outfile = open(targetfile, 'w')
    pe = pefile.PE(sourcefile)
    
    sections = pe.sections
    for i in range(len(sections)):
        section = sections[i]
        data = section.get_data()
        padding_flag = False
        section_start_addr = pe.OPTIONAL_HEADER.ImageBase + section.VirtualAddress
        cur = section_start_addr
        section_range = range(section_start_addr, section_start_addr + len(data))
        while (last_section(section) and cur in section_range) or (not last_section(section) and cur < section.next_section_virtual_address):
            if (cur + 1) % 16 == 1:
                # Write the address
                outfile.write('{0:08x}'.format(cur))

            outfile.write(' ')    
            if cur in section_range:
                # Inside section
                outfile.write('{0:02x}'.format(data[cur - section_start_addr]))
            else:
                # Inside padding area
                outfile.write('??')

            if (cur + 1) % 16 == 0:
                outfile.write('\n')
            cur += 1
    
    outfile.close()
    

def main():
    if len(sys.argv) != 3:
        usage()
        sys.exit(-1)
    bin2bytes(sys.argv[1], sys.argv[2])
    

if __name__ == '__main__':
    main()
