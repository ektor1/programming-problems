
def towerBreakers(n, m):
    """
    n = number of towers, m = height of towers
    Explanation: Since both players will always play optimally the winner is defined by the number and height of the towers.
    If there is only one tower of m > 1 then P1 will always win since he can reduce its height to 1 leaving P2 unable to play. 
    
    However, for any number of towers of m = 1, P2 will always win since P1 will be unable to make his first move.

    If there is an even number of towers, n%2 == 0, then P2 will always be able to mirror P1's moves. P2 has the advantage as he is always going 
    to be the last one that reduces the height of a tower to 1 making P1 unable to make a move. Therefore, when there is an odd number of 
    towers, n%2 != 0, P1 will always win since he always moves first. 
    """
    
    if n % 2 == 0 or m == 1:
        return 2
    
    else:
    # if n % 2!= 0:
    # if n % 2 == 0 and m % 2 == 2 
        return 1