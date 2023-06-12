import random
import time

def intersect (bagA, bagB):
    result = []
    for o in bagA:
        if o in bagB:
            result.append(o)
    return result

bagB = random.sample(range(1000000), 100000)
bagA = random.sample(range(1000000), 1000)


start_time = time.time()
intersect_result = intersect(bagA, bagB)
print(intersect_result)
intersect_time = time.time() - start_time


setA = set(bagA)
setB = set(bagB)


start_time = time.time()
set_intersect_result = list(setA.intersection(setB))
print(set_intersect_result)
set_intersect_time = time.time() - start_time


print(f"Time exec for intersect function: {intersect_time} s")
print(f"Time exec for set.intersection: {set_intersect_time} s")

"""
https://stackoverflow.com/questions/38559245/how-to-speed-up-4-million-set-intersections
The intersection() method performs well in terms of time complexity,
 as it has an average time complexity of O(min(len(set1), len(set2))).
 This means that the time it takes to find the intersection is
 proportional to the size of the smaller set.
"""