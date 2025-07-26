import itertools

# Generate all unique combinations of 4 ones and 4 zeros
combinations = set(itertools.permutations([1, 1, 1, 1, 0, 0, 0, 0]))
unique_combinations = [list(x) for x in combinations]

# Test pairs to check for two 1s
strategy1 = [(0, 1), (2, 3), (4, 5), (6, 7), (0, 2), (0, 3), (1, 2), (1, 3)]
strategy2 = [(0, 1), (1, 2), (2, 3), (0, 3), (0, 2), (1, 3), (4, 5), (6, 7)]
strategy3 = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (6, 7)]

strategy1highest = 0
strategy2highest = 0
strategy3highest = 0

for arr in unique_combinations:
    strat1tests = 0
    strat2tests = 0
    strat3tests = 0
    strat1found = False
    strat2found = False
    strat3found = False
    for i, j in strategy1:
        strat1tests += 1
        if arr[i] == 1 and arr[j] == 1:
            # print(f"Array: {arr}, strat1tests: {strat1tests}")
            strat1found = True
            if strat1tests > strategy1highest:
                strategy1highest = strat1tests
            break
    for i, j in strategy2:
        strat2tests += 1
        if arr[i] == 1 and arr[j] == 1:
            # print(f"Array: {arr}, strat2tests: {strat2tests}")
            strat2found = True
            if strat2tests > strategy2highest:
                strategy2highest = strat2tests
            break
            found = True
            break
    for i, j in strategy3:
        strat3tests += 1
        if arr[i] == 1 and arr[j] == 1:
            # print(f"Array: {arr}, strat3tests: {strat3tests}")
            strat3found = True
            if strat3tests > strategy3highest:
                strategy3highest = strat3tests
            break
    winner = (
        "Strategy1"
        if strat1tests < strat2tests and strat1tests < strat3tests
        else "Strategy2" if strat2tests < strat3tests else "Strategy3"
    )
    print(
        f"Array: {arr}, Winner: {winner}! {'N/A' if not strat1found else strat1tests}, {'N/A' if not strat2found else strat2tests}, {'N/A' if not strat3found else strat3tests}"
    )
print(
    f"Strategy1: {strategy1highest}, Strategy2: {strategy2highest}, Strategy3: {strategy3highest}"
)
