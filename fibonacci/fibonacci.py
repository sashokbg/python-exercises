def main():
    fibonacci(10)

def fibonacci(element):
    el1 = 1
    el2 = 1
    tmp = 0

    for i in range(10):
        print(el1)
        tmp = el1 + el2
        el1 = el2
        el2 = tmp

if __name__ == '__main__':
    main();
