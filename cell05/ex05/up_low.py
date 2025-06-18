import sys

input_string = sys.argv[1]

trans_table = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 
                            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
swapped_case = input_string.translate(trans_table)

print(swapped_case)
print(swapped_case)