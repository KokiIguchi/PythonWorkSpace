import math

input_angle = float(input("角度を入力して下さい(°):"))
angle = input_angle * math.pi /180
print(f'{input_angle}° -> {angle}ラジアン')
print(f'sin({input_angle}) => {math.sin(angle)}')

#度からラジアンにする別の方法
#print(math.radians(input_angle))
#逆(ラジアンから度)
#print(math.degrees(angle))