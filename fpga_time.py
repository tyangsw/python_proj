#!/usr/bin/env python
import sys
import os
import binascii

binary_file = open(sys.argv[1], 'rb')
binary_file.seek(0, os.SEEK_END)
num_byte = binary_file.tell();
#print("%d bytes" % num_byte)

for offset in range(num_byte):
    print("offset = %d" % offset)
    binary_file.seek(offset)
    eight_bytes = binary_file.read(4)
    if eight_bytes == b"\x01\xA0\x01\x30":
        print("Find it! offset 0x%08X" % offset)
        binary_file.seek(offset+4)
        data = binary_file.read(4)
        hex = binascii.b2a_base64(data)
        print(hex)
        break
    else:
        print("Not found")

binary_file.close()


    
#search for user register 0x3001A001 in fpga binary

#read time timestamp from user register
#decode timestamp
# bit[31:27] 5 bits = 31 days in a month
# bit[26:22] 4 bits = 12 months in a year
# bit[21:16] 6 bits = 0~63 (2000 2063)
# bit[17:12] 6 bits = 24 hours in a day
# bit[11:06] 6 bits = 60 minuts in an hour
# bit[05:00] 6 bits = 60 seconds in a minute


