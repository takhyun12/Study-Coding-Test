dx = -1, 0, 1, -1, 0, 1, -1, 0, 1
dy = -1, -1, -1, 0, 0, 0, 1, 1, 1

def check_beam(board, x, y):
    return board[x][y-1][0] or board[x+1][y-1][0] or (board[x-1][y][1] and board[x+1][y][1])

def check_col(board, x, y):
    return y == 0 or board[x][y-1][0] or board[x][y][1] or board[x-1][y][1]

def solution(n, build_frame):
    board = [[[0, 0] for _ in range(n+2)] for _ in range(n+2)]
    for x, y, a, b in build_frame:
        if a:
            if b:
                if check_beam(board, x, y):
                    board[x][y][1] = 1
            else:
                board[x][y][1] = 0
                for d in range(9):
                    nx, ny = x + dx[d], y + dy[d]
                    if nx >= 0 and ny >= 0:
                        if board[nx][ny][0] == 1:
                            if not check_col(board, nx, ny):
                                board[x][y][1] = 1
                                break
                        if board[nx][ny][1] == 1:
                            if not check_beam(board, nx, ny):
                                board[x][y][1] = 1
                                break
        else:
            if b:
                if check_col(board, x, y):
                    board[x][y][0] = 1
            else:
                board[x][y][0] = 0
                for d in range(9):
                    nx, ny = x + dx[d], y + dy[d]
                    if nx >= 0 and ny >= 0:
                        if board[nx][ny][0] == 1:
                            if not check_col(board, nx, ny):
                                board[x][y][0] = 1
                                break
                        if board[nx][ny][1] == 1:
                            if not check_beam(board, nx, ny):
                                board[x][y][0] = 1
                                break
    answer = []
    for x in range(n+2):
        for y in range(n+2):
            if board[x][y][0]:
                answer.append([x, y, 0])
            if board[x][y][1]:
                answer.append([x, y, 1])
    answer.sort()
    return answer