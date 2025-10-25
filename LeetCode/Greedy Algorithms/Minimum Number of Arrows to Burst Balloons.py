def findMinArrowShots(points):
    points.sort(key=lambda x: x[1])

    arrows = 1
    current_end = points[0][1]

    for start, end in points[1:]:
        if start > current_end:
            arrows += 1
            current_end = end

    return arrows

points1 = [[10,16],[2,8],[1,6],[7,12]]
print(findMinArrowShots(points1))  # Output: 2
points2 = [[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points2))  # Output: 4
points3 = [[1,2],[2,3],[3,4],[4,5]]
print(findMinArrowShots(points3))  # Output: 2
