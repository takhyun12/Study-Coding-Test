def check_match(lock, key):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] + key[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key[0])
    n = len(lock[0])

    new_key_0 = [[0] * n for _ in range(n)]
    new_key_1 = [[0] * n for _ in range(n)]
    new_key_2 = [[0] * n for _ in range(n)]
    new_key_3 = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            new_key_0[i][j] = key[i][j]
            new_key_1[j][m-i-1] = key[i][j]
            new_key_2[m-i-1][m-j-1] = key[i][j]
            new_key_3[m-j-1][i] = key[i][j]

    for key in [new_key_0, new_key_1, new_key_2, new_key_3]:
        for i in range(n):
            for j in range(n):
                left_up_key = [row[i:] + [0]*i for row in key[j:]] + [[0]*n]*j
                if check_match(lock, left_up_key):
                    return True
                left_down_key = [[0]*n]*(n-j-1) + [row[i:] + [0]*i for row in key[:j+1]]
                if check_match(lock, left_down_key):
                    return True
                right_up_key = [[0]*i + row[:n-i] for row in key[j:]] + [[0]*n]*j
                if check_match(lock, right_up_key):
                    return True
                right_down_key = [[0]*n]*(n-j-1) + [[0]*i + row[:n-i] for row in key[:j+1]]
                if check_match(lock, right_down_key):
                    return True
    return False