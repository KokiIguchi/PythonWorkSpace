print("偶数一覧=>",end="")
for i in range(2,99,2):
    print(i,end="")
    print(",",end="")


#解答例2
result =[]
for i in range(1,100):
    if i % 2 ==0:
        result.append(i)
print(f'偶数一覧=>{result}')

#解答例3
print("偶数一覧=>",end="")
for i in range(1,100):
    if i % 2 == 0 :
        print(i,end="")
