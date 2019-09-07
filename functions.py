# -*- coding: utf-8 -*-
import re
import sys

def write2file(file2write2, text2write):
    file = open(file2write2, mode='w', encoding='utf-8')
    file.write(str(text2write).encode('utf-8').decode('utf-8'))
    file.close()
    
def append2file(file2write2, text2write):
file = open(file2write2, mode='a', encoding='utf-8')
file.write(str(text2write).encode('utf-8').decode('utf-8'))
file.close()

def striphtmlCRLF(htmltext):
    result = re.sub('<[^<]+?>', '\r\n', htmltext)
    result = re.sub('\s\s', ' ', result)
    # result = re.sub('\r\n+?', '\r\n', result)
    result = re.sub('\s\s', ' ', result)
    # result = result.replace('  ', r' ')
    # result = re.sub('[\r\n\r\n]+', '\r\n', result)
    # for r in (('Ţ', 'Ț'), ('Ş', 'Ș'), ('ţ', 'ț'), ('ş', 'ș'), ('\\t', ''), ('  ', ' '), ('( ', '('), (' )', ')'), (' :', ':'), (' ;', ';'), ('\\u2028', ' '), ('\r\n\r\n', '\r\n')):
        # result = str(result).replace(*r)
        # result = str(result).replace(*r)
        # result = result.strip()
    doublespace = '  '
    for doublespace in result:
        # result = str(result).replace(*r)
        result = str(result).replace(r'  ', r' ')
        result = str(result).replace(' \r\n', '\r\n')
        result = str(result).replace('\r\n ', '\r\n')
    result = re.sub('\s\r\n', '\r\n', result)
    result = re.sub('\r\n\s', '\r\n', result)
        # result = result.strip()
    while result.find(' \r\n') != -1:
        result = result.replace(' \r\n', '\r\n')
    result = result.strip('')
    return result

# sys.stdout.buffer.write(htmltext.encode('utf-8')).file.write
