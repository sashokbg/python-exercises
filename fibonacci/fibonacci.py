import argparse

def main():
    args, number = parseArgs()
    fibonacci(number)

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', help='Calculate the fibonacci sequence to the n-th element', type = int)
    args = parser.parse_args()
    return args, args.number

def fibonacci(element):
    el1 = 1
    el2 = 1
    tmp = 0

    for i in range(element):
        print(el1)
        tmp = el1 + el2
        el1 = el2
        el2 = tmp

if __name__ == '__main__':
    main();
