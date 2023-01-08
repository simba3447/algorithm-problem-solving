def solution(triangle):
    height = len(triangle)
    cache = [[-1 for _ in range(height)] for _ in range(height)]

    def find_max(h, w):
        if h == height - 1:
            return triangle[h][w]
        
        if cache[h][w] == -1:
            cache[h][w] = max(find_max(h + 1, w), find_max(h + 1, w + 1)) + triangle[h][w]
        
        return cache[h][w]

    return find_max(0, 0)