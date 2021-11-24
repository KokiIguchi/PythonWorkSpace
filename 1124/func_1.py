def combine_list(list1,list2):
    if type(list1) is list and typs (list2) is list:
        list3 = []
        for i in list1:
            list3.append(i)
        for i in list2:
            list3.append(i)
        return list3
    else:
        print("引数がリストではありません")
        return[list1,list2]