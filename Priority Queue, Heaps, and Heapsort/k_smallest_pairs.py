from List_Heap import List_Heap

nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3


def k_smallest_pairs(nums1, nums2, k):
    list_heap = List_Heap(k)

    i = 0
    j = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            s = nums1[i] + nums2[j]
            element = [s, [nums1[i], nums2[j]]]

            if list_heap.size >= k:
                if list_heap.Heap[list_heap.size][0] > element[0]:
                    list_heap.subsert(element)
            else:
                list_heap.insert(element)
    return list_heap


k_smallest_pairs(nums1, nums2, k).Print()
