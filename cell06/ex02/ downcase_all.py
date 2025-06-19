import sys

def downcase_all(*args):
    if not args:
        print("none")
    else:
        for text in args:
            print(text.lower())

downcase_all(*sys.argv[1:])