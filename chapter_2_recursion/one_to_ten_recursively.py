def print_num(start, end):
    print(start, end=' ')
    if start == end:
        return
    return print_num(start + 1, end)


if __name__ == '__main__':
    print('This program will print all numbers from start to end.')
    try:
        start = int(input('Enter the start number: '))
        end = int(input('Enter the end number: '))
        print_num(start, end)
    except ValueError:
        print('Enter a digits only!')
    except RecursionError:
        print('\nMaximum recursion depth exceeded or start number is '
              'higher than end number.')
