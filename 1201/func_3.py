def do_anything(*para):
    #para 受け取った値は、タプルとなる。タプルとは、順序付けられた複数の要素で構成される組。
    print (f'受け取った値：{para}')

    if len(para) == 0:
        return 'やることが無いので暇です。'
    elif len(para) == 1:
        para2 = para[0]
        #para2, =para ←こっちでも動く
        if type(para2) != int and type(para2) != str:
            print ('難しくて無理です。')
        else:
            print(para2 * 2)
    elif len(para) == 2:
        para1,para2 = para
        if type(para1) == type(para2) != int and type(para1) == type(para2) != str:
            print('無茶言わないで！')
        elif type(para1) != type(para2):
            print('できません～')
        else:
            print(para1 + para2)
    elif len(para) >= 3:
        print('無理です...')

do_anything()
do_anything(10)
do_anything('asdfg')
do_anything([1,2,3])
do_anything(10,20)
do_anything(10,'abc')
do_anything('x','yz')
do_anything([1,2,3],[4,5,6])
do_anything(1,2,3)
