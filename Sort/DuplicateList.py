l = [1,2,3,4,4,4,5,6,7,7]

def findduplicates(list):
    duplicates = []
    for i in range(1, len(list)):
        if list[i] == list[i - 1]:
            if list[i] not in duplicates:
                duplicates.append(list[i])
    return duplicates

print("Duplicates are : ", findduplicates(l))