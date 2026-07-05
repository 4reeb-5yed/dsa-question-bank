def find_min_arrows(balloons):
    if not balloons:
        return 0
    balloons.sort(key=lambda x: x[1])
    arrows = 1
    end = balloons[0][1]
    for i in range(1, len(balloons)):
        if balloons[i][0] > end:
            arrows += 1
            end = balloons[i][1]
    return arrows