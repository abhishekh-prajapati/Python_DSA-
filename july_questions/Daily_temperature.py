def daily_temp(degree):

    store = []
    for i in range(len(degree)):
        found = False
        for j in range(i + 1, len(degree)):
            if degree[j] > degree[i]:
                store.append(j - i )
                found = True
                break
        if not found:
            store.append(0)
    return store
temperatures = [30, 40, 20, 50, 60]
print(daily_temp(temperatures))
