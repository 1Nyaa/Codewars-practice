
# A staircase is given with a non-negative cost per each step. Once you pay the cost,
# you can either climb one or two steps.
# Create a solution to find the minimum sum of costs to reach the top.
# You can start at either of the first two steps.

def climbing_stairs(cost):
    n = len(cost)
    answ = [0] * (n + 1)

    for i in range(2, n + 1):
        answ[i] = min(answ[i - 1] + cost[i - 1], answ[i - 2] + cost[i - 2])

    return answ[n]
