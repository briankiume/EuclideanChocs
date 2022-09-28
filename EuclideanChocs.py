def euclideanChocs(n, m):
    chocs = []
    for x in range(0, n, m):
        chocs.append(x)
    new = [chocs[-1]]
    while ((new[-1] + m) % n != 0) | ((new[-1] + m - n) != 0):
        if (new[-1] + m) > n:
            new.append(new[-1] + m - n)
        if (new[-1] + m) < n:
            new.append(new[-1] + m)

    chocs_all = chocs[:-1] + new
    return len(chocs_all)


print(euclideanChocs(10, 4))
