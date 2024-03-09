# 查找句子中的单词结尾出现最多次的元音字母
# 定义函数
def count_common_vowel(string):
    l_list = string.split()
    yuan = 'aeiou'
    yuan_list = {}
    i_max_num = 0
    s_max = ''
    for i in l_list:
        i_lower = i.lower()
        s_last = i_lower[-1]
        if s_last in yuan:
            if s_last in yuan_list:
                yuan_list[s_last] += 1
            else:
                yuan_list[s_last] = 1
    for v in yuan_list:
        if i_max_num < yuan_list[v]:
            s_max = v
            i_max_num = yuan_list[v]
    return s_max


# 调用函数
string = input()
result = count_common_vowel(string)

print(result)
