# 选择排序
def selection_sort(lst):
    # 在这里编写你的代码
    n = len(lst)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i],lst[min_index] = lst[min_index],lst[i]
    return lst

# 接收整数输入并转换为列表
data_list = list(map(int, input().split()))

# 调用 selection_sort() 函数
result = selection_sort(data_list)

# 打印排序后的列表
print(result)

