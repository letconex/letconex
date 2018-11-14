import re
import sys

def write2file(file2write2, text2write):
    file = open(file2write2, mode='w', encoding='utf-8')
    file.write(str(text2write).encode('utf-8').decode('utf-8'))
    file.close()
