def minMeetingRooms(intervals):
    if not intervals:
        return 0

    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    s_ptr = e_ptr = 0
    rooms = 0
    max_rooms = 0

    while s_ptr < len(intervals):
        if starts[s_ptr] < ends[e_ptr]:
            rooms += 1
            s_ptr += 1
        else:
            rooms -= 1
            e_ptr += 1
        max_rooms = max(max_rooms, rooms)

    return max_rooms

intervals = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(intervals))  # Output: 2

intervals2 = [[7,10],[2,4]]
print(minMeetingRooms(intervals2))  # Output: 1
