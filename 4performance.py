def intersect (bagA, bagB):
    result = []
    for o in bagA:
        if o in bagB:
            result.append(o)
    return result

def intersect_modif (bagA, bagB):
    result = []
    mainBag = bagA if len(bagA) < len(bagB) else bagB
    subBag = bagA if len(bagA) > len(bagB) else bagB
    print(mainBag)
    print(subBag)
    for o in mainBag:
        if o in subBag:
            result.append(o)
    return result


bagA = {1,2,4,56575,232,24,5}
bagB = {43,564,2,4,653,6}

print(intersect(bagA, bagB))
print(intersect_modif(bagA, bagB))
print(bagA.intersection(bagB))
print(min(5,4))


"""
https://stackoverflow.com/questions/38559245/how-to-speed-up-4-million-set-intersections
The intersection() method performs well in terms of time complexity,
 as it has an average time complexity of O(min(len(set1), len(set2))).
 This means that the time it takes to find the intersection is
 proportional to the size of the smaller set.
"""