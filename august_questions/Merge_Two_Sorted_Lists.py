def merge(list1, list2):
    i = 0
    j = 0
    content = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            content.append(list1[i])
            i += 1
        else:
            content.append(list2[j])
            j += 1
    while i < len(list1):
        content.append(list1[i])
        i += 1
    while j < len(list2):
        content.append(list2[j])
        j += 1
    return content
