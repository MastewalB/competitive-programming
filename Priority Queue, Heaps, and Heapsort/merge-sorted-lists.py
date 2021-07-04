from MinHeap import MinHeap

#lists = [[1, 4, 5], [1, 3, 4], [2, 6, 7]]
lists = [[1, 2, 4, 5, 6, 7], [2, 3]]
new_list = []
total_len = 0
max_len = 0
for i in lists:
    if len(i) > max_len:
        max_len = len(i)
    total_len += len(i)


heap = MinHeap(max_len)

i = 0
count = 0
while i < max_len:
    j = 0
    while j < len(lists):

        if i < len(lists[j]) and count < max_len:
            print(j, i)
            heap.insert(lists[j][i])
            count += 1
        elif i < len(lists[j]) and count == max_len:
            min_item = heap.remove()
            new_list.append(min_item)
            count -= 1
            print("Min ", min_item)
            heap.insert(lists[j][i])
            count += 1
        j += 1
    i += 1
heap.Print()
if heap.size != 0:
    while heap.size != 0:
        # heap.Print()
        min_item = heap.remove()
        count -= 1
        new_list.append(min_item)
        print("Min ", min_item)

print(new_list)
