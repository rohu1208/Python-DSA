# Store frequency
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(lst)

freq = {}
# for i in range(0, n): # O(n)
#     if lst[i] in freq: #O(1)
#         freq[lst[i]] += 1 #O(1)
#     else:
#         freq[lst[i]] = 1  # if not exist add
# print(freq)

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print(freq)
