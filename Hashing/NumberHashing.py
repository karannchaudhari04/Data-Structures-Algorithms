#Number hashing using List

n = [1,2,1,4,2,3,4,5,6,1,7,8,]
m = [1,2,3,4,10,9,7]

hash_list = [0] * 11

for num in n:
    hash_list[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])


#Number hashing using dictionary

x = [1,2,1,4,2,3,4,5,6,1,7,8,]
y = [1,2,3,4,10,9,7]

hash_dict = {}

for num in x:
    if num in hash_dict:
        hash_dict[num] += 1
    else:
        hash_dict[num] = 1

for num in y:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_dict.get(num, 0))