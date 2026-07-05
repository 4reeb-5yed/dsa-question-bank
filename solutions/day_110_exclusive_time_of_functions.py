def exclusive_time(n, logs):
    result = [0] * n
    stack = []
    prev_time = 0
    for log in logs:
        fid, is_start, time = log.split(':')
        fid, time = int(fid), int(time)
        is_start = is_start == 'start'
        if not stack:
            stack.append((fid, time))
            prev_time = time
        elif is_start:
            result[stack[-1][0]] += time - prev_time
            stack.append((fid, time))
            prev_time = time
        else:
            result[fid] += time - prev_time + 1
            stack.pop()
            if stack:
                prev_time = time + 1
    return result