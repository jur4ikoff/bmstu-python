import os
import math

with open('in.txt', 'r') as input_file, open('out.txt', 'w') as output_file:
    min_len = min(map(len, input_file))
    while min_len != float('inf'):
        input_file.seek(0)
        next_min_len = float('inf')
        for line in input_file:
            line_len = len(line)
            if line_len == min_len:
                output_file.write(line)
            elif min_len < line_len < next_min_len:
                next_min_len = line_len
        min_len = next_min_len
