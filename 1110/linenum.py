import os

DATA_FILENAME = 'files/word.txt'
if(os.path.exists(DATA_FILENAME)):
    with open(DATA_FILENAME) as f:
        line_num = 1
        for line in f:
            print('{:0>4}:{}'.format(line_num, line.strip()))
            line_num += 1

