def print_rangoli(size):
    # 此处编写代码
    wid = size * 4 - 3
    a = ord('a')
    last = ''
    ll = []
    for i in range(2 * size):
        if i < size:
            ss = last + chr(a + size - 1 - i) + last[::-1]
            new_ss = '-'.join(ss)
            pp = new_ss.center(wid, '-')
            print(pp)
            last = last + chr(a + size - 1 - i)
            ll.append(pp)
        else:
            print(ll[2 * size-1-i])


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
