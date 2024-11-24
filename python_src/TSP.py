def calculate(destinations: list[list[float]]) -> tuple[list[int], float]:

    n = len(destinations)
    if n <= 1:
        return ([0], 0)

    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0 

    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):  
                continue
            for j in range(n):
                if mask & (1 << j):  
                    continue
                dp[mask | (1 << j)][j] = min(
                    dp[mask | (1 << j)][j],
                    dp[mask][i] + destinations[i][j]
                )

    final_mask = (1 << n) - 1 
    min_cost = float('inf')
    last_node = -1
    for i in range(1, n):  
        cost = dp[final_mask][i] + destinations[i][0]
        if cost < min_cost:
            min_cost = cost
            last_node = i

    path = [0]  
    mask = final_mask
    current_node = last_node
    while current_node != 0:
        path.append(current_node)
        for i in range(n):
            if mask & (1 << i) and dp[mask][current_node] == dp[mask ^ (1 << current_node)][i] + destinations[i][current_node]:
                mask ^= (1 << current_node)
                current_node = i
                break
    path.append(0)

    return path[::-1], min_cost 

