n = input("整数を入力してください")
numbers =range(1,int(n)+1)
total =sum(numbers)
average=total/len(numbers)
print (f"1~{n}までの合計: {total}")
print(f"平均:{average}")

# total = 0
# average = 0
# num = int(n)
# i = 0
# while i <= num:
#     total += i
#     i += 1
# average = total /num