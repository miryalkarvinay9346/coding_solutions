def findLeagueWinner(A, M):
    # write your code here 
    if A==M:
        return "DRAW"
    if A>M:
        return "TEAM A"
    return "TEAM M"
    """
    if A > M:
        return "TEAM A"
    elif M > A:
        return "TEAM M"
    else:
        return "DRAW"
        
    """