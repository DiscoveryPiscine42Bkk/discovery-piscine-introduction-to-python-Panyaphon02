import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    input_str = sys.argv[1]
    result = ''.join([c for c in input_str if c == 'z'])

    if result:
        print(result)
    else:
        print("none")

if __name__ == "__main__":
    main()