from collections import defaultdict
from heapq import heappush,heappop

# 갈 수 있는지 체크
def check_go(y1,x1,d,visit,c) :
    dy, dx = [-1, 0, 1, 0], [0, -1, 0, 1]
    if not visit[(y1,x1,d)] and not visit[(y1+dy[d],x1+dx[d],(d+2)%4)] : return True
    elif visit[(y1,x1,d)] > c or visit[(y1+dy[d],x1+dx[d],(d+2)%4)] > c : return True
    else : return False

def solution(board) :
    visit = defaultdict(int)
    N = len(board)
    dy,dx = [-1,0,1,0],[0,-1,0,1]
    pq = [(1, 0, 0, 3)]  # c,y,x,d
    visit[(0,0,3)] = 1
    while pq :
        c,y1,x1,d = heappop(pq)
        y2,x2 = y1+dy[d],x1+dx[d]

        if (y1,x1) == (N-1,N-1) or (y2,x2) == (N-1,N-1) :
            return c-1

        # 상좌하우 이동
        for dr in range(4) :
            if all(0<= k1 < N  and 0<=k2 <N and not board[k1][k2] for k1,k2 in ((y1+dy[dr],x1+dx[dr]),(y2+dy[dr],x2+dx[dr]))) \
                and check_go(y1+dy[dr],x1+dx[dr],d,visit,c+1) :
                visit[(y1+dy[dr],x1+dx[dr],d)] = c+1
                heappush(pq,(c+1,y1+dy[dr],x1+dx[dr],d))

        # 첫번째 축 회전
        for dr in (0,1,2,3) :
            if (d % 2 and dr % 2) or (not d % 2 and not dr % 2): continue
            if all(0 <= k1 < N and 0 <= k2 < N and not board[k1][k2] for k1, k2 in
                   ((y1 + dy[dr], x1 + dx[dr]), (y2 + dy[dr], x2 + dx[dr]))) \
                    and check_go(y1, x1, dr, visit, c + 1):
                visit[(y1, x1, dr)] = c + 1
                heappush(pq, (c + 1, y1, x1, dr))

        # 두번째 축 회전
        for dr in (0, 1, 2, 3):
            if (d % 2 and dr % 2) or (not d % 2 and not dr % 2): continue
            if all(0 <= k1 < N and 0 <= k2 < N and not board[k1][k2] for k1, k2 in
                   ((y1 + dy[dr], x1 + dx[dr]), (y2 + dy[dr], x2 + dx[dr]))) \
                    and check_go(y2, x2, dr, visit, c + 1):
                visit[(y2, x2, dr)] = c + 1
                heappush(pq, (c + 1, y2, x2, dr))