def filereader():
    f = open("demo.txt", 'r')
    for x in f.read().splitlines():
        print(len(x))
def main():
    filereader()


if __name__ == "__main__":
    main()
