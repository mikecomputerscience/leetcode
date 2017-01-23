import math
from io import StringIO


# 1. Two Sum
# nums = [2, 7, 11, 15]
# target = 9
# return [0, 1]
# Assume each input have exactly one solution
# But you cannot assume all numbers are unique
def two_sum(nums, target):
    length = len(nums)
    first = 0
    second = 0
    for i in range(length):
        for j in range(i):
            if nums[i] + nums[j] == target:
                first = min(i, j)
                second = max(i, j)
                break
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                first = min(i, j)
                second = max(i, j)
                break
    return [first, second]


# Assume all num are positive and sorted
def two_sum_1(nums, target):
    length = len(nums)
    first = 0
    last = length - 1
    middle = (first + last) // 2
    while True:
        if nums[middle] > target:
            last = middle - 1
            middle = (first + last) // 2
        else:
            break
    new_nums = nums[:last + 1]
    print(new_nums)


# Assume all num are positive and sorted
def two_sum_2(nums, target):
    length = len(nums)
    first = 0
    last = length - 1
    middle = (first + last) // 2
    while True:
        if nums[middle] > target:
            last = middle - 1
            middle = (first + last) // 2
        else:
            break
    new_nums = nums[:last + 1]
    print(new_nums)


def two_sum_hash(nums, target):
    length = len(nums)
    answer = []
    stores = {}
    counts = {}
    for index_1, item in enumerate(nums):
        stores[item] = index_1
    for index_1, item in enumerate(nums):
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    if target % 2 == 0 and target // 2 in stores and counts[target // 2] == 2:
        first = 0
        second = 0
        for index_1, item_1 in enumerate(nums):
            if item_1 == target // 2:
                first = index_1
                break
        for index_2, item_2 in enumerate(nums[first + 1: length]):
            if item_2 == target // 2:
                second = index_2 + first + 1
                break
        return [first, second]
    else:
        for num in nums:
            if target - num in stores and target - num != num:
                answer.append(min(stores[num], stores[target - num]))
                answer.append(max(stores[num], stores[target - num]))
                break
    return answer


# There are duplicates, use list as the value of dictionary
def two_sum_hash_list_as_value(nums, target):
    stores = dict()
    for index, value in enumerate(nums):
        if value in stores:
            stores[value].append(index)
        else:
            stores[value] = [index]
    result = [-2, -1]
    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder in stores:
            store = stores[remainder]
            if remainder == nums[i]:
                if len(store) == 2:
                    result = store
                    break
                else:
                    continue
            result = [i, store[0]]
            break
    return result


print('\n#1. Two Sum:')
# two_sum_nums = [2, 7, 11, 15, 18, 20, 27]
# two_sum_nums = [2, 7, 11]
# two_sum_nums = [3, 2, 4]
two_sum_nums = [0, 4, 3, 0]
# two_sum_target = 9
# two_sum_target = 18
# two_sum_target = 6
# two_sum_target = 0
two_sum_target = 7
# print(two_sum(two_sum_nums, two_sum_target))
# print(two_sum_1(two_sum_nums, two_sum_target))
# print(two_sum_2(two_sum_nums, two_sum_target))
print(two_sum_hash(two_sum_nums, two_sum_target))
print(two_sum_hash_list_as_value(two_sum_nums, two_sum_target))


# 4. Median of Two Sorted Arrays
# Two sorted arrays sorted_one, sorted_two of size m and n
# Find the median of the two sorted arrays together
# Runtime is O(log(m+n))
# [1, 3], [2] => 2.0
# [1, 2], [3, 4] => 2.5
def get_median_of_a_sorted_array(sorted_array):
    length = len(sorted_array)
    if length == 0:
        return None
    middle = (length - 1) / 2
    return (sorted_array[math.floor(middle)] + sorted_array[math.ceil(middle)]) / 2


def get_median_of_two_sorted_arrays(nums1, nums2):
    length1 = len(nums1)
    length2 = len(nums2)
    if length1 == 0 and length2 == 0:
        return None
    median1 = get_median_of_a_sorted_array(nums1)
    median2 = get_median_of_a_sorted_array(nums2)
    if length1 == 0:
        return median2
    if length2 == 0:
        return median1

    # print(median1)
    # print(median2)
    # print('This is', median1 == median2)
    if median1 == median2:
        print('Case 1')
        return median1
    if len(nums1) == 1 and len(nums2) == 1:
        print('Case 2')
        print(nums1)
        print(nums2)
        print(nums1[0])
        print(nums2[0])
        print((nums1[0] + nums2[0]) / 2)
        return (nums1[0] + nums2[0]) / 2
    if len(nums1) == 1:
        print('Case 3')
        print(nums1)
        print(nums2)
        print(get_median_of_a_sorted_array(nums2))
        print(nums1[0])
        print((get_median_of_a_sorted_array(nums2) + nums1[0]) / 2)
        return (get_median_of_a_sorted_array(nums2) + nums1[0]) / 2
    if len(nums2) == 1:
        print('Case 4')
        return (get_median_of_a_sorted_array(nums1) + nums2[0]) / 2
    if median1 > median2:
        print('Case 5')
        nums1 = nums1[:math.ceil(len(nums1) / 2):]
        nums2 = nums2[math.floor(len(nums2) / 2)::]
        print(nums1)
        print(nums2)
        return get_median_of_two_sorted_arrays(nums1, nums2)
    if median1 < median2:
        print('Case 6')
        nums1 = nums1[math.floor(len(nums1) / 2)::]
        nums2 = nums2[:math.ceil(len(nums2) / 2):]
        print(nums1)
        print(nums2)
        return get_median_of_two_sorted_arrays(nums1, nums2)
        # get_median_of_two_sorted_arrays(nums1, nums2)
        # return median1


def get_median_of_two_sorted_arrays_1(nums1, nums2):
    length1 = len(nums1)
    length2 = len(nums2)
    if length1 == 0 and length2 == 0:
        return None
    median1 = get_median_of_a_sorted_array(nums1)
    median2 = get_median_of_a_sorted_array(nums2)
    if length1 == 0:
        return median2
    if length2 == 0:
        return median1

    # print(median1)
    # print(median2)
    # print('This is', median1 == median2)
    if median1 == median2:
        print('Case 1')
        return median1


print('\n#4. Median of Two Sorted Arrays')
test_sorted_a_1 = [1, 3]
test_sorted_a_2 = [2]
test_sorted_b_1 = [1, 2]
test_sorted_b_2 = [3, 4]
test_sorted_c_1 = [1, 5]
test_sorted_c_2 = [2, 6]
# print(get_median_of_two_sorted_arrays(test_sorted_a_1, test_sorted_a_2))
# print(get_median_of_two_sorted_arrays(test_sorted_b_1, test_sorted_b_2))
# print(get_median_of_two_sorted_arrays(test_sorted_c_1, test_sorted_c_2))
print(get_median_of_a_sorted_array([]))
print(get_median_of_a_sorted_array([2]))
print(get_median_of_a_sorted_array([1, 3, 5]))
print(get_median_of_a_sorted_array([3, 4]))
print(2.0 == 2.0)
print('This median problem is not done...')


# 5. Longest Palindromic Substring
def longest_palindrome(s):
    s = '#' + '#'.join(s) + '#'
    rl = [0] * len(s)
    max_right = 0
    pos = 0
    max_len = 0
    max_center = 0
    for i in range(len(s)):
        if i < max_right:
            # rl[i] = min(rl[2 * pos - i], max_right - i)
            rl[i] = min(rl[2 * pos - i], max_right - i + 1)
        else:
            rl[i] = 1
        while i - rl[i] >= 0 and i + rl[i] < len(s) and s[i - rl[i]] == s[i + rl[i]]:
            rl[i] += 1
        if rl[i] + i - 1 > max_right:
            max_right = rl[i] + i - 1
            pos = i
        # max_len = max(max_len, rl[i])
        if rl[i] > max_len:
            max_len = rl[i]
            max_center = pos
    # return max_len - 1
    max_palindromic_length = max_len - 1
    max_palindromic_list = s[max_center - max_palindromic_length: max_center + max_palindromic_length + 1]
    result = StringIO()
    for item in max_palindromic_list:
        if not item == '#':
            result.write(item)
    return result.getvalue()


print('\n#5. Longest Palindromic Substring')
# longest_palindrome_s = 'abcba'
# longest_palindrome_s = 'abcdedcba'
# longest_palindrome_s = 'abcdeedcba'
# longest_palindrome_s = 'ccd'
longest_palindrome_s = 'aada'
print(longest_palindrome(longest_palindrome_s))


# 6. ZigZag Conversion
# Given ("PAYPALISHIRING", 3)
# return "PAHNAPLSIIGYIR"
def convert(s, num_rows):
    length = len(s)
    if length <= num_rows or num_rows == 1:
        return s
    index = 0
    num_cols = math.ceil((4 * length) / (3 * num_rows))
    stores = list()
    for row in range(num_rows):
        stores += [[' '] * num_cols]
    # stores = [([' '] * num_cols) for each_row in range(num_rows)]
    for c in range(num_cols - 1):
        for r in range(num_rows):
            if c % 2 == 0:
                stores[r][c] = s[index]
                index += 1
            else:
                if r % 2 == 1:
                    stores[-r - 1][c] = s[index]
                    index += 1
    left = length - index
    last_col = num_cols - 1
    # while index < length:
    if last_col % 2 == 0:
        for r in range(left):
            stores[r][last_col] = s[index]
            index += 1
    else:
        for r in range(2 * left):
            if r % 2 == 1 and r < num_rows:
                stores[-r - 1][last_col] = s[index]
                index += 1
    print(stores)

    result = StringIO()
    for r in range(num_rows):
        for c in range(num_cols):
            if stores[r][c] != ' ':
                result.write(stores[r][c])
    return result.getvalue()


print('\n#6. ZigZag Conversion:')
# convert_s = 'PAYPALISHIRING'
convert_s = 'ABCD'
convert_num_rows = 3
print(convert(convert_s, convert_num_rows))
print('NOT done. dont know why the error on leetcode')


# 7. Reverse Integer
# 123 --> 321
# -123 --> -321
# 10 --> 1
# 120 --> 21
# 32-bit integer
# returns 0 when the reversed integer overflows
# 1000000003 --> 3000000001 --> 0
# Largest 32-bit integer: 2,147,483,647
# Largest 32-bit integer: 2147483647
def reverse_integer(x):
    if x == 0:
        return 0
    is_positive = False
    if x > 0:
        is_positive = True
    abs_x = abs(x)
    str_x = str(abs_x)
    length = len(str_x)
    result = StringIO()
    for index in range(length):
        result.write(str_x[-index - 1])
    ans = result.getvalue()
    if is_positive:
        return int(ans)
    else:
        return int('-' + ans)


def reverse_integer_1(x):
    if x == 0:
        return 0
    is_positive = False
    if x > 0:
        is_positive = True
    abs_x = abs(x)
    str_x = str(abs_x)
    length = len(str_x)
    stores = list()
    for index in range(length):
        stores.append(str_x[-index - 1])
    ans = ''
    for char in stores:
        ans += char
    if is_positive:
        return int(ans)
    else:
        return int('-' + ans)


def reverse_integer_2(x):
    if x == 0:
        return 0
    is_positive = False
    if x > 0:
        is_positive = True
    abs_x = abs(x)
    while abs_x % 10 == 0:
        abs_x /= 10
    abs_x = int(abs_x)
    str_x = str(abs_x)
    length = len(str_x)
    stores = list()
    for index in range(length):
        stores.append(str_x[-index - 1])
    ans = ''
    for char in stores:
        ans += char
    if int(ans) > 2147483647:
        return 0
    if is_positive:
        return int(ans)
    else:
        return int('-' + ans)


print('\n#7. Reverse Integer:')
reverse_integer_x = 123
print(reverse_integer(reverse_integer_x))
print(reverse_integer_1(reverse_integer_x))
print(reverse_integer_2(reverse_integer_x))


# 8. String to Integer (atoi)
def my_atoi(string):
    if not string:
        return 0
    string = string.strip()
    length = len(string)
    if length == 0:
        return 0
    start = 0
    sign = 1
    result = 0
    if string[start] == '-':
        sign = -1
        start += 1
    elif string[start] == '+':
        start += 1
    for i in range(start, length):
        if string[i] < '0' or string[i] > '9':
            break
        result = (result * 10) + int(string[i])
    result *= sign
    int_max = pow(2, 31) - 1
    int_min = -int_max - 1
    if sign == 1 and result > int_max:
        return int_max
    if sign == -1 and result < int_min:
        return int_min
    return result


def my_atoi_nine_chapter(string):
    string = string.strip()
    if string == "":
        return 0
    i = 0
    sign = 1
    result = 0
    length = len(string)
    max_int = (1 << 31) - 1
    if string[i] == '+':
        i += 1
    elif string[i] == '-':
        i += 1
        sign = -1

    for i in range(i, length):
        if string[i] < '0' or string[i] > '9':
            break
        result = result * 10 + int(string[i])
    result *= sign
    if result >= max_int:
        return max_int
    if result < max_int * -1:
        return max_int * - 1 - 1
    return result


# my_atoi_str = ' - 3 924x8fc '
# my_atoi_str = ' + 374'
# my_atoi_str = '+'
# my_atoi_str = '-'
# my_atoi_str = '+-2'
# my_atoi_str = '  -0012a42'
my_atoi_str = '-2147483649'
print('\n#8. String to Integer (atoi):')
print(my_atoi(my_atoi_str))
print(my_atoi_nine_chapter(my_atoi_str))


