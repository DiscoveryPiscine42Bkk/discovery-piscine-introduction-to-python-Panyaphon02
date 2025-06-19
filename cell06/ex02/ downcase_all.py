import sys

def downcase_all(*args):
    if args:
        for text in args:
            print(text.lower())
    else:
        print("none")

downcase_all(*sys.argv[1:])