import sys

if __name__ == '__main__':
    show = list(map(int, sys.argv[1:]))
    with open('bakery.csv') as f:
        sales = f.readlines()
        if len(show) == 2:
            for line in sales[show[0] - 1:show[1]]:
                print(line.strip())
        elif len(show) == 1:
            for line in sales[show[0] - 1:]:
                print(line.strip())
        else:
            for line in sales:
                print(line.strip())
    exit()
