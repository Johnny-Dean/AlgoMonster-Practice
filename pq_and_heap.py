import heapq
from typing import List


def heap_top_3(arr: List[int]) -> List[int]:
    heapq.heapify(arr)
    res = []
    for i in range(3):
        res.append(heapq.heappop(arr))
    return res

if __name__ == '__main__':
    print(heap_top_3([3, 1, 2, 10, 33, 100, 20,]))
