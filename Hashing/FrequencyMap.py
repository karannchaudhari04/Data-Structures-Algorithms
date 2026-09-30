nums = [5,1,4,5,1,1,7,4,3,2,7]

freq_map = dict()

for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1

print(freq_map)

#Different method

num = [7,2,2,6,7,5]

hash_map = dict()
for j in range(0, len(num)):
    hash_map[num[j]] = hash_map.get(num[j], 0) +1

print(hash_map)