str1 = "abcdef"
# new_str1 = str1[::-1]
# print(new_str1)

idx = -1
while idx >= -len(str1):
    print(str1[idx])
    idx -=1

#memo
#2**2 = 4
#2**3 = 8

#memo
# i =len(str1)
# rev = list(str1)
# for c in str1:
#     i -= 1
#     rev[i] = c
# print(join(rev))