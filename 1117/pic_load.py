import pickle

with open('bignum.pkl' , 'lb')as f:
    big_num = pickle.load(f)

print(big_num)