def check_prime(n):
    for i in range(2, number):  # 从2开始，到number-1结束
        if (number % i) == 0:  # 判断是否能被i整除
            return False
        return True


number = int(input('输入一个数字：'))
is_prime = check_prime(number)

if is_prime:
    print(f'{number} 是素数')
else:
    print(f'{number} 不是素数')
