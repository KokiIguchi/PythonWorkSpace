import time
sheep_num = 0
time_sleep=0
sheep = int(input("何匹数えますか？:"))
if sheep < 100:
    while   sheep_num <sheep :
        print('羊が{}匹'.format(sheep_num+1))
        sheep_num += 1
        time.sleep(time_sleep)
        time_sleep += 1
else:
    print('数が多すぎます。')
print('～おわり～')

#解答例
while True:
    max_num =int(input("何匹数えますか？:"))
    if max_num < 100:
        print ("数が多すぎます")
        continue
    else:
        break
my_count = 1
while my_count < max_num:
    print('羊が{}匹'.format(my_count))
    time_sleep(my_count/10)
    my_count += 1
#↑こっちの方がかっこいい書き方