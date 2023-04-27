def print_num(start, end):
    print(start)
    if start == end:
        return
    return print_num(start + 1, end)


if __name__ == '__main__':
    print_num(1, 10)
