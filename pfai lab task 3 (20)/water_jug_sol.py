def water_jug_dfs(jug1, jug2, target):
    stack = []
    visited = set()
    stack.append((0, 0, []))

    while stack:
        x, y, path = stack.pop()

        if (x, y) in visited:
            continue
        visited.add((x, y))

        path.append((x, y))

        if x == target or y == target:
            print("Solution Found:")
            step = 1
            for i in range(len(path) - 1):
                action = rule_applied(path[i], path[i + 1])
                print("Step", step, ":", action)
                print("State:", path[i + 1])
                step = step + 1
            return

        next_states = []

        next_states.append((jug1, y))

        next_states.append((x, jug2))
        
        next_states.append((0, y))
        
        next_states.append((x, 0))
        
        transfer = min(x, jug2 - y)
        
        next_states.append((x - transfer, y + transfer))
        
        transfer = min(y, jug1 - x)
        
        next_states.append((x + transfer, y - transfer))

        for state in next_states:
            if state not in visited:
                stack.append((state[0], state[1], path[:]))

    print("No solution found.")


def rule_applied(prev, curr):
    x1, y1 = prev
    x2, y2 = curr

    if x2 > x1 and y2 == y1:
        return "Fill Jug1"
    elif y2 > y1 and x2 == x1:
        return "Fill Jug2"
    elif x2 < x1 and y2 == y1:
        return "Empty Jug1"
    elif y2 < y1 and x2 == x1:
        return "Empty Jug2"
    elif x2 < x1 and y2 > y1:
        return "Pour from Jug1 to Jug2"
    elif y2 < y1 and x2 > x1:
        return "Pour from Jug2 to Jug1"
    else:
        return "No action"


jug1 = int(input("Jug1 Capacity: "))
jug2 = int(input("Jug2 Capacity: "))
target = int(input("Enter amount of water: "))

water_jug_dfs(jug1, jug2, target)
