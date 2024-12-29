def towersofhanoi(n, s, d, a):
    if (n == 1):
        print(f"move from source {s} to destination {d}")
        return
    
    towersofhanoi(n-1, s, a, d)
    print(f"move from source {s} to destination {d}")
    towersofhanoi(n-1, a, d, s)

n = 3
towersofhanoi(n , 'A', 'B', 'C')