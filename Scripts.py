
def IsFreeCase(N, Q, Case):
    for q in Q:
        if q[0] == Case[0] or q[1] == Case[1]:
            return False
        for i in range(N):
            if Case in [[q[0]+i, q[1]+i], [q[0]+i, q[1]-i], [q[0]-i, q[1]+i],[q[0]-i, q[1]-i]]:
                return False
    return True

def FreeCases(N, Q):
    F = []
    for i in range(N):
        for j in range(N):
            if IsFreeCase(N, Q, [i, j]):
                F.append([i, j])
    return F

def MaxQueens(N):

        # Init
    Open = []
    Q = []
    Qmax = []
    A = []
    for i in range(N):
        for j in range(N):
            A.append([i, j])

    Open.append(A)

        # Main loop
    while len(Open) != 0:

        q = Open[-1][0].copy()
        Q.append(q.copy())

        if len(Q) > len(Qmax):
            Qmax = Q.copy()

        if len(Q) == N:
            return Q, len(Q)
        
        if len(FreeCases(N, Q)) != 0:
            Open.append(FreeCases(N, Q).copy())
        else:
            if len(Open[-1]) > 0:
                Open[-1].pop(0)
                Q.pop(-1)
        
            while(len(Open[-1]) == 0):
                if len(Q) != 0:
                    Q.pop(-1)
                Open.pop(-1)
                if len(Open) == 0:
                    break
                else:
                    Open[-1].pop(0)
                
    return Qmax, len(Qmax)
