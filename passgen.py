#!/usr/bin/env python3

import hashlib

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?','@','[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

all_chr = lower_case + upper_case + numbers + symbols

str_len = 3

string = [0 for _ in range(str_len)]

def printfn(string):
    end_str = []
    for element in string:
        end_str.append(all_chr[element])
    return(''.join(end_str))

def gen_words(str_len,hashes,cracked):
    string = [0 for _ in range(str_len)]
    while string != [len(all_chr) for _ in range(str_len)]:
        for index in range(len(string)):
            if string[index] == len(all_chr):
                string[index] = 0
                if (index+1) == str_len:
                    return
                string[(index + 1)] += 1
                # get string of password and check hash against table
        #print(printfn(string))
        cracked = check_hash(printfn(string),hashes,cracked)
        string[0] += 1
    return(cracked)

def check_hash(string, hashes, cracked):
    hash_obj = hashlib.sha256(string.encode('utf-8'))
    hash_str = hash_obj.hexdigest()
    print("Hash of %s is : %s" % (string,hash_str))
    if hash_str in hashes:
        cracked.append([hash_str,string])
    return(cracked)

if __name__ == "__main__":
    hash_file = open('hash.txt','r')
    hashes = []
    for line in hash_file:
        hashes.append(str(line).strip('\n'))
    print(hashes)
    
    cracked = []
    
    cracked = gen_words(5,hashes,cracked)
    
    cracked_file = open('result.txt','w')
    
    print(cracked)
    if cracked != None:
        for item in cracked:
            cracked_file.write('%s\t:\t%s' % (item[0],item[1]))
    else:
        #cracked_file.write('No hashes recovered')
        print("No hashes recovered")