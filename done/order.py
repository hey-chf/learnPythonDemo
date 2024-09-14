# 用你的代码替换 ___
# 冒泡排序
def bubble_sort(lst):
    # 在这里编写你的代码
    # 请使用泡沫排序算法进行排序
    ll = len(lst)
    for i in range(ll, -1, -1):
        for j in range(i-1):
            if lst[j] > lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp
            else:
                continue
    return lst


# 接收输入并转换为列表
data_list = list(map(int, input().split()))

# 调用冒泡排序函数
sorted_list = bubble_sort(data_list)

# 打印排序后的列表
print(sorted_list)

# 示例输入
# 1 15 6 8 2 5 9
# 示例输出
# [1, 2, 5, 6, 8, 9, 15]
