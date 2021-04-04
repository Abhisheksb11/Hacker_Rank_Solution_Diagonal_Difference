def diagonalDifference(arr):
    
    d1=sum([arr[x][x] for x in range(len(arr))])
    d2=sum([arr[x][n-1-x]for x in range(len(arr))])
    
    return abs(d2-d1)
        
