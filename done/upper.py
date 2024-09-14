def is_anagram_present(string1, string2):
    # 检查两个字符串是否包含相同的字符
    def is_anagram(s1, s2):
        # 将字符串转换为字符列表并按字符排序
        return sorted(s1) == sorted(s2)

    # 检查一个字符串是否是另一个字符串的子串
    def is_substring(s1, s2):
        return s1 in s2

    # 首先检查两个字符串是否由相同的字符组成
    if is_anagram(string1, string2):
        # 如果它们本身就是相同的字符组成，则string1是string2的子串
        return True

    # 生成string1的所有可能变位词（通过排列组合）
    permutations = set(permutations := [''.join(p) for p in itertools.permutations(string1)])

    # 检查每个变位词是否是string2的子串
    for permutation in permutations:
        if is_substring(permutation, string2):
            return True

    # 如果没有任何变位词是string2的子串，则返回False
    return False

# 导入需要的库
import itertools

# 示例使用
string1 = "listen"
string2 = "enlists"
print(is_anagram_present(string1, string2))  # 应该输出 True，因为 "listen" 的变位词 "enlist" 是 "enlists" 的子串

string3 = "hello"
string4 = "world"
print(is_anagram_present(string3, string4))  # 应该输出 False，因为 "hello" 的任何变位词都不是 "world" 的子串