# 9. Palindrome Number
# No extra space
# Cannot convert it to a string
# Palindromic numbers are 0, 1-9, 11, 22-99, 101, 111, 121...
def is_palindrome(x):
    if x < 0:
        return False
    if x < 10:
        return True
    for index in range(len(str(x)) // 2):
        if ((x // (pow(10, index))) % 10) != ((x // (pow(10, len(str(x)) - index - 1))) % 10):
            return False
    return True


print('\n#9. Palindrome Number:')
test_is_palindrome_x = 646
print(is_palindrome(test_is_palindrome_x))

# 10. Regular Expression Matching
"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
The function prototype should be:
def isMatch(self, s, p):
Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""


def is_match(s, p):
    return s + p + ' Not Done'


is_match_s = 'aa'
is_match_p = 'a'
print('\n#10. Regular Expression Matching:')
print(is_match(is_match_s, is_match_p))


# 12. Integer to Roman
# range from 1 to 3999
def int_to_roman(num):
    store = []
    count = 0
    while num:
        remainder = num % 10
        store.append(int_to_roman_single_character(count, remainder))
        num //= 10
        count += 1
    result = ''
    for i in range(len(store) - 1, -1, -1):
        result += store[i]
    return result


def int_to_roman_single_character(bit, num):
    # bit can be 0, 1, 2
    # num can be 0, 1, 2, ..., 9
    if bit == 3:
        return 'M' * num
    romans_dict = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    romans = [''] * 10
    romans[1] = romans_dict[pow(10, bit)]
    for i in range(2, 4):
        romans[i] = romans[i - 1] + romans[1]
    romans[4] = romans_dict[pow(10, bit)] + romans_dict[pow(10, bit) * 5]
    romans[5] = romans_dict[pow(10, bit) * 5]
    for j in range(6, 9):
        romans[j] = romans[j - 1] + romans[1]
    romans[9] = romans_dict[pow(10, bit)] + romans_dict[pow(10, bit) * 10]
    return romans[num]


int_to_roman_num = 374
# int_to_roman_num = 111
# int_to_roman_num = 3999
print('\n#12. Integer to Roman:')
print(int_to_roman(int_to_roman_num))


# 13. Roman to Integer
# 1 to 3999
def roman_to_integer(s):
    s = s.upper()
    length = len(s)
    letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    romans = dict(zip(letters, values))
    if length == 1:
        return romans[s[0]]
    result = 0
    index = 0
    while index in range(length - 1):
        if romans[s[index]] < romans[s[index + 1]]:
            result += (romans[s[index + 1]] - romans[s[index]])
            index += 2
        else:
            result += romans[s[index]]
            index += 1
        if index == length - 1:
            return result + romans[s[-1]]
        if index == length + 1:
            return result
    return result


print('\n#13. Roman to Integer:')
test_roman_to_integer = 'CCCLXXIV'
print(roman_to_integer(test_roman_to_integer))


# 14. Longest Common Prefix
# Find the longest common prefix string amongst an array of strings
def longest_common_prefix(strs):
    length = len(strs)
    if length == 0:
        return ''
    if length == 1:
        return strs[0]
    min_length = len(strs[0])
    for i in range(1, length):
        if len(strs[i]) < min_length:
            min_length = len(strs[i])
    result = StringIO()
    for j in range(min_length):
        letter = strs[0][j]
        if letter_match(strs, j):
            result.write(letter)
        else:
            break
    return result.getvalue()


def letter_match(strs, i):
    length = len(strs)
    letter = strs[0][i]
    for k in range(1, length):
        if strs[k][i] != letter:
            return False
    return True


def longest_common_prefix_second(strs):
    length = len(strs)
    if length == 0:
        return ''
    if length == 1:
        return strs[0]
    min_length = len(strs[0])
    for i in range(1, length):
        if len(strs[i]) < min_length:
            min_length = len(strs[i])
    result = ''
    for j in range(min_length):
        letter = strs[0][j]
        if letter_match(strs, j):
            result += letter
        else:
            break
    return result


print('\n#14. Longest Common Prefix:')
longest_common_prefix_strs = ['ab', 'aba', 'abc', 'abd', 'abcd']
# longest_common_prefix_strs = ['a', 'a', 'b']
# longest_common_prefix_strs = ['a', 'b']
# longest_common_prefix_strs = ['aca', 'cba']
print(longest_common_prefix(longest_common_prefix_strs))
print(longest_common_prefix_second(longest_common_prefix_strs))


# 20. Valid Parentheses
# () --> True
# ()[]{} --> True
# (] --> False
# ([)] --> False
def is_valid_parentheses(s):
    left = ['(', '[', '{']
    right = [')', ']', '}']
    if s[0] in right:
        return False
    length = len(s)
    if length % 2 == 1:
        return False
    stores = list()
    for i in range(length):
        if s[i] in left:
            stores.append(s[i])
        else:
            if not if_match(stores[-1], s[i]):
                return False
            del stores[-1]
    if len(stores) == 0:
        return True
    else:
        return False


def if_match(left, right):
    if left in ['(', ')'] and right in ['(', ')'] and left != right:
        return True
    elif left in ['[', ']'] and right in ['[', ']'] and left != right:
        return True
    elif left in ['{', '}'] and right in ['{', '}'] and left != right:
        return True
    else:
        return False


print('\n#20. Valid Parentheses:')
is_valid_parentheses_s = '{[()]}'
print(is_valid_parentheses(is_valid_parentheses_s))


# 26. Remove Duplicate from Sorted Array
# Remove in place, no extra space.
# [1, 1, 2] --> [1, 2] --> return length 2
def remove_duplicates(nums):
    length = len(nums)
    if length <= 1:
        return length
    index = length - 1
    memo = nums[index]
    while index > 0:
        if nums[index - 1] == memo:
            nums.pop(index - 1)
        else:
            memo = nums[index - 1]
        index -= 1
    return len(nums)


print('\n#26. Remove Duplicate from Sorted Array:')
test_remove_duplicates_nums = [1, 1, 2]
print(remove_duplicates(test_remove_duplicates_nums))


# 27. Remove Element
# Given an array and a value, remove all instances of that value in place and return the new length.
# No extra space is allowed. Order can be changed, return length only.
# [3, 2, 2, 3], 3 ==> 2
def remove_element(nums, val):
    index = len(nums) - 1
    while index >= 0:
        if nums[index] == val:
            nums.pop(index)
        index -= 1
    return len(nums)


def remove_element_better(nums, val):
    length = len(nums)
    count = 0
    low = 0
    high = length - 1
    while low <= high:
        if nums[low] == val and nums[high] != val:
            temp = nums[high]
            nums[high] = nums[low]
            nums[low] = temp
            low += 1
            high -= 1
            count += 1
        elif nums[low] != val:
            low += 1
        elif nums[high] == val:
            high -= 1
            count += 1
    for i in range(count):
        nums.pop()
    print(nums)
    return length - count


def remove_element_best(nums, val):
    length = len(nums)
    index = 0
    for i in range(length):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    for j in range(length - index):
        nums.pop()
    print(nums)
    return index


print('\n#27. Remove Element:')
remove_element_nums = [3, 2, 2, 3, 4, 3]
remove_element_better_nums = [3, 2, 2, 3, 4, 3]
remove_element_best_nums = [3, 2, 2, 3, 4, 3]
test_remove_element_val = 3
print(remove_element(remove_element_nums, test_remove_element_val))
print(remove_element_better(remove_element_better_nums, test_remove_element_val))
print(remove_element_best(remove_element_best_nums, test_remove_element_val))


# 28. Implement strStr()
# '', '' --> 0
# 'a', '' --> 0
def str_str(haystack, needle):
    hay_len = len(haystack)
    needle_len = len(needle)
    if needle_len > hay_len:
        return -1
    if needle_len == 0:
        return 0
    for i in range(hay_len - needle_len + 1):
        for j in range(needle_len):
            if needle[j] != haystack[i + j]:
                break
            if j == needle_len - 1:
                return i
    return -1


str_str_haystack = 'cabac'
str_str_needle = 'aba'
print('\n#28.Implement strStr():')
print(str_str(str_str_haystack, str_str_needle))


# 31. Next Permutation
# 1, 2, 3 --> 1, 3, 2
# 3, 2, 1 --> 1, 2, 3
# 1, 1, 5 --> 1, 5, 1
# Do not return anything, modify nums in-place instead.
# No extra space
def next_permutation(nums):
    print(nums)
    length = len(nums)
    if length <= 1:
        pass
    else:  # len >= 2
        first_decrease_index = -1
        for i in range(-2, -length - 1, -1):
            if nums[i] < nums[i + 1]:
                first_decrease_index = i
                break
        if first_decrease_index == -1:
            swap_list(nums, 0, length - 1)
            print(nums)
        else:
            for j in range(-1, first_decrease_index, -1):
                if nums[j] > nums[first_decrease_index]:
                    temp = nums[j]
                    nums[j] = nums[first_decrease_index]
                    nums[first_decrease_index] = temp
                    break
            low = first_decrease_index + 1
            high = -1
            swap_list(nums, low, high)
            print(nums)


def swap_list(nums, low, high):
    while low < high:
        temp = nums[low]
        nums[low] = nums[high]
        nums[high] = temp
        low += 1
        high -= 1


# next_permutation_nums = [1, 1, 2, 5]
next_permutation_nums = [1, 6, 8, 7, 7, 4, 3, 2]
# next_permutation_nums = [5, 4, 3, 2, 1]
print('\n#31. Next Permutation:')
next_permutation(next_permutation_nums)


# 36. Valid Sudoku
# Empty cells are filled with a '.'
# Only the filled cells need to be validated
def is_distinct_1d(array):
    stores = [0] * 10
    for item in array:
        if '0' <= item <= '9':
            stores[int(item)] += 1
    if max(stores) > 1:
        return False
    else:
        return True


def is_distinct_2d(array):
    stores = [0] * 10
    for row in range(len(array)):
        for column in range(len(array[row])):
            if '0' <= array[row][column] <= '9':
                stores[int(array[row][column])] += 1
    if max(stores) > 1:
        return False
    else:
        return True


def is_valid_sudoku(board):
    flag_row = False
    flag_column = False
    flag_2d = False
    for r in range(0, 9):
        if not is_distinct_1d(board[r]):
            return False
        if r == 8:
            flag_row = True
    for c in range(0, 9):
        if not is_distinct_1d([item[c] for item in board]):
            return False
        if c == 8:
            flag_column = True
    for row in [0, 3, 6]:
        for column in [0, 3, 6]:
            if not is_distinct_2d([item[column:column + 3] for item in board[row:row + 3]]):
                return False
            if row == 6 and column == 6:
                flag_2d = True
    if flag_row and flag_column and flag_2d:
        return True


print('\n#36. Valid Sudoku:')
test_is_valid_sudoku_board = [
    [5, 3, '.', '.', 7, '.', '.', '.', '.'],
    [6, '.', '.', 1, 9, 5, '.', '.', '.'],
    ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
    [8, '.', '.', '.', 6, '.', '.', '.', 3],
    [4, '.', '.', 8, '.', 3, '.', '.', 1],
    [7, '.', '.', '.', 2, '.', '.', '.', 6],
    ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
    ['.', '.', '.', 4, 1, 9, '.', '.', 5],
    ['.', '.', '.', '.', 8, '.', '.', 7, 9]
]
test_is_valid_sudoku_board_1 = [
    "..4...63.",
    ".........",
    "5......9.",
    "...56....",
    "4.3.....1",
    "...7.....",
    "...5.....",
    ".........",
    "........."
]
test_is_valid_sudoku_board_2 = [
    ['.', '.', '4', '.', '.', '.', '6', '3', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['5', '.', '.', '.', '.', '.', '.', '9', '.'],
    ['.', '.', '.', '5', '6', '.', '.', '.', '.'],
    ['4', '.', '3', '.', '.', '.', '.', '.', '1'],
    ['.', '.', '.', '7', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '5', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']
]

# print(is_valid_sudoku(test_is_valid_sudoku_board))
# print(is_valid_sudoku(test_is_valid_sudoku_board_1))
print(is_valid_sudoku(test_is_valid_sudoku_board_2))


# 38. Count and Say
# 1, 11, 21, 1211, 111221, ...
# Given an integer n, generate the nth sequence as a string
# 1 --> '1'
# 2 --> '11'
# 3 --> '21'
# 4 --> '1211'
def count_and_say(n):
    if n == 1:
        return '1'
    stores = ['0'] * (n + 1)
    stores[1] = '1'
    for i in range(2, n + 1):
        memo = list(stores[i - 1])
        length = len(memo)
        count = 0
        value = memo[0]
        pairs = list()
        for j in range(length):
            count += 1
            if memo[j] != value:
                value = memo[j]
            if j == length - 1:
                pairs.append(str(count) + value)
            elif memo[j + 1] != value:
                pairs.append(str(count) + value)
                count = 0
        stores[i] = ''.join(pairs)
    return stores[-1]


print('\n#38. Count and Say:')
count_and_say_n = 10
print(count_and_say(count_and_say_n))


# 42. Trapping Rain Water
def trap_rain_water(height):
    # Time O(n), Space O(n)
    if not height:
        return 0
    length = len(height)
    result = 0
    if length <= 2:
        return 0
    # length >= 3
    left = [0] * length
    right = [0] * length
    max_left = height[0]
    max_right = height[-1]
    for i in range(1, length):
        if height[i - 1] > max_left:
            max_left = height[i - 1]
        left[i] = max_left
    for j in range(-2, -length - 1, -1):
        if height[j + 1] > max_right:
            max_right = height[j + 1]
        right[j] = max_right
    for k in range(length):
        result += max((min(left[k], right[k]) - height[k]), 0)
    return result


def trap_rain_water_constant_space(height):
    # Time O(n), Space O(1)
    # This one is a little better
    if not height:
        return 0
    length = len(height)
    result = 0
    if length <= 2:
        return 0
    # length >= 3
    max_height = height[0]
    max_index = 0
    for i in range(length):
        if height[i] > max_height:
            max_height = height[i]
            max_index = i
    max_left = height[0]
    max_right = height[-1]
    for j in range(1, max_index):
        if height[j - 1] > max_left:
            max_left = height[j - 1]
        result += max((max_left - height[j]), 0)
    for k in range(length - 2, max_index, -1):
        if height[k + 1] > max_right:
            max_right = height[k + 1]
        result += max((max_right - height[k]), 0)
    return result


def trap_rain_water_two_pointers(height):
    # Time O(n), Space O(1), two pointers
    if not height:
        return 0
    length = len(height)
    if length <= 2:
        return 0
    result = 0
    low = 0
    high = length - 1
    left_max = height[low]
    right_max = height[high]
    while low <= high:
        if left_max < right_max:
            if height[low] >= left_max:
                left_max = height[low]
            else:
                result += left_max - height[low]
            low += 1
        else:
            if height[high] >= right_max:
                right_max = height[high]
            else:
                result += right_max - height[high]
            high -= 1
    return result


trap_rain_water_height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print('\n#42. Trapping Rain Water:')
print(trap_rain_water(trap_rain_water_height))
print(trap_rain_water_constant_space(trap_rain_water_height))
print(trap_rain_water_two_pointers(trap_rain_water_height))


# 48. Rotate Image
# Given an n x n 2D matrix
# Rotate by 90 degrees clockwise
# Do this in-place, return void
def rotate_image(matrix):
    print(matrix)
    length = len(matrix)
    if length <= 1:
        pass
    else:  # length >= 2
        for row in range(length - 1):
            for col in range(row + 1, length):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        for row_1 in range(length):
            low = 0
            high = length - 1
            while low < high:
                temp_1 = matrix[row_1][low]
                matrix[row_1][low] = matrix[row_1][high]
                matrix[row_1][high] = temp_1
                low += 1
                high -= 1
    print(matrix)


# rotate_image_matrix = [
#     [1, 2],
#     [3, 4]
# ]
# rotate_image_matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
rotate_image_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print('\n#48. Rotate Image:')
rotate_image(rotate_image_matrix)


# 49. Group Anagrams
# given: ["eat", "tea", "tan", "ate", "nat", "bat"]
# All inputs will be in lower-case
# return:
# [
#   ["ate", "eat","tea"],
#   ["nat", "tan"],
#   ["bat"]
# ]
# Time Limit Exceeded, not happy
def group_anagrams_result_sorted(strs):
    if strs is None:
        return [[]]
    length = len(strs)
    if length == 0:
        return [[]]
    if length == 1:
        return [[strs[0]]]
    copy = list()
    for word in strs:
        copy.append(word)
    for i in range(length):
        temp = ''.join(sorted(copy[i]))
        copy[i] = temp
    counts = [0] * length
    for j in range(length):
        if counts[j] != 0:
            continue
        target = copy[j]
        for k in range(j + 1, length):
            if counts[k] != 0:
                continue
            if copy[k] == target:
                counts[k] = j + 1
        counts[j] = j + 1
    indexes = dict()
    for index, item in enumerate(counts):
        if item in indexes:
            indexes[item].append(index)
        else:
            indexes[item] = [index]
    lengths = dict()
    for key, value in indexes.items():
        lengths[key] = len(value)
    length_indexes = dict()
    for key, value in lengths.items():
        if value in length_indexes:
            length_indexes[value].append(key)
        else:
            length_indexes[value] = [key]
    result = list()
    the_length = len(length_indexes)
    for l in range(the_length):
        max_index = max(length_indexes)
        max_item = length_indexes[max_index]
        for each_item in max_item:
            temp = [strs[m] for m in indexes[each_item]]
            result.append(temp)
        del length_indexes[max_index]
    return result


# Time Limit Exceeded, not happy
def group_anagrams_result_not_sorted(strs):
    if strs is None:
        return [[]]
    length = len(strs)
    if length == 0:
        return [[]]
    if length == 1:
        return [[strs[0]]]
    copy = list()
    for word in strs:
        copy.append(word)
    for i in range(length):
        temp = ''.join(sorted(copy[i]))
        copy[i] = temp
    counts = [0] * length
    for j in range(length):
        if counts[j] != 0:
            continue
        target = copy[j]
        for k in range(j + 1, length):
            if counts[k] != 0:
                continue
            if copy[k] == target:
                counts[k] = j + 1
        counts[j] = j + 1
    indexes = dict()
    for index, item in enumerate(counts):
        if item in indexes:
            indexes[item].append(index)
        else:
            indexes[item] = [index]
    result = list()
    for key, value in indexes.items():
        result.append([strs[l] for l in value])
    return result


# https://www.youtube.com/watch?v=DhiT3hDt3ZA
# I think the one is not correct
# This one is answer to the following problem:
# https://www.lintcode.com/en/problem/anagrams/
def group_anagrams_jikai_tang(strs):
    dic = {}
    res = []
    for word in strs:
        ordered_str = str(sorted(word))
        print(ordered_str)
        if ordered_str in dic:
            dic[ordered_str].append(word)
        else:
            dic[ordered_str] = [word]
    for key in dic:
        if len(dic[key]) >= 2:
            res += dic[key]
    return res


# http://www.cnblogs.com/zuoyuan/p/3769993.html
# Finally accepted. but only 42%, not good enough, will do it later
def group_anagrams_zuoyuan(strs):
    if strs is None:
        return [[]]
    length = len(strs)
    if length == 0:
        return [[]]
    if length == 1:
        return [[strs[0]]]
    dic = {}
    res = []
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in dic:
            dic[sorted_word].append(word)
        else:
            dic[sorted_word] = [word]
    for key, value in dic.items():
        res.append(value)
    return res


group_anagrams_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# group_anagrams_strs = ["", "b", 'c', 'ab', 'ba', 'ab']
print('\n49. Group Anagrams:')
print(group_anagrams_result_sorted(group_anagrams_strs))
print(group_anagrams_result_not_sorted(group_anagrams_strs))
# print(group_anagrams_jikai_tang(group_anagrams_strs))
print(group_anagrams_zuoyuan(group_anagrams_strs))
print('NOT DONE')


# 53. Maximum Subarray
# Find the contiguous subarray within an array(len >= 1) which has the largest sum.
# Array = [−2,1,−3,4,−1,2,1,−5,4]
# Return [4,−1,2,1] (sum = 6)
# Input: [-1]; return -1
# If you get a O(n) solution, try divide and conquer
def max_subarray(nums):
    length = len(nums)
    if length == 0:
        return 0
    if length == 1:
        return nums[0]
    if length == 2:
        return max(nums[0], nums[1], nums[0] + nums[1])
    middle = length // 2
    result_contain_middle = nums[middle]
    left_max = nums[middle - 1]
    left_sum = 0
    for left in range(middle - 1, -1, -1):
        left_sum += nums[left]
        if left_sum > left_max:
            left_max = left_sum
    result_contain_middle += max(left_max, 0)
    right_max = nums[middle + 1]
    right_sum = 0
    for right in range(middle + 1, length, 1):
        right_sum += nums[right]
        if right_sum > right_max:
            right_max = right_sum
    result_contain_middle += max(right_max, 0)

    return max(result_contain_middle, max_subarray(nums[:middle:]), max_subarray(nums[middle + 1::]))


print('\n#53. Maximum Subarray:')
test_max_subarray = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# test_max_subarray = [-1, -2, -1, 2, 3]
# test_max_subarray = [-2, -1]
# test_max_subarray = [-2]
print(max_subarray(test_max_subarray))


# 58. Length of Last Word
# A string consists of upper/lower-case alphabets and space
# Return the length of last word
# Return 0 if the last word does not exist
# s = 'Hello World'
# return 5
def length_of_last_word(s):
    words = s.split()
    if len(words) == 0:
        return 0
    return len(words[-1])


print('\n#58. Length of Last Word:')
length_of_last_word_s = '  hello d'
print(length_of_last_word(length_of_last_word_s))


# 60. Permutation Sequence
# n = 3
# k result
# 1 "123"
# 2 "132"
# 3 "213"
# 4 "231"
# 5 '312'
# 6 '321'
# 1 <= n <= 9
def get_permutation(n, k):
    result = ''
    # total = get_factorial(n)
    each = get_factorial(n - 1)
    result += str(((k - 1) // each) + 1)
    print('not done')
    return result


def get_factorial(n):
    result = 1
    if n == 0:
        return result
    stores = []
    for i in range(n + 1):
        stores.append(1)
    for j in range(1, n + 1):
        stores[j] = j * stores[j - 1]
    return stores[n]


get_permutation_n = 4
get_permutation_k = 2
print('\n#60. Permutation Sequence:')
print(get_permutation(get_permutation_n, get_permutation_k))


# print(get_permutation(get_permutation_n, 3))
# print(get_permutation(get_permutation_n, 7))
# print(get_permutation(get_permutation_n, 18))
# print(get_permutation(get_permutation_n, 19))
# print(get_permutation(get_permutation_n, 30))
# print(get_permutation(get_permutation_n, 36))


# 62. Unique Paths
# A robot is at top-left corner of a m X n grid(m is row, n is column).
# Move only down or right, return unique paths to bottom-right.
# 1 <= m, n <= 100
def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1
    if m == 2 and n == 2:
        return 2

    smaller = min(m, n)
    larger = max(m, n)
    m = smaller
    n = larger
    print(m)
    print(n)

    stores = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for index in range(1, n + 1):
        stores[1][index] = 1
    for index in range(1, m + 1):
        stores[index][1] = 1

    for outer in range(2, m + 1):
        for index in range(outer, n + 1):
            stores[outer][index] += stores[outer][index - 1] + stores[outer - 1][index]
        for index in range(outer, m + 1):
            stores[index][outer] = stores[outer][index]

    print(stores)
    return stores[-1][-1]


print('\n#62. Unique Paths:')
test_unique_paths_m = 3
test_unique_paths_n = 7
print(unique_paths(test_unique_paths_m, test_unique_paths_n))


# 64. Minimum Path Sum
# A mXn grid filled with non-negative numbers, from top left to bottom right
# Return the min of the num sum on the path
# Can only move either down or right.
def minimum_path_sum(grid):
    grid += [0]
    print(grid)
    return grid[-1]


print('\n#64. Minimum Path Sum:')
test_minimum_path_sum = [[1, 2, 3, 4], [0, 1, 2, 2], [3, 1, 0, 3]]
print(minimum_path_sum(test_minimum_path_sum))


# 66. Plus One
# Non-negative number
# Most significant digit is the head of the list
# return the new list
def plus_one(digits):
    length = len(digits)
    if is_all_nine(digits):
        new_list = [0] * (length + 1)
        new_list[0] = 1
        return new_list
    else:  # length is the same
        for i in range(length - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        return digits


def is_all_nine(nums):
    for i in range(len(nums)):
        if nums[i] != 9:
            return False
    return True


plus_one_digits = [9, 9, 9]
print('\n#66. Plus One:')
print(plus_one(plus_one_digits))


# 67. Add Binary
def add_binary(a, b):
    a = int(a, 2)
    b = int(b, 2)
    result = a + b
    result = bin(result)
    result = result[2:len(result)]
    return result


add_binary_a = '11'
add_binary_b = '1'
print('\n#67. Add Binary:')
print(add_binary(add_binary_a, add_binary_b))


# 70. Climbing Stair
# There are n steps to reach the top.
# Each time climb 1 or 2 steps, how many distinct ways?
# 0 => 1
# 1 => 1
# 2 => 2
# 3 => 3
# 4 => 5
# Fibonacci series
def get_ways_to_climb_stair(step):
    ways = [0] * (step + 1)
    if step <= 1:
        return 1
    ways[0] = 1
    ways[1] = 1
    for index in range(2, len(ways)):
        ways[index] = ways[index - 1] + ways[index - 2]
    return ways[-1]


print('\n#70. Climbing Stairs')
test_climb_stair = 10
print(get_ways_to_climb_stair(test_climb_stair))


# 73. Set Matrix Zeroes
# m X n matrix, if element = 0, set entire row and column = 0
# Do it in place, return void
def set_zeroes(matrix):
    print(matrix)
    row_len = len(matrix)
    if row_len == 0:
        pass
    else:
        col_len = len(matrix[0])
        if col_len == 0:
            pass
        else:
            first_row_contains_zero = False
            first_col_contains_zero = False
            for i in range(col_len):
                if matrix[0][i] == 0:
                    first_row_contains_zero = True
                    break
            for j in range(row_len):
                if matrix[j][0] == 0:
                    first_col_contains_zero = True
                    break
            for row in range(1, row_len):
                for k in range(1, col_len):
                    if matrix[row][k] == 0:
                        matrix[row][0] = 0
            for col in range(1, col_len):
                for l in range(1, row_len):
                    if matrix[l][col] == 0:
                        matrix[0][col] = 0
            for m in range(1, col_len):
                if matrix[0][m] == 0:
                    set_zeroes_for_col(matrix, m)
            for n in range(1, row_len):
                if matrix[n][0] == 0:
                    set_zeroes_for_row(matrix, n)
            if first_row_contains_zero:
                set_zeroes_for_row(matrix, 0)
            if first_col_contains_zero:
                set_zeroes_for_col(matrix, 0)
    print(matrix)


def set_zeroes_for_row(matrix, row):
    length = len(matrix[row])
    for i in range(length):
        matrix[row][i] = 0


def set_zeroes_for_col(matrix, col):
    length = len(matrix)
    for i in range(length):
        matrix[i][col] = 0


set_zeroes_matrix = [
    [1, 2, 1, 4, 2],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 1, 2]
]
print('\n#73. Set Matrix Zeroes')
set_zeroes(set_zeroes_matrix)


# 88. Merge Sorted Array
# Two sorted integer arrays nums1 and nums2
# The first list should have enough space for merging two lists
# Merge nums2 into nums1 as one sorted array
# m = len(nums1)
# n = len(nums2)
# return void, modify nums1 in-place
def merge(nums1, m, nums2, n):
    if m == 0:
        nums1 = nums2
        print(nums1)
        return
    if n == 0:
        print(nums1)
        return
    for i in range(n):
        insert_index = get_insert_index(nums1, nums2[i])
        nums1.append(0)
        m += 1
        for j in range(m - 1, insert_index, -1):
            nums1[j] = nums1[j - 1]
        nums1[insert_index] = nums2[i]

    print(nums1)
    return


def get_insert_index(nums, value):
    length = len(nums)
    if value < nums[0]:
        return 0
    if value > nums[-1]:
        return length

    first = 0
    last = length - 1
    middle = (first + last) // 2
    ans = 0
    while ans in range(0, length + 1):
        if nums[middle] == value:
            ans = middle + 1
            for index in range(middle + 1, last + 1):
                if nums[index] > value:
                    return ans
                ans += 1
            return ans
        elif nums[middle] < value:
            if nums[middle + 1] > value:
                ans = middle + 1
                return ans
            first = middle + 1
            middle = (first + last) // 2
        else:
            if nums[middle - 1] < value:
                ans = middle
                return ans
            last = middle - 1
            middle = (first + last) // 2


def merge1(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]


print('\n#88. Merge Sorted Array:')
# mer_nums1 = [0, 1, 2, 3, 4, 5, 6]
# merge_nums1 = [1, 2, 3, 5, 7, 8]
merge_nums1 = [1, 2, 3, 0]
# mer_nums2 = [0, 1, 2, 3, 4, 5]
# merge_nums2 = [2, 3, 4, 6, 9]
merge_nums2 = [1]
# mer_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
merge_nums = [1, 1, 1, 3, 3, 4, 5, 5]
merge_m = 3
merge_n = 1
merge1(merge_nums1, merge_m, merge_nums2, merge_n)
# print(get_insert_index(merge_nums, 6))


# 92. Reverse Linked List II
print('\n#92. Reverse Linked List II:')
print('See Leetcode')


# 95. Unique Binary Search Trees II
# Integer n >= 1, generate all structurally unique BSTs that store values 1, 2, ..., n
# n = 3, display 5 real BSTs
def get_unique_bst_2(bst):
    bst -= 3
    return bst


print('\n#95. Unique Binary Search Trees II:')
test_unique_bst_II = 3
print(get_unique_bst_2(test_unique_bst_II))


# 96. Unique Binary Search Trees
# Only return the number of unique BSTs
def get_unique_bst(bst):
    if bst == 0:
        return 0
    stores = [0] * (bst + 1)
    stores[0] = 1
    stores[1] = 1
    # stores[2] = 2
    # stores[3] = 5
    # stores[4] = 14
    # stores[5] = 42
    # stores[6] = 132
    # stores[7] = 429
    for index in range(2, bst + 1):
        sums = [0] * index
        for inner in range(0, index // 2):
            sums[inner] = 2 * stores[inner] * stores[index - 1 - inner]
        if index % 2 == 0:
            stores[index] = sum(sums)
        else:
            stores[index] = sum(sums) + (stores[index // 2] ** 2)
    return stores[bst]


print('\n#96. Unique Binary Search Trees:')
test_unique_bst = 6
print(get_unique_bst(test_unique_bst))

# 100. Same Tree
# Same structure and same node value
print('\n#100. Same Tree:')

# 104. Maximum Depth of Binary Tree
# Given a binary tree, find its maximum depth
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node
print('\n#104. Maximum Depth of Binary Tree:')
print('done on leetcode')


# 118. Pascal's Triangle
# give 5, return
# [
#           [1],
#          [1, 1],
#        [1, 2, 1],
#      [1, 3, 3, 1],
#     [1, 4, 6, 4, 1]
# ]
def generate_pascal_triangle(num_rows):
    results = [[1] * (r + 1) for r in range(num_rows)]
    if num_rows == 1:
        return [[1]]
    if num_rows == 2:
        return [[1], [1, 1]]
    for r in range(2, num_rows):
        for c in range(1, r):
            results[r][c] = results[r - 1][c - 1] + results[r - 1][c]
    return results


print('\n#118. Pascal\'s Triangle:')
test_generate_pascal_triangle = 10
print(generate_pascal_triangle(test_generate_pascal_triangle))


# 119. Pascal's Triangle II
# Index k, return the kth row
# 0 --> [1]
# 1 --> [1, 1],
# 2 --> [1, 2, 1],
# 3 --> [1, 3, 3, 1],
# 4 --> [1, 4, 6, 4, 1]
# 5 --> [1, 5, 10, 10, 5, 1]
# 6 --> [1, 6, 15, 20, 15, 6, 1]
# Only use O(k) extra space
def get_row(row_index):
    if row_index == 0 or row_index == 1:
        return [1] * (row_index + 1)
    stores = [1, 1]
    for index in range(2, (row_index + 1)):
        stores.append(1)
        stores[-2] += stores[-3]
        for inner in range(3, (index + 1)):
            stores[-inner] += stores[-(inner + 1)]
    return stores


print('\n#119. Pascal\'s Triangle II:')
test_get_row_row_index = 6
print(get_row(test_get_row_row_index))


# 120. Triangle
# From top to bottom, find the min sum
def triangle_min_path(triangle):
    row = len(triangle)
    if row == 1:
        return triangle[0][0]
    stores = [0] * row
    stores[0] = triangle[0][0]

    return stores[-1]


print('\n#120. Triangle:')
test_triangle_min_path = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(triangle_min_path(test_triangle_min_path))
print('NOT DONE')


# 121. Best Time to Buy and Sell Stock
# An array for which the ith element is the price of a given stock on day i.
# At most one transaction (buy one and sell one share of the stock), return the maximum profit.
# [7, 1, 5, 3, 6, 4] => 5
# [7, 6, 4, 3, 1] => 0
# 61.18%
def buy_and_sell_stock_1(prices):
    length = len(prices)
    if length <= 1:
        return 0
    price_min = prices[0]
    profits = [0] * length
    for index, item in enumerate(prices):
        if item < price_min:
            price_min = item
        profits[index] = item - price_min
    return max(profits)


# This one is pretty slow, dont know why
# 5.9%
def buy_and_sell_stock_1_1(prices):
    length = len(prices)
    if length <= 1:
        return 0
    max_prices = [0] * length
    for i in range(1, length):
        max_prices[i] = max(prices[-i], max_prices[i - 1])
    profits = [0] * length
    for j in range(length):
        profits[j] = max_prices[length - j - 1] - prices[j]
    return max(max(profits), 0)


# A little improvement from 1_1
# 21.79%
def buy_and_sell_stock_1_2(prices):
    length = len(prices)
    if length <= 1:
        return 0
    max_prices = [0] * length
    for i in range(1, length):
        max_prices[i] = max(prices[-i], max_prices[i - 1])
    profits = [0] * length
    for j in range(length):
        memo = max_prices[length - j - 1] - prices[j]
        if memo > 0:
            profits[j] = memo
    return max(profits)


print('\n#121. Best Time to Buy and Sell Stock')
test_buy_and_sell_stock = [7, 1, 5, 3, 6, 4]
# test_buy_and_sell_stock = [7, 6, 4, 3, 1]
# test_buy_and_sell_stock = [1, 2]
print(buy_and_sell_stock_1(test_buy_and_sell_stock))
print(buy_and_sell_stock_1_1(test_buy_and_sell_stock))
print(buy_and_sell_stock_1_2(test_buy_and_sell_stock))


# 122. Best Time to Buy and Sell Stock II
# Can make n transactions
# Buy, sell, buy, sell
# Sell before buy
# At most 1 transaction per day
def buy_and_sell_stock_2(prices):
    length = len(prices)
    if length <= 1:
        return 0

    # profit = 0
    # decided = list()
    # not_decided = list()
    # hand = 0

    for i in range(length):
        pass


print('\n#122. Best Time to Buy and Sell Stock II:')
# stock_2_prices = [7, 1, 5, 3, 6, 5]
stock_2_prices = [1, 4, 9, 2, 7, 3]
print(buy_and_sell_stock_2(stock_2_prices))
print('NOT Done...')


# 125. Valid Palindrome
# Only consider alphanumeric characters and ignore cases
# "A man, a plan, a canal: Panama" is a palindrome
# "race a car" is not a palindrome
def is_palindrome(s):
    stores = list()
    for char in s:
        if char.isalnum():
            stores.append(char.lower())
    length = len(stores)
    if length <= 1:
        return True
    first = 0
    last = length - 1
    while first < last:
        if stores[first] != stores[last]:
            return False
        else:
            first += 1
            last -= 1
    return True


def is_palindrome_better(s):
    length = len(s)
    if length <= 1:
        return True
    low = 0
    high = length - 1
    while low <= high:
        if not s[low].isalnum():
            low += 1
        elif not s[high].isalnum():
            high -= 1
        else:
            if s[low].lower() != s[high].lower():
                return False
            else:
                low += 1
                high -= 1
    return True


print('\n#125. Valid Palindrome:')
is_palindrome_s = "A man, a plan, a canal: Panama"
# is_palindrome_s = "race a car"
print(is_palindrome(is_palindrome_s))
print(is_palindrome_better(is_palindrome_s))


# 134. Gas Station
# N gas stations from 0, to n -1
# Gas at station i is gas[i], it costs cost[i] to go from i to (i + 1)
# Return the starting station's index if can travel around
# Return -1 if not
# The solution is guaranteed to be unique
def can_complete_circuit(gas, cost):
    if sum(cost) > sum(gas):
        return -1
    start = 0
    total = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            start = i + 1
            total = 0
    return start


print('\n#134. Gas Station:')


# 135. Candy
# n children
# every child at least one candy
# Children with a higher rating get more candies than their neighbors
def candy(ratings):
    length = len(ratings)
    candies = [1] * length
    for i in range(1, length):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for j in range(length - 2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            candies[j] = max(candies[j], candies[j + 1] + 1)
    return sum(candies)


# candy_ratings = [1, 2, 3]
# candy_ratings = [1, 2, 3, 7, 4, 3, 2, 1]
candy_ratings = [3, 7, 4, 2, 1, 1, 2]
print('\n#135. Candy')
print(candy(candy_ratings))


# 136. Single Number:
# An array of integers, every element appears twice except for one element.
# Find that single element.
# Linear runtime, without using extra memory
def get_single_number(nums):
    ans = 0
    for item in nums:
        ans ^= item
    return ans


print('\n#136. Single Number:')
test_single_number = [1, 1, 2, 2, 3, 4, 4]
print(get_single_number(test_single_number))


# 137. Single Number II
# (3 * n) + 1 numbers
# return the single number
def get_single_number_2(nums):
    ans = 0
    for item in nums:
        ans ^= item
    return ans


print('\n#137. Single Number II:')
single_number_2_nums = [1, 2, 3, 3, 2, 1, 374, 2, 1, 3]
print(get_single_number_2(single_number_2_nums))
print('NOT done')


# 168. Excel Sheet Column Title
# 1 --> A
# 2 --> B
# 3 --> C
# 26 --> Z
# 27 --> AA
# 28 --> AB
# 52 --> AZ
# 53 --> BA
def convert_to_title(n):
    stores = dict()
    for i in range(26):
        stores[i] = chr(i + 65)
    # print(stores)
    if n <= 26:
        return stores[n - 1]
    whole = n // 26
    remainder = n % 26
    print(whole)
    print(remainder)
    return stores[whole - 1] + stores[remainder - 1]


print('\n#168. Excel Sheet Column Title:')
convert_to_title_n = 52
# print(convert_to_title(convert_to_title_n))
print('NOT done...')


# 153. Find Minimum in Rotated Sorted Array
# [0, 1, 2, 4, 5, 6, 7] rotated to [4, 5, 6, 7, 0, 1, 2]
# return the min value
def find_min_in_rotated_sorted_array(nums):
    low = 0
    high = len(nums) - 1
    while low < high and nums[low] >= nums[high]:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]


print('\n#153. Find Minimum in Rotated Sorted Array:')
find_min_in_rotated_sorted_array_nums = [2, 3, 4, 5, 6]
print(find_min_in_rotated_sorted_array(find_min_in_rotated_sorted_array_nums))


# 169. Majority Element:
# Array of size n, the majority element is the element that appears more than math.floor(n/2) times
# Array is non-empty and the majority element always exists
def get_majority_element(majority):
    major_dict = {}
    for major in majority:
        if major in major_dict:
            major_dict[major] += 1
        else:
            major_dict[major] = 1
    # print(major_dict)
    # print(max(major_dict))  # max key
    # print(max(major_dict.values()))  # max value
    # print(max(major_dict, key=major_dict.get))  # key of max value
    # print(major_dict[max(major_dict)])  # value of max key
    return max(major_dict, key=major_dict.get)


def majority_element(nums):
    majors = {}
    for major in nums:
        if major in majors:
            majors[major] += 1
        else:
            majors[major] = 1
    majority = nums[0]
    count = majors[majority]
    for key, value in majors.items():
        if value > count:
            count = value
            majority = key
    return majority


def majority_element_constant_space(nums):
    nums = sorted(nums)
    current_majority = nums[0]
    current_count = 1
    index = 1
    while index < len(nums):
        count = 1
        for i in range(index, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                break
        if count > current_count:
            current_count = count
            current_majority = nums[index]
        index += count
    return current_majority


def majority_element_constant_space_better(nums):
    nums = sorted(nums)
    return nums[len(nums) // 2]


def majority_element_constant_space_best(nums):
    result = 0
    count = 0
    for num in nums:
        if count == 0:
            result = num
            count = 1
        elif num == result:
            count += 1
        else:
            count -= 1
    return result


print('\n#169. Majority Element:')
test_majority = [1, 2, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 4, 5, 5, 5]
# test_majority = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3]
print(get_majority_element(test_majority))
print(majority_element(test_majority))
print(majority_element_constant_space(test_majority))
print(majority_element_constant_space_better(test_majority))
print(majority_element_constant_space_best(test_majority))


# 171. Excel Sheet Column Number
def excel_column_number(string):
    string = string.upper()
    print(string)
    stores = {}
    for i in range(1, 27):
        stores[chr(64 + i)] = i
    length = len(string)
    result = 0
    for i in range(length):
        result += (pow(26, i)) * stores[string[-i - 1]]
    return result


print('\n#171. Excel Sheet Column Number')
test_excel_column_number = 'ac'
print(excel_column_number(test_excel_column_number))


# 172. Factorial Trailing Zeroes
# Return the number of trailing zeroes in n!
# Logarithmic time complexity.
# 11! = 39916800, return 2
# one (2, 5) pair --> one zero
# 2 is anywhere, so one 5 --> one zero
# one 10 --> two zeroes
def factorial(n):
    stores = [1] * (n + 1)
    for n in range(2, n + 1):
        stores[n] = n * stores[n - 1]
    return stores[-1]


def trailing_zeroes(n):
    five_count = n // 5
    return five_count


print('\n#172. Factorial Trailing Zeroes:')
test_trailing_zeroes_n = 25
# test_trailing_zeroes_n = 24
print(factorial(24))
print(factorial(test_trailing_zeroes_n))
print(trailing_zeroes(test_trailing_zeroes_n))
print('Not done......')


# 189. Rotate Array
# Rotate an array of n elements to the right by k steps
# n = 7, k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]
# :return type is void so do not return anything, modify nums in-place instead.
def move_list_last_to_first(move):
    length = len(move)
    if length <= 1:
        return move
    new_first = move[-1]
    new_first_list = [new_first]
    move = move[::-1]
    move = move[1::]
    move = move[::-1]
    move = new_first_list + move
    return move


def rotate_array(rotate, k):
    print(rotate)
    length = len(rotate)
    if length <= 1:
        return rotate
    result = rotate[::]
    result[0] = rotate[::]
    for index in range(1, length):
        result[index] = move_list_last_to_first(result[index - 1])
    print(rotate)
    return result[k % length]


def rotate_array_no_return_in_place_modify(rotate, k):
    print(rotate)
    length = len(rotate)
    rotate = rotate[::]
    if length <= 1:
        pass
    else:
        result = rotate[::]
        result[0] = rotate[::]
        for index in range(1, length):
            result[index] = move_list_last_to_first(result[index - 1])
        rotate = result[k % length]
    print(rotate)


def rotate_array_one_func(nums, k):
    print(nums)
    length = len(nums)
    k %= length
    temp = nums[:length - k]
    for i in range(length):
        if i < k:
            nums[i] = nums[length - k + i]
        else:
            nums[i] = temp[i - k]
    print(nums)


def rotate_new_0(nums, k):
    # O(n) time, O(n) space
    print(nums)
    if not nums:
        pass
    else:
        length = len(nums)
        if length <= 1:
            pass
        else:  # length >= 2
            k %= length
            temp = list()
            for i in range(length - k, length):
                temp.append(nums[i])
            for j in range(length - k - 1, -1, -1):
                nums[j + k] = nums[j]
            for l in range(k):
                nums[l] = temp[l]
    print(nums)


def rotate_new_1(nums, k):
    # O(n) time, O(n) space
    print(nums)
    if not nums:
        pass
    else:
        length = len(nums)
        if length <= 1:
            pass
        else:  # length >= 2
            k %= length
            for i in range(length - k, length):
                nums.append(nums[i])
            for j in range(length - k - 1, -1, -1):
                nums[j + k] = nums[j]
            for l in range(k):
                nums[l] = nums[l + length]
            for m in range(k):
                nums.pop()
    print(nums)


def rotate_new_2(nums, k):
    # O(n * k) time, O(1) space
    # Time Limit Exceeded on leetcode
    print(nums)
    if not nums:
        pass
    else:
        length = len(nums)
        if length <= 1:
            pass
        else:  # length >= 2
            k %= length
            for i in range(k):
                right_shift_a_list(nums)
    print(nums)


def right_shift_a_list(nums):
    if not nums:
        pass
    else:
        length = len(nums)
        if length <= 1:
            pass
        else:
            temp = nums[-1]
            for i in range(length - 2, -1, -1):
                nums[i + 1] = nums[i]
            nums[0] = temp


def rotate_new_3(nums, k):
    # O(n) time, O(1) space
    print(nums)
    if not nums:
        pass
    else:
        length = len(nums)
        if length <= 1:
            pass
        else:  # length >= 2
            k %= length
            reverse_partial_list(nums, 0, length - k - 1)
            reverse_partial_list(nums, length - k, length - 1)
            reverse_partial_list(nums, 0, length - 1)
    print(nums)


def reverse_partial_list(nums, first, last):
    if not nums:
        pass
    else:
        length = len(nums)
        if length <= 1:
            pass
        else:
            while first < last:
                temp = nums[first]
                nums[first] = nums[last]
                nums[last] = temp
                first += 1
                last -= 1


print('\n#189. Rotate Array:')
test_rotate_array = [1, 2, 3, 4, 5, 6, 7]
test_rotate_k = 3
rotate_array(test_rotate_array, test_rotate_k)

test_rotate_array_no_return = [1, 2, 3, 4, 5, 6, 7]
rotate_array_no_return_in_place_modify(test_rotate_array_no_return, test_rotate_k)

test_rotate_array_one_func = [1, 2, 3, 4, 5, 6, 7]
rotate_array_one_func(test_rotate_array_one_func, test_rotate_k)

print('rotate_new_0:')
rotate_new_0_nums = [1, 2, 3, 4, 5, 6, 7]
rotate_new_0(rotate_new_0_nums, test_rotate_k)

print('rotate_new_1:')
rotate_new_1_nums = [1, 2, 3, 4, 5, 6, 7]
rotate_new_1(rotate_new_1_nums, test_rotate_k)

print('rotate_new_2:')
rotate_new_2_nums = [1, 2, 3, 4, 5, 6, 7]
rotate_new_2(rotate_new_2_nums, test_rotate_k)

print('rotate_new_3:')
rotate_new_3_nums = [1, 2, 3, 4, 5, 6, 7]
rotate_new_3(rotate_new_3_nums, test_rotate_k)


# 190. Reverse Bits
# Reverse bits of a given 32 bits unsigned integer
# 43261596 --> 964176192
# 00000010100101000001111010011100
# 00000010100101000001111010011100
# 00111001011110000010100101000000
def reverse_bits(n):
    # binary = bin(n)
    binary = bin(n)[2:].zfill(32)
    print(binary)
    return int(binary, 2)


print('\n#190. Reverse Bits:')
reverse_bits_n = 43261596
print(reverse_bits(reverse_bits_n))


# 191. Number of 1 bits
# The 32-bit integer 11 has binary representation 00000000000000000000000000001011, return 3
def hamming_weight(n):
    number = bin(n)[2:].zfill(32)
    count = 0
    for letter in number:
        if letter == '1':
            count += 1
    return count


print('\n#191. Number of 1 bits:')
test_hamming_weight = 11
print(hamming_weight(test_hamming_weight))


# 198. House Robber
# A list of non-negative integers, get the max money
def rob_house(moneys):
    length = len(moneys)
    if length == 0:
        return 0
    if length == 1:
        return moneys[0]
    if length == 2:
        return max(moneys[0], moneys[1])
    stores = [0] * length
    stores[0] = max(moneys[length - 1], 0)
    stores[1] = max(moneys[length - 2], stores[0])
    for index in range(2, length):
        stores[index] = max((moneys[length - index - 1] + stores[index - 2]), stores[index - 1])
    print(stores)
    return stores[-1]


print('\n#198. House Robber:')
test_rob_house = [3, 1, 4, 2, 1, 5]
print(rob_house(test_rob_house))


# 202. Happy Number
# 1, 19, 2003, 200000000000000000000000003 --> True
def is_happy(n):
    stores = [0] * 2000
    while True:
        n = square_sum(n)
        if n == 1:
            return True
        elif stores[n] == 2:
            return False
        else:
            stores[n] += 1


def square_sum(ss_num):
    ss_sum = 0
    while ss_num:
        ss_sum += (ss_num % 10) ** 2
        ss_num //= 10
    return ss_sum


print('\n#202. Happy Number:')
test_is_happy = 2003
print(is_happy(test_is_happy))


# 204. Count Primes:
# Count the number of prime numbers < a non-negative number, n
# n = 0, 1, 2, 3, 4, 5 ...
# 1 is NOT a prime number
# count_prime_1 counts the most amount of numbers
# count_prime_2 passes leetcode
# count_prime_3 counts the least amount, but it exceeds time limit in leetcode, don't know why
def count_prime_1(n):
    if n <= 2:
        return 0
    origin_nums = list(range(2, n))
    primes = list()
    for index, item in enumerate(origin_nums):
        if item != 0:
            primes.append(item)
            for j in range(index + 1, len(origin_nums)):
                if origin_nums[j] % item == 0:
                    origin_nums[j] = 0
                j += 1
    return len(primes)


def count_prime_2(n):
    if n <= 2:
        return 0
    is_prime = [True for _ in range(n)]
    is_prime[0] = False
    is_prime[1] = False
    for num in range(2, int(math.sqrt(n)) + 1):
        if is_prime[num]:
            for j in range(num ** 2, n, num):
                is_prime[j] = False
    return is_prime.count(True)


def count_prime_3(n):
    if n <= 2:
        return 0
    stores = [0] * n
    stores[0] = 1
    stores[1] = 1
    primes = list()
    for num in range(2, n):
        if stores[num] == 0:
            primes.append(num)
            for prime in primes:
                memo = num * int(prime)
                if memo < n:
                    stores[memo] += 1
        elif num % 2 == 0:
            memo = num * 2
            if memo < n:
                stores[memo] += 1
        else:
            for prime in primes:
                memo = num * int(prime)
                if prime <= math.sqrt(num) and memo < n:
                    stores[memo] += 1
    return len(primes)


print('\n#204. Count Primes:')
test_count_prime = 1000
print('There are', count_prime_1(test_count_prime), 'prime numbers less than', test_count_prime)
print(count_prime_1(test_count_prime))
print(count_prime_2(test_count_prime))
print(count_prime_3(test_count_prime))


# 205. Isomorphic Strings
# egg, add --> True
# foo, bar --> False
# paper, title --> True
# aba, baa --> False
# s and t have same length
def is_isomorphic(s, t):
    length = len(s)
    if length <= 1:
        return True
    stores = dict()
    for i in range(length):
        letter_s = s[i: i + 1]
        letter_t = t[i: i + 1]
        if letter_s in stores:
            if stores[letter_s] != letter_t:
                return False
        else:
            stores[letter_s] = letter_t
    stores.clear()
    for i in range(length):
        letter_s = s[i: i + 1]
        letter_t = t[i: i + 1]
        if letter_t in stores:
            if stores[letter_t] != letter_s:
                return False
        else:
            stores[letter_t] = letter_s
    return True


print('\n#205. Isomorphic Strings:')
is_isomorphic_s = 'ab'
is_isomorphic_t = 'aa'
print(is_isomorphic(is_isomorphic_s, is_isomorphic_t))
print('done, but it has some wet code...')


# 206. Reverse Linked List
# Reverse a singly linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    if not head:
        return None
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


print('\n#206. Reverse Linked List:')
print('Done')


# 213. House Robber II
# Houses are in a circle
# Money in each house is >= 0 integer
def rob_house_normal_array(nums):
    length = len(nums)
    if length == 0:
        return 0
    if length == 1:
        return nums[0]
    if length == 2:
        return max(nums[0], nums[1])
    stores = [0] * length
    stores[0] = nums[0]
    stores[1] = max(nums[0], nums[1])
    for index in range(2, length):
        stores[index] = max(nums[index] + stores[index - 2], stores[index - 1])
    return stores[-1]


def rob_house_2(nums):
    length = len(nums)
    if length == 0:
        return 0
    if length == 1:
        return nums[0]
    if length == 2:
        return max(nums[0], nums[1])
    if length == 3:
        return max(nums[0], nums[1], nums[2])
    stores = [0] * length
    stores[0] = nums[0]
    stores[1] = max(nums[1], nums[0])
    for index in range(2, length - 1):
        stores[index] = max(nums[index] + stores[index - 2], stores[index - 1])
    stores[-1] = max(stores[-2], nums[-1] + rob_house_normal_array(nums[1:length - 2]))
    return stores[-1]


print('\n#213. House Robber II:')
test_rob_house_2 = [3, 1, 4, 2, 1, 5]
print(rob_house_2(test_rob_house_2))


# 217. Contains Duplicate
# An array of integers, return true if contain duplicate
def if_contain_duplicate(nums):
    length = len(nums)
    if length <= 1:
        return False
    stores = set(nums)
    if len(stores) == len(nums):
        return False
    else:
        return True


def if_contain_duplicate_hash(nums):
    # O(n) time, O(n) space
    if not nums:
        return False
    length = len(nums)
    if length <= 1:
        return False
    stores = dict()
    for num in nums:
        if num in stores:
            return True
        else:
            stores[num] = 1
    return False


def if_contain_duplicate_sort(nums):
    # O(nlgn) time, O(1) space
    if not nums:
        return False
    length = len(nums)
    if length <= 1:
        return False
    nums = sorted(nums)
    for i in range(1, length):
        if nums[i] == nums[i - 1]:
            return True
    return False


print('\n#217. Contains Duplicate:')
test_if_contain_duplicate = [1, 2, 1]
print(if_contain_duplicate(test_if_contain_duplicate))
print(if_contain_duplicate_hash(test_if_contain_duplicate))
print(if_contain_duplicate_sort(test_if_contain_duplicate))


# 219. Contains Duplicate II
# An integer k
# Two distinct indices i and j, |i - j| is at most k
# k = 1, 2, 3, 4...
# Return whether nums[i] = nums[j] exists
def contains_nearby_duplicate(nums, k):
    length = len(nums)
    if length <= 1:
        return False
    stores = dict()
    for index, item in enumerate(nums):
        if item in stores:
            if index - stores[item] <= k:
                return True
        stores[item] = index
    return False


print('\n#219. Contains Duplicate II:')
contains_nearby_duplicate_nums = [0, 1, 2, 3, 4, 5, 5]
contains_nearby_duplicate_k = 1
print(contains_nearby_duplicate(contains_nearby_duplicate_nums, contains_nearby_duplicate_k))


# 220. Contains Duplicate III
# An integer k
# Two distinct indices i and j
# |i - j| is at most k
# |nums[i] - nums[j]| is at most t
# k = 1, 2, 3, 4...
# t = 0, 1, 2, 3, 4...
# Return whether nums[i] = nums[j] exists
def contains_nearby_almost_duplicate(nums, k, t):
    length = len(nums)
    if length <= 1 or t < 0:
        return False
    if k >= length - 1:
        if max(nums) - min(nums) <= t:
            return True
        else:
            return False
    for index in range(length - k):
        if max(nums[index:index + k + 1]) - min(nums[index:index + k + 1]) <= t:
            return True
        else:
            return False


print('\n#220. Contains Duplicate III:')
almost_duplicate_nums = [1, 2]
almost_duplicate_k = 1
almost_duplicate_t = 0
print(contains_nearby_almost_duplicate(almost_duplicate_nums, almost_duplicate_k, almost_duplicate_t))
print('NOT done...')


# 223. Rectangle Area
# (a, b) is bottom-left point
# (c, d) is top-right point
def compute_area(a, b, c, d, e, f, g, h):
    ac = list()
    for i in range(a, c + 1):
        ac.append(i)
    ac_set = set(ac)
    eg = list()
    for i in range(e, g + 1):
        eg.append(i)
    eg_set = set(eg)
    horizontal = ac_set & eg_set
    if horizontal:
        width = max(horizontal) - min(horizontal)
    else:
        width = 0

    bd = list()
    for i in range(b, d + 1):
        bd.append(i)
    bd_set = set(bd)
    fh = list()
    for i in range(f, h + 1):
        fh.append(i)
    fh_set = set(fh)
    vertical = bd_set & fh_set
    if vertical:
        height = max(vertical) - min(vertical)
    else:
        height = 0

    return ((c - a) * (d - b)) + ((g - e) * (h - f)) - (width * height)


# def compute_area_1(A, B, C, D, E, F, G, H):
#     ac = list()
#     for i in range(A, C + 1):
#         ac.append(i)
#     ac_set = set(ac)
#     eg = list()
#     for i in range(E, G + 1):
#         eg.append(i)
#     eg_set = set(eg)
#     horizontal = ac_set & eg_set
#     if horizontal:
#         width = max(horizontal) - min(horizontal)
#     else:
#         width = 0
#
#     bd = list()
#     for i in range(B, D + 1):
#         bd.append(i)
#     bd_set = set(bd)
#     fh = list()
#     for i in range(F, H + 1):
#         fh.append(i)
#     fh_set = set(fh)
#     vertical = bd_set & fh_set
#     if vertical:
#         height = max(vertical) - min(vertical)
#     else:
#         height = 0
#
#     return ((C - A) * (D - B)) + ((G - E) * (H - F)) - (width * height)
print('\n#223. Rectangle Area:')
area_a = 0
area_b = 0
area_c = 0
area_d = 0
area_e = -1
area_f = -1
area_g = 1
area_h = 1
print(compute_area(area_a, area_b, area_c, area_d, area_e, area_f, area_g, area_h))
# print(compute_area_1(area_a, area_b, area_c, area_d, area_e, area_f, area_g, area_h))
print('done but too slow...')

# 226. Invert Binary Tree
# Swap nodes on same level
print('\n#226. Invert Binary Tree:')


# 229. Majority Element II
# size n, find all elements that appear more than floor(n/3)
# O(n) time, O(1) space
def majority_element_ii(nums):
    if not nums:
        return []
    length = len(nums)
    if length <= 1:
        return nums
    result = list()
    result_0 = nums[0]
    result_1 = nums[1]
    count_0 = 0
    count_1 = 0
    for num in nums:
        if num == result_0:
            count_0 += 1
        elif num == result_1:
            count_1 += 1
        elif count_0 == 0:
            result_0 = num
            count_0 = 1
        elif count_1 == 0:
            result_1 = num
            count_1 = 1
        else:
            count_0 -= 1
            count_1 -= 1
    if result_0 == result_1:
        if nums.count(result_0) > length // 3:
            return [result_0]
        else:
            return []
    for item in (result_0, result_1):
        if nums.count(item) > length // 3:
            result.append(item)
    return result


majority_element_ii_nums = [1, 2, 3, 3, 3, 4, 4, 4]
# majority_element_ii_nums = [2, 2]
print('\n#229. Majority Element II')
print(majority_element_ii(majority_element_ii_nums))


# 231. Power of Two
# 1, 2, 4, 8, 16, 32 --> True
# 0, 3, 5, 6, 7, 9 --> False
def is_power_of_two(n):
    if n == 0:
        return False
    if n == 1 or n == 2:
        return True
    if n % 2 == 1:
        return False
    while not (n % 2):
        n //= 2
        if n == 2:
            return True
    return False


print('\n#231. Power of Two:')
test_is_power_of_two = 6
print(is_power_of_two(test_is_power_of_two))

# 237. Delete Node in a Linked List
print('\n#237. Delete Node in a Linked List:')
print('done on leetcode')


# 238. Product of Array Except Self
# array of n integers, n > 1 (n = 2, 3, 4...)
# return an array output, output[i] = product of all elements of nums except nums[i]
# solve it without division and in O(n)
# [1, 2, 3, 4] ==> [24, 12, 8, 6]
# try to do it in constant space
def product_except_self(nums):
    # O(n) time, O(n) space
    length = len(nums)
    left = [1] * length
    right = [1] * length
    result = [1] * length
    for i in range(1, length):
        left[i] = left[i - 1] * nums[i - 1]
    for j in range(length - 2, -1, -1):
        right[j] = right[j + 1] * nums[j + 1]
    for k in range(length):
        result[k] = left[k] * right[k]
    return result


def product_except_self_constant_space(nums):
    # O(n) time, O(1) space
    length = len(nums)
    result = [1] * length
    for i in range(1, length):
        result[i] = result[i - 1] * nums[i - 1]
    num = 1
    for j in range(length - 2, -1, -1):
        num *= nums[j + 1]
        result[j] *= num
    return result


product_except_self_nums = [1, 2, 3, 4]
print('\n#238. Product of Array Except Self:')
print(product_except_self(product_except_self_nums))
print(product_except_self_constant_space(product_except_self_nums))


# 242. Valid Anagram
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# only lowercase alphabets
def is_anagram_lowercase(s, t):
    stores = dict()
    for i in range(97, 123):
        stores[chr(i)] = 0
    for letter in s:
        stores[letter] += 1
    for letter in t:
        stores[letter] -= 1
    for key, value in stores.items():
        if value != 0:
            return False
    return True


# This one is faster than the lowercase one
def is_anagram_dict(s, t):
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        return False
    letters = dict()
    for item in s:
        if item in letters:
            letters[item] += 1
        else:
            letters[item] = 1
    for letter in t:
        if letter not in letters:
            return False
        letters[letter] -= 1
        if letters[letter] < 0:
            return False
    return True


# Faster than lowercase but slower than dict one
def is_anagram_sort_first(s, t):
    s_len = len(s)
    t_len = len(t)
    if s_len != t_len:
        return False
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))
    if s == t:
        return True
    else:
        return False


print('\n#242. Valid Anagram:')
is_anagram_s = 'anagram'
is_anagram_t = 'nagaram'
print(is_anagram_lowercase(is_anagram_s, is_anagram_t))
print(is_anagram_dict(is_anagram_s, is_anagram_t))
print(is_anagram_sort_first(is_anagram_s, is_anagram_t))
print(is_anagram_sort_first('', ''))


# 258. Add Digits:
# Add all digits until the result has only one digit
# Return this one digit
# Without any loop/recursion in O(1) runtime
def add_digits(num):
    answer = 0
    length = len(str(num))
    for i in range(length):
        answer += (num % 10)
        if answer >= 10:
            answer = (answer % 10) + (answer // 10)
        num //= 10
    return answer


print('\n#258. Add Digits:')
test_add_digits = 38
print(add_digits(test_add_digits))


# 263. Ugly Number
# positive integer whose prime factors only include 2, 3, 5
# 6, 8 --> True
# 14 --> False (because it has another prime factor)
# Special, 1 is an ugly number
def is_ugly(num):
    if num == 1:
        return True
    while not (num % 2):
        num //= 2
    while not (num % 3):
        num //= 3
    while not (num % 5):
        num //= 5
    if num == 1:
        return True
    else:
        return False


print('\n#263. Ugly Number:')
test_is_ugly = 10
print(is_ugly(test_is_ugly))
print('Not done. it takes too much time......')


# 278. First Bad Version
# You have n versions [1, 2, ..., n] and you want to find out the first bad one
# Versions after a bad version are all bad versions
def first_bad_version(arr, n):
    first = 0
    last = n - 1
    middle = (first + last) // 2
    while first <= last:
        if arr[middle] == 0:
            last = middle - 1
            middle = (first + last) // 2
        else:
            first = middle + 1
            middle = (first + last) // 2
    return first + 1


print('\n#278. First Bad Version:')
# first_bad_cctv_index = [0, 1, 2, 3, 4]
# first_bad_ctv_result = [1, 2, 3, 4, 5]
first_bad_version_list = [1, 1, 1, 0]
first_bad_version_n = len(first_bad_version_list)
print(first_bad_version(first_bad_version_list, first_bad_version_n))


# 279. Perfect Squares
# A positive integer n, find the least number of perfect square numbers(1, 4, 9, 16, ...) which sum to n
# n = 12, return 3, because 12 = 4 + 4 + 4
# n = 13, return 2, because 13 = 4 + 9
# perfect_squares(n) is wrong
# perfect_squares_1(n) is right, but slow
# perfect_squares_2(n) is do it later
def perfect_squares(n):
    sqrt = math.floor(math.sqrt(n))
    stores = [0] * (n + 1)
    stores[1] = 1
    for outer in range(1, sqrt):
        stores[outer ** 2] = 1
        for inner in range((outer ** 2) + 1, (outer + 1) ** 2):
            stores[inner] = 1 + stores[inner - (outer ** 2)]
    if sqrt == math.ceil(math.sqrt(n)):
        stores[sqrt ** 2] = 1
    if sqrt != math.ceil(math.sqrt(n)):
        stores[sqrt ** 2] = 1
        for index in range((sqrt ** 2) + 1, n + 1):
            stores[index] = 1 + stores[index - (sqrt ** 2)]
    # print(sqrt)
    # print(stores)
    return stores[-1]


def perfect_squares_1(n):
    while n % 4 == 0:
        n //= 4
    if math.floor(math.sqrt(n)) == math.ceil(math.sqrt(n)):
        return 1
    if n % 8 == 7:
        return 4
    sqrt = math.floor(math.sqrt(n))
    for a in range(1, sqrt + 1):
        b = math.floor(math.sqrt(n - a ** 2))
        if (a ** 2) + (b ** 2) == n:
            return 2
    return 3


print('\n#279. Perfect Squares:')
test_perfect_squares = 646
print(perfect_squares(test_perfect_squares))
print(perfect_squares_1(test_perfect_squares))


# 283. Move Zeros:
# An array of integers, move zeros to the end, keep the relative order of other numbers
# Return the new array
# in-place, no copy of the array
# Minimize the total number of operations
# Do not return anything, modify nums in-place instead.
def move_zeroes(zero_nums):
    print(zero_nums)
    move_times = 0
    move_index = 0
    while move_times < len(zero_nums):
        if zero_nums[move_index] == 0:
            del zero_nums[move_index]
            zero_nums.append(0)
        else:
            move_index += 1
        move_times += 1
    print(zero_nums)


def move_zeroes_better(nums):
    print(nums)
    length = len(nums)
    index = 0
    for i in range(length):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for j in range(index, length):
        nums[j] = 0
    print(nums)


print('\n#283. Move Zeros:')
move_zeros_nums = [0, 1, 0, 3, 12]
move_zeros_better_nums = [0, 1, 0, 3, 12]
move_zeroes(move_zeros_nums)
move_zeroes_better(move_zeros_better_nums)


# 289. Game of Life
# 8 neighbors
# live 1, dead 0
# live, = 0 or 1 live nb, die.  -1
# live, = 2 or 3 live nb, live. 0
# live, > 3 live nb, die.       -1
# dead, = 3 live nb, live.      +1
# Define 4 states by myself:
# 0: die to die   (origin is die)
# 1: live to live (origin is live)
# 2: live to die  (origin is live)
# 3: die to live  (origin is die)
def game_of_life(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    O(m x n) time, O(1) space
    """
    print(board)
    if not board:
        pass
    else:
        row_len = len(board)
        if row_len == 0:
            pass
        else:
            col_len = len(board[0])
            if col_len == 0:
                pass
            else:
                for i in range(row_len):
                    for j in range(col_len):
                        if board[i][j] == 0:
                            if count_live(board, i, j) == 3:
                                board[i][j] = 3
                        else:  # origin is live
                            if count_live(board, i, j) < 2 or count_live(board, i, j) > 3:
                                board[i][j] = 2
                for k in range(row_len):
                    for l in range(col_len):
                        board[k][l] %= 2
    print(board)


def count_live(nums, row, col):
    if not nums:
        return 0
    row_len = len(nums)
    if row_len == 0:
        return 0
    col_len = len(nums[0])
    if col_len == 0:
        return 0
    result = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < row_len and 0 <= j < col_len:
                if nums[i][j] == 1 or nums[i][j] == 2:
                    result += 1
    if nums[row][col] == 1 or nums[row][col] == 2:
        result -= 1
    return result


game_of_life_board = [
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
print('\n#289. Game of Life')
game_of_life(game_of_life_board)


# 290. Word Pattern
# pattern = 'abba'
# str = 'dog cat cat dog'
# return True
def word_pattern(pattern, string):
    pattern_to_str = False
    str_to_pattern = False
    len_pattern = len(pattern)
    stores = dict()
    words = string.split()
    len_string = len(words)
    if len_pattern != len_string:
        return False
    for i in range(len_pattern):
        if pattern[i] in stores:
            if stores[pattern[i]] != words[i]:
                return False
        else:
            stores[pattern[i]] = words[i]
        if i == len_pattern - 1:
            pattern_to_str = True

    stores.clear()
    for i in range(len_pattern):
        if words[i] in stores:
            if stores[words[i]] != pattern[i]:
                return False
        else:
            stores[words[i]] = pattern[i]
        if i == len_pattern - 1:
            str_to_pattern = True

    return pattern_to_str and str_to_pattern


print('\n#290. Word Pattern:')
word_pattern_pattern = 'abba'
word_pattern_string = 'dog cat cat dog'
print(word_pattern(word_pattern_pattern, word_pattern_string))


# 292. Nim Game:
# Remove 1 or 2 or 3 stones a time
# I take the first nim
# The one who removes the last stone wins
# n stones
# return true if I win, false if my friend wins
# If there are 4 stones, I will never win, return False
def nim_game(stone_num):
    return stone_num % 4 != 0


print('\n#292. Nim Game:')
test_nim_game = 4
print(nim_game(test_nim_game))


# 299. Bulls and Cows
# bulls: match both digit and position --> A
# cows: match digit but wrong position --> B
# secret: '1807'
# guess : '7810'
# bulls = 1, cows = 3, return '1A3B'
# secret and guess may contain duplicates
# secret = '1123'
# guess = '0111'
# return '1A1B'
# secret and guess only contain digits and equal length
def bulls_and_cows(secret, guess):
    length = len(secret)
    bull = 0
    cow = 0
    stores = dict()
    for i in range(length):
        if secret[i] == guess[i]:
            bull += 1
        try:
            stores[secret[i]] += 1
        except KeyError:
            stores[secret[i]] = 1
    for i in range(length):
        if guess[i] in stores and stores[guess[i]] != 0:
            cow += 1
            stores[guess[i]] -= 1
    cow -= bull
    return str(bull) + 'A' + str(cow) + 'B'


print('\n#299. Bulls and Cows:')
bulls_and_cows_secret = '1807'
bulls_and_cows_guess = '7810'
print(bulls_and_cows(bulls_and_cows_secret, bulls_and_cows_guess))


# 300. Longest Increasing Subsequence
# An unsorted array of integers, find the length of longest increasing subsequence.
# Given [10, 9, 2, 5, 3, 7, 101, 18]
# Longest increasing subsequence is [2, 3, 7, 101], return 4 (the length)
# O(n^2) is ok, try to get O(n * lgn)
# lis() is a wrong answer, it does not work form some lists
# lis_1() is ok, O(n^2)
# lis_2() should be O(n * lgn), try it later
def lis(nums):
    length = len(nums)
    if length <= 1:
        return length
    if length == 2:
        if nums[0] < nums[1]:
            return 2
        else:
            return 1
    middle = length // 2
    result_contain_middle = 1

    left_min = nums[middle]
    left_count = 0
    for left in range(middle - 1, -1, -1):
        if nums[left] < left_min:
            left_min = nums[left]
            left_count += 1
    result_contain_middle += left_count

    right_max = nums[middle]
    right_count = 0
    for right in range(middle + 1, length, 1):
        if nums[right] > right_max:
            right_max = nums[right]
            right_count += 1
    result_contain_middle += right_count

    return max(result_contain_middle, lis(nums[:middle:]), lis(nums[middle + 1::]))


def lis_1(nums):
    length = len(nums)
    if length == 0:
        return 0
    results = [0] * length
    for middle in range(0, length):
        result_contain_middle = 1
        left_min = nums[middle]
        left_count = 0
        for left in range(middle - 1, -1, -1):
            if nums[left] < left_min:
                left_min = nums[left]
                left_count += 1
        result_contain_middle += left_count
        right_max = nums[middle]
        right_count = 0
        for right in range(middle + 1, length, 1):
            if nums[right] > right_max:
                right_max = nums[right]
                right_count += 1
        result_contain_middle += right_count
        results[middle] = result_contain_middle
    return max(results)


print('\n#300. Longest Increasing Subsequence:')
# test_lis = [10, 9, 2, 5, 3, 7, 101, 18]
test_lis = [10, 9, 2, 5, 3, 4]  # lis does not work for these ones
# test_lis = [5]
print(lis(test_lis))
print(lis_1(test_lis))


# 303. Range Sum Query - Immutable
# An integer array, find the sum of the elements between indices i and j (i <= j), inclusive.
# The array does not change, there are many calls to sum_range.
# [-2, 0, 3, -5, 2, -1]
# sum_range(0, 2) -> 1
# sum_range(2, 5) -> -1
# sum_range(0, 5) -> -3
# It is easy to get a solution, but in order to be efficient, I need to work out a new way, Dynamic Programming...
def sum_range(range_nums, i, j):
    length = len(range_nums)
    if i > (length - 1) or j > (length - 1):
        return 0
    result = 0
    for index in range(i, j + 1):
        result += range_nums[index]
    return result


def sum_range_dp(range_nums, i, j):
    length = len(range_nums)
    if i > (length - 1) or j > (length - 1):
        return 0
    stores = [0] * (length + 1)
    for index in range(1, length + 1):
        stores[index] = stores[index - 1] + range_nums[index - 1]
    return stores[j + 1] - stores[i]


print('\n#303. Range Sum Query - Immutable:')
test_sum_range = [-2, 0, 3, -5, 2, -1]
test_sum_range_i = 0
test_sum_range_j = 5
print(sum_range(test_sum_range, test_sum_range_i, test_sum_range_j))
print(sum_range_dp(test_sum_range, test_sum_range_i, test_sum_range_j))


# 309. Best Time to Buy and Sell Stock with Cooldown
# Buy one and sell one multiple times with the following restrictions:
# You may not engage in multiple transactions at the same time (ie. you must sell the stock before your buy again)
# After you sell your stock, you cannot buy stock on next day(ie. cooldown 1 day)
# prices = [1, 2, 3, 0, 2]
# max_profit = 3
# transactions = [buy, sell, cooldown, buy, sell]
def stock_with_cooldown(prices):
    length = len(prices)
    if length <= 1:
        return 0
    price_min = prices[0]
    profits = [0] * length
    for index, item in enumerate(prices):
        if item < price_min:
            price_min = item
        profits[index] = item - price_min
    return max(profits) - max(profits)


print('\n#309. Best Time to Buy and Sell Stock with Cooldown:')
test_stock_with_cooldown = [1, 2, 3, 0, 2]
print(stock_with_cooldown(test_stock_with_cooldown))
print('NOT done')


# 312. Burst Balloons
# n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
# You are asked to burst all the balloons. Balloon i gives you nums[left] * nums[i] * nums[right] coins.
# Return the max coins.
# nums[-1] = nums[n] = 1. They are not real, so you can not burst them.
# 0 <= n <= 500, 0 <= nums[i] <= 100
# nums = [3, 1, 5, 8]
# Return 167
def burst_balloons(balloons):
    balloons = balloons[::]
    balloons[0] = 0
    return balloons[0]


print('\n#312. Burst Balloons:')
test_burst_balloons = [3, 1, 5, 8]
print(burst_balloons(test_burst_balloons))


# 326. Power of Three
# Return True if n is a power of three
# 1, 3, 9, 27, 81, 243 --> True
# 0, 2, 4, 5, 6, 7, 8, 10 --> False
# Could you do it without using any loop / recursion?
def power_of_three(n):
    if n == 0 or n == 2:
        return False
    if n == 1 or n == 3:
        return True
    while not (n % 3):
        n //= 3
        if n == 3:
            return True
    return False


print('\n#326. Power of Three:')
test_power_of_three = 81
print(power_of_three(test_power_of_three))


# 334. Increasing Triplet Subsequence
# arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1
# [1, 2, 3, 4, 5] --> True
# [5, 4, 3, 2, 1] --> False
def increasing_triplet(nums):
    if not nums:
        return False
    length = len(nums)
    if length <= 2:
        return False
    low = 0
    high = length - 1
    for i in range(length):
        if nums[i] <= nums[low]:
            low = i
        else:
            break
    for j in range(length - 1, -1, -1):
        if nums[j] >= nums[high]:
            high = j
        else:
            break
    if low >= high:
        return False
    for k in range(low + 1, high):
        if nums[low] <= nums[k] <= nums[high]:
            return True
    return False


# increasing_triplet_nums = [0, 1, 2, 3, 4]
# increasing_triplet_nums = [1, 5, 0, 3]
# increasing_triplet_nums = [5, 4, 5, 2, 1]
increasing_triplet_nums = [1, 2, -10, -8, -7]
print('\n#334. Increasing Triplet Subsequence:')
print(increasing_triplet(increasing_triplet_nums))
print('not done')


# 338. Counting Bits
# num = 0 or 1 or 2 or 3 or ...
# For every numbers i in the range 0<=i<=num,
# Calculate the number of 1's in their binary representation and return them as an array
# Example num = 5, you should return [0, 1, 1, 2, 1, 2]
# O(n) in both time and space complexity
def count_bit(bit_num):
    result = list()
    result.append(bit_num)
    return result


print('\n#338. Counting Bits:')
test_count_bit = 0
print(count_bit(test_count_bit))


# 342. Power of Four
def is_power_of_four(num):
    if num == 1 or num == 4:
        return True
    if num in [0, 2, 3]:
        return False
    while not (num % 4):
        num //= 4
        if num == 4:
            return True
    return False


print('\n#342. Power of Four:')
test_if_power_of_four = 16
print(is_power_of_four(test_if_power_of_four))


# 343. Integer Break
# 2 <= n <= 58, break n into the sum of AT LEAST two positive integers and return the max product of those integers.
# n = 2, return 1 (2 = 1 + 1)
# n = 10, return 36 (10 = 3 + 3 + 4)
def break_integer(breakint):
    if breakint <= 3:
        return breakint - 1
    stores = [0] * (breakint + 1)
    stores[2] = 2
    stores[3] = 3
    for index in range(4, breakint + 1):
        stores[index] = max(3 * stores[index - 3], 2 * stores[index - 2])
    return stores[breakint]


print('\n#343. Integer Break:')
test_break = 10
print(break_integer(test_break))


# 344. Reverse String:
def reverse_string(normal_string):
    return normal_string[::-1]


print('\n#344. Reverse String:')
test_reverse = 'hello'
print(reverse_string(test_reverse))


# 345. Reverse Vowels of a String
# Case Sensitive, wth
def reverse_vowels(s):
    all_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    stores = [None] * len(s)
    for index, item in enumerate(s):
        if item in all_vowels:
            stores[index] = item
    vowels = list()
    for letter in stores:
        if letter:
            vowels.append(letter)
    result = StringIO()
    for letter in s:
        if letter in all_vowels:
            result.write(vowels.pop())
        else:
            result.write(letter)
    return result.getvalue()


print('\n#345. Reverse Vowels of a String:')
test_reverse_vowels = 'leetcode'
print(reverse_vowels(test_reverse_vowels))


# 349. Intersection of two arrays:
# two arrays, get the third array containing the intersections
# Element in the result must be unique
# Result can be in any order
def get_intersection(inter_one, inter_two):
    inter_one_set = set(inter_one)
    inter_two_set = set(inter_two)
    inter_one_unique = list(inter_one_set)
    inter_two_unique = list(inter_two_set)
    inter_result = list()
    for value_one in inter_one_unique:
        for value_two in inter_two_unique:
            if value_one == value_two:
                inter_result.append(value_one)
                break
    return inter_result


print('\n#349. Intersection of two arrays:')
test_inter_one = [1, 2, 2, 1]
test_inter_two = [2, 2]
print(get_intersection(test_inter_one, test_inter_two))


# 350. Intersection of Two Arrays II
# Return an array of common integers
def get_intersection_2(nums1, nums2):
    dict_one = {}
    for item in nums1:
        if item in dict_one:
            dict_one[item] += 1
        else:
            dict_one[item] = 1
    dict_two = {}
    for item in nums2:
        if item in dict_two:
            dict_two[item] += 1
        else:
            dict_two[item] = 1
    stores = list()
    for key, value in dict_one.items():
        if key in dict_two:
            if value <= dict_two[key]:
                stores.extend([key] * value)
            else:
                stores.extend([key] * dict_two[key])
    return stores


print('\n#350. Intersection of Two Arrays II:')
test_inter_2_one = [1, 2, 2, 1, 2]
test_inter_2_two = [2, 2]
print(get_intersection_2(test_inter_2_one, test_inter_2_two))


# 357. Count Numbers with Unique Digits
# A non-negative integer, count all numbers with unique digits, x, where 0<=x<10^n
# n = 2, return 91 (0<=x<100, total number is 100 - [11, 22, 33, 44, 55, 66, 77, 88, 99])
def count_numbers_with_unique_digits(power):
    stores = [0] * 11
    stores[1] = 10
    stores[2] = 81
    for index in range(3, 11):
        stores[index] = stores[index - 1] * (11 - index)
    results = [0] * 11
    results[1] = 10
    for index in range(2, 11):
        results[index] = results[index - 1] + stores[index]
    if power > 10:
        return results[10]
    return results[power]


def count_numbers_with_unique_digits_to_pass_leetcode(power):
    stores = [0] * 11
    stores[1] = 10
    stores[2] = 81
    for index in range(3, 11):
        stores[index] = stores[index - 1] * (11 - index)
    results = [0] * 11
    results[0] = 1
    results[1] = 10
    for index in range(2, 11):
        results[index] = results[index - 1] + stores[index]
    if power > 10:
        return results[10]
    return results[power]


print('\n#357. Count Numbers with Unique Digits:')
test_count_numbers_with_unique_digits = 2
print(count_numbers_with_unique_digits(test_count_numbers_with_unique_digits))
print(count_numbers_with_unique_digits_to_pass_leetcode(test_count_numbers_with_unique_digits))


# 368. Largest Divisible Subset
# A set of distinct positive integers, find the largest subset such that every pair a % b = 0
# Return the largest array
# lds goes from small to large, this may cause some wrong answer
# lds_1 goes from large to small, same problem
# lds_2 wth
def lds(nums):
    length = len(nums)
    if length == 0:
        return []
    nums.sort()
    stores = {}
    for outer in range(length):
        temp = [nums[outer]]
        divisor = nums[outer]
        for item in nums[outer + 1:]:
            if item % divisor == 0:
                divisor = item
                temp.append(item)
        stores[len(temp)] = temp
    return stores[max(stores)]


def lds_1(nums):
    length = len(nums)
    if length == 0:
        return []
    nums.sort(reverse=True)
    stores = {}
    for outer in range(length):
        temp = [nums[outer]]
        dividend = nums[outer]
        for item in nums[outer + 1:]:
            if dividend % item == 0:
                dividend = item
                temp.append(item)
        temp.reverse()
        stores[len(temp)] = temp
    return stores[max(stores)]


def lds_2(nums):
    nums = sorted(nums)
    size = len(nums)
    dp = [1] * size
    pre = [None] * size
    for x in range(size):
        for y in range(x):
            if nums[x] % nums[y] == 0 and dp[y] + 1 > dp[x]:
                dp[x] = dp[y] + 1
                pre[x] = y
    idx = dp.index(max(dp))
    ans = []
    while idx is not None:
        ans += nums[idx],
        idx = pre[idx]
    return ans


def lds_3(nums):
    my_set = {-1: set()}
    for x in sorted(nums):
        my_set[x] = max((my_set[d] for d in my_set if x % d == 0), key=len) | {x}
    return list(max(my_set.values(), key=len))


def lds_4(nums):
    if not nums:
        return []
    nums.sort()
    n = len(nums)
    dp, index = [1] * n, [-1] * n
    max_dp, max_index = 1, 0
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                index[i] = j

        if max_dp < dp[i]:
            max_dp, max_index = dp[i], i

    print(dp)
    print(index)
    print(max_index)
    ans = []
    while max_index != -1:
        ans.append(nums[max_index])
        max_index = index[max_index]
    # ans.reverse()
    return ans


print('\n#368. Largest Divisible Subset:')
# test_lds = [1, 2, 3, 4, 5, 6, 7, 8]
# test_lds = [2, 1]
test_lds = [1, 2, 4, 8, 9, 72]
# test_lds = [1, 3, 9, 18, 90, 180, 360, 720]
# print(lds(test_lds))
# print(lds_1(test_lds))
# print(lds_2(test_lds))
# print(lds_3(test_lds))
print(lds_4(test_lds))
print('NOT Done. Don\'t know how to do it...')


# 371. Sum of Two Integers:
# Calculate the sum of two integers a and b,
# but you are NOT allowed to use the operator + and -
def add_two_integer_without_plus_minus(a, b):
    """
    circuit full-adder
    since Python don't restrict to 32bit, we need
    1. Masking
    2. Overflow handling
    :param a: int
    :param b: int
    :return: int
    """
    max_int = 0x7FFFFFFF
    min_int = 0x80000000
    mask = 0x100000000
    while b:
        a, b = (a ^ b) % mask, ((a & b) << 1) % mask
    if a <= max_int:
        return a
    else:
        return ~((a % min_int) ^ max_int)


print('\n#371. Sum of Two Integers:')
a_371 = -12
b_371 = -8
print(add_two_integer_without_plus_minus(a_371, b_371))


# 374. Guess Number Higher or Lower
def guess_number(n):
    # l, r = 1, n
    # while l <= r:
    #     mid = l + ((r - l) >> 1)
    #     res = guess(mid)
    #     if res == 0:
    #         return mid
    #     elif res == 1:
    #         l = mid + 1
    #     else:
    #         r = mid - 1
    # return l
    return n + 374 - n


print('\n#374. Guess Number Higher or Lower:')
test_guess_number_n = 10
print(guess_number(test_guess_number_n))
print('NOT done')


# 378. Kth Smallest Element in a Sorted Matrix
# n x n matrix, rows and columns are sorted in ascending order
# Find the kth smallest element in the matrix
# It is the kth smallest element in the sorted order, not the kth distinct element
# 1 <= k <= n^2
def kth_smallest(matrix, k):
    length = len(matrix)
    positions = [0] * length
    result = matrix[0][0]
    if k == 1:
        return result
    count = 1
    print('NOT DONE')
    return positions * count


kth_smallest_matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
kth_smallest_k = 8
print('\n#378. Kth Smallest Element in a Sorted Matrix:')
print(kth_smallest(kth_smallest_matrix, kth_smallest_k))


# 383. Ransom Note
# Use magazine to construct ransom_note
# Each letter in the magazine can only be used once in your ransom note
# All lowercase letters
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
def can_construct(ransom_note, magazine):
    stores = dict()
    for i in range(97, 123):
        stores[chr(i)] = 0
    for letter in magazine:
        stores[letter] += 1
    for letter in ransom_note:
        stores[letter] -= 1
    if min(stores.values()) < 0:
        return False
    else:
        return True


print('\n#383. Ransom Note:')
can_construct_ransom_note = 'aa'
can_construct_magazine = 'aab'
print(can_construct(can_construct_ransom_note, can_construct_magazine))


# 387. First Unique Character in a String
# Find the first non-repeating character and return the index
# If it doesn't exist, return -1
# s = "leetcode" return 0
# s = "loveleetcode",return 2
# s = "haha",return -1
# All lowercase
def first_uniq_char(s):
    stores = dict()
    for i in range(97, 123):
        stores[chr(i)] = 0
    for letter in s:
        stores[letter] += 1
    for j in range(len(s)):
        if stores[s[j: j + 1]] == 1:
            return j
    return -1


print('\n#387. First Unique Character in a String:')
# first_uniq_char_s = 'leetcode'
first_uniq_char_s = 'loveleetcode'
# first_uniq_char_s = 'haha'
print(first_uniq_char(first_uniq_char_s))


# 389. Find the Difference
# Strings s and t contain only lowercase letters
# t is random shuffling s then add one more letter at a random position
# Find the add letter in t
def find_the_difference(s, t):
    stores = dict()
    for i in range(97, 123):
        stores[chr(i)] = 0
    for letter in s:
        stores[letter] += 1
    for letter in t:
        stores[letter] -= 1
    add_on_letter = min(stores, key=stores.get)
    return add_on_letter


print('\n#389. Find the Difference:')
find_the_difference_s = 'abcd'
find_the_difference_t = 'abcde'
print(find_the_difference(find_the_difference_s, find_the_difference_t))


# 400. Nth Digit
# Find the Nth digit of 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# 1 --> 1
# 3 --> 3
# 9 --> 9
# 10 --> 1
# 11 --> 0
# n < 2 ** 31
def find_nth_digit(n):
    last_nums = [0] * 10
    for i in range(1, 10):
        last_nums[i] = pow(10, i) - 1
    quantities_for_digit = [0] * 10
    for j in range(1, 10):
        quantities_for_digit[j] = (last_nums[j] - last_nums[j - 1]) * j
    total_quantities = [0] * 10
    for k in range(1, 10):
        total_quantities[k] = total_quantities[k - 1] + quantities_for_digit[k]

    # stores = [0] * 10
    # for i in range(1, 10):
    #     stores[i] = 9 * pow(10, (i - 1)) * i

    digit_number = get_digit_number(total_quantities, n)
    if digit_number == 1:
        return n
    if digit_number == 2:
        if n % 2 == 0:
            return ((n - total_quantities[digit_number - 1]) // 20) + 1
        else:
            remainder = (n - total_quantities[digit_number - 1]) % 20
            if remainder == 0:
                return 9
            else:
                return (remainder - 2) // 2
    if digit_number == 3:
        return 374


def get_digit_number(stores, m):
    for j in range(1, 10):
        if m <= stores[j]:
            return j


print('\n#400. Nth Digit:')
# print(get_digit_number(181))
print(find_nth_digit(2890))
print('NOT DONE')


# 401. Binary Watch
# Given a non-negative integer n which represents the number of LEDs that are currently on.
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Order does not matter
# '01:00' should be '1:00'
# '10:2' should be '10:02'
def read_binary_watch(num):
    hour_stores = ['0'] * 4
    hour_stores[0] = ['0']
    hour_stores[1] = ['1', '2', '4', '8']
    hour_stores[2] = ['3', '5', '6', '9', '10']
    hour_stores[3] = ['7', '11']
    minute_stores = ['00'] * 6
    minute_stores[0] = ['00']
    minute_stores[1] = ['01', '02', '04', '08', '16', '32']
    minute_stores[2] = ['03', '05', '09', '17', '33', '06', '10', '18', '34', '12', '20', '36', '24', '40', '48']
    minute_stores[4] = ['58', '54', '46', '30', '57', '53', '45', '29', '51', '43', '27', '39', '23', '15']
    minute_stores[3] = ['07', '11', '19', '35', '13', '21', '37', '25', '41', '49', '14', '22', '38', '26', '42', '50',
                        '28', '44', '52', '56']
    minute_stores[5] = ['31', '47', '55', '59']
    stores = list()
    for i in range(min(4, num + 1)):
        for hour in hour_stores[i]:
            if (num - i) <= 5:
                for minute in minute_stores[num - i]:
                    stores.append(hour + ':' + minute)
    return stores


print('\n#401. Binary Watch:')
read_binary_watch_num = 1
print(read_binary_watch(read_binary_watch_num))

# 404. Sum of Left Leaves
# Find the sum of all left leaves in a given binary tree

print('\n#404. Sum of Left Leaves:')
print('done on leetcode')


# 407. Trapping Rain Water II
def trap_rain_water_2d(height_map):
    if not height_map:
        return 0
    row_len = len(height_map)
    if row_len <= 2:
        return 0
    # row_len >= 3
    col_len = len(height_map[0])
    if col_len <= 2:
        return 0
    # col_len >= 3
    result = 0
    row_max = [0] * row_len
    col_max = [0] * col_len

    for i in range(row_len):
        row_max[i] = get_list_max_index(height_map[i])

    for j in range(col_len):
        temp = list()
        for k in range(row_len):
            temp.append(height_map[k][j])
        col_max[j] = get_list_max_index(temp)

    for row in range(1, row_len - 1):
        left_max = height_map[row][0]
        right_max = height_map[row][-1]
        for index in range(1, col_len - 1):
            row_value = 0
            if index == row_max[row]:
                pass
            elif index < row_max[row]:
                for left in range(index):
                    if height_map[row][left] > left_max:
                        left_max = height_map[row][left]
                row_value = left_max
            else:  # index > row_max[row]
                for right in range(col_len - 1, index, -1):
                    if height_map[row][right] > right_max:
                        right_max = height_map[row][right]
                row_value = right_max
            if row_value == 0:
                pass
            else:
                if col_max[index] == row:
                    pass
                elif col_max[index] > row:
                    max_up = height_map[0][index]
                    for m in range(row):
                        if height_map[m][index] > max_up:
                            max_up = height_map[m][index]
                    result += max((min(max_up, row_value) - height_map[row][index]), 0)
                else:  # col_max[index] < row
                    max_down = height_map[-1][index]
                    for n in range(row_len - 1, row, -1):
                        if height_map[n][index] > max_down:
                            max_down = height_map[n][index]
                    result += max((min(max_down, row_value) - height_map[row][index]), 0)
    return result


def get_list_max_index(nums):
    max_value = nums[0]
    max_index = 0
    for i in range(len(nums)):
        if nums[i] > max_value:
            max_value = nums[i]
            max_index = i
    return max_index


# trap_rain_water_2d_height_map = [
#     [1, 4, 3, 1, 3, 2],
#     [3, 2, 1, 3, 2, 4],
#     [2, 3, 3, 2, 3, 1]
# ]

# trap_rain_water_2d_height_map = [
#     [1, 3, 3, 1, 3, 2],
#     [3, 2, 1, 3, 2, 3],
#     [3, 3, 3, 2, 3, 1]
# ]

trap_rain_water_2d_height_map = [
    [12, 13, 1, 12],
    [13, 4, 13, 12],
    [13, 8, 10, 12],
    [12, 13, 12, 12],
    [13, 13, 13, 13]
]

print('\n#407. Trapping Rain Water II:')
print(trap_rain_water_2d(trap_rain_water_2d_height_map))


# 409. Longest Palindrome
# A string contains lowercase or uppercase
# Build a longest palindrome
# Case sensitive, Aa is not palindrome
# 'abccccdd' --> 'dccaccd' --> 7
def build_longest_palindrome(s):
    s = s.replace(' ', '')
    length = len(s)
    answer = 0
    stores = dict()
    for letter in s:
        if letter in stores:
            stores[letter] += 1
        else:
            stores[letter] = 1
    for value in stores.values():
        answer += (2 * (value // 2))
    if answer != length:
        answer += 1
    return answer


print('\n#409. Longest Palindrome:')
build_longest_palindrome_s = 'abccccdd'
# build_longest_palindrome_s = 'abccccddab'
print(build_longest_palindrome(build_longest_palindrome_s))


# 412. Fizz Buzz
# from 1 to n
# 3 --> 'Fizz'
# 5 --> 'Buzz'
# 3 and 5 --> 'FizzBuzz'
def fizz_buzz(number):
    result = list()
    for i in range(1, number + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))
    return result


print('\n#412. Fizz Buzz:')
print(fizz_buzz(15))


# 415. Add Strings
# Two non-negative numbers num1 and num2 represented as string
# Return the sum of num1 and num2
# Length < 5100
# Contains only digits 0 to 9
# No leading zero
# Build-in convert is not allowed
def add_strings(num1, num2):
    stores = dict()
    for i in range(10):
        stores[str(i)] = i
    val_1 = 0
    val_2 = 0
    len_1 = len(num1)
    len_2 = len(num2)
    for j in range(len_1):
        val_1 += (stores[num1[j:j + 1]]) * pow(10, len_1 - 1 - j)
    for k in range(len_2):
        val_2 += (stores[num2[k:k + 1]]) * pow(10, len_2 - 1 - k)
    return str(val_1 + val_2)


print('\n#415. Add Strings:')
add_strings_num1 = '0'
add_strings_num2 = '9'
print(add_strings(add_strings_num1, add_strings_num2))


# 438. Find All Anagrams in a String
# Input: s: 'abab' p: 'ab'
# Output:[0, 1, 2]
def find_anagrams(s, p):
    # This is too slow, need optimization
    if not s:
        return []
    s_len = len(s)
    p_len = len(p)
    if s_len < p_len:
        return []
    result = list()
    for i in range(s_len - p_len + 1):
        if is_anagram_lowercase(s[i:i + p_len], p):
            result.append(i)
    return result


def is_anagram(a, b):
    stores = dict()
    for item in a:
        if item in stores:
            stores[item] += 1
        else:
            stores[item] = 1
    for letter in b:
        if letter not in stores:
            return False
        else:
            stores[letter] -= 1
    for key, value in stores.items():
        if value != 0:
            return False
    return True


# Submission Result: Time Limit Exceeded
def find_anagrams_sort_first(s, p):
    if s is None or p is None:
        return []
    s_len = len(s)
    p_len = len(p)
    if s_len < p_len:
        return []
    target = ''.join(sorted(p))
    result = []
    for i in range(s_len - p_len + 1):
        word = s[i:i + p_len]
        sorted_word = ''.join(sorted(word))
        if sorted_word == target:
            result.append(i)
    return result


# Accepted, 96.31% and bug free, awesome!!!
def find_anagrams_dict(s, p):
    if s is None or p is None:
        return []
    s_len = len(s)
    p_len = len(p)
    if s_len < p_len:
        return []
    if s_len == p_len:
        if ''.join(sorted(s)) == ''.join(sorted(p)):
            return [0]
        else:
            return []
    target = {}
    for letter in p:
        if letter in target:
            target[letter] += 1
        else:
            target[letter] = 1
    result = []
    current = {}
    for i in range(p_len):
        if s[i] in current:
            current[s[i]] += 1
        else:
            current[s[i]] = 1
    if current == target:
        result.append(0)
    for j in range(1, s_len - p_len + 1):
        new_char = s[p_len + j - 1]
        if new_char in current:
            current[new_char] += 1
        else:
            current[new_char] = 1
        remove_char = s[j - 1]
        current[remove_char] -= 1
        if current[remove_char] == 0:
            del current[remove_char]
        if current == target:
            result.append(j)
    return result


find_anagrams_s = 'abab'
find_anagrams_p = 'ab'
print('\n#438. Find All Anagrams in a String:')
print(find_anagrams(find_anagrams_s, find_anagrams_p))
print(find_anagrams_sort_first(find_anagrams_s, find_anagrams_p))
print(find_anagrams_dict(find_anagrams_s, find_anagrams_p))


# 448. Find all numbers disappeared in an array
# 1 =< a[i] <= n (n = size of array)
# some appear twice and others appear once
# find not appear elements
# constant space, O(n) time
# [4,3,2,7,8,2,3,1]
# return [5, 6]
def find_disappeared_numbers(nums):
    return 'NOT DONE' + str(nums[0])


find_disappeared_numbers_nums = [4, 3, 2, 7, 8, 2, 3, 1]
print('\n#448. Find all numbers disappeared in an array:')
print(find_disappeared_numbers(find_disappeared_numbers_nums))


# 461. Hamming Distance
# The number of positions at which the corresponding bits are different
# 0 =< x, y <= 2^31
# x = 1, y = 4
# 1 (0 0 0 1)
# 4 (0 1 0 0)
# return 2
def hamming_distance(x, y):
    bin_x = bin(x)
    bin_y = bin(y)
    print(bin_x)
    print(bin_y)
    return 'Not Done'


hamming_distance_x = 1
hamming_distance_y = 4
print('\n#461. Hamming Distance:')
print(hamming_distance(hamming_distance_x, hamming_distance_y))
