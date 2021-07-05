from MaxHeap import MaxHeap


def smash(stone_1, stone_2):
    return stone_1 - stone_2 if stone_1 > stone_2 else stone_2 - stone_1


stones = [2, 7, 4, 1, 8, 1]
heap = MaxHeap(len(stones))
for i in stones:
    heap.insert(i)

while heap.size > 1:
    stone_1 = heap.remove()
    stone_2 = heap.remove()

    smashed = smash(stone_1, stone_2)
    if smashed != 0:
        heap.insert(smashed)

if heap.size > 0:
    print(heap.remove())
else:
    print(0)
