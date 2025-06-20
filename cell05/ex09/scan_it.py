import sys

def main():
    if len(sys.argv) < 3:
        print("none")
    else:
        word = sys.argv[1]
        text = sys.argv[2]
        count = text.split().count(word)
        print(count)

if __name__ == "__main__":
    main()