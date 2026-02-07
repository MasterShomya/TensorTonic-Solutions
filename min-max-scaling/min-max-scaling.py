def min_max_scaling(data):
    rows = len(data)
    cols = len(data[0])

    mins = [float('inf')] * cols
    maxs = [float('-inf')] * cols

    for r in range(rows):
        for c in range(cols):
            mins[c] = min(mins[c], data[r][c])
            maxs[c] = max(maxs[c], data[r][c])

    scaled = []

    for r in range(rows):
        new_row = []
        for c in range(cols):
            min_val = mins[c]
            max_val = maxs[c]
            range_val = max_val - min_val

            if range_val == 0:
                new_row.append(0.0)
            else:
                new_row.append((data[r][c] - min_val) / range_val)

        scaled.append(new_row)

    return scaled
