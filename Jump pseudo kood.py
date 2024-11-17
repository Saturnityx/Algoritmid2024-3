def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Hüppefaas
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Lineaarne otsing
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i

    return -1