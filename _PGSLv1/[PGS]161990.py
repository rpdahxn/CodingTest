# 1
# def solution(wallpaper):
#     answer = []
    
#     h = len(wallpaper)
#     w = len(wallpaper[0])
#     files = []
    
#     for i in range(h):
#         for j in range(w):
#             if wallpaper[i][j] == '#':
#                 files.append([i, j])
#     files.sort(key = lambda x : (x[0], x[1]))

#     min_y = min(files, key=lambda x: x[1])[1]
#     max_y = max(files, key=lambda x: x[1])[1]
#     start = [files[0][0], min_y]
#     end = [files[-1][0]+1, max_y+1]

            
#     return start+end

# 2
def solution(wallpaper):

    h = len(wallpaper)
    w = len(wallpaper[0])
    xs = []
    ys = []
    
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == '#':
                xs.append(i)
                ys.append(j)

    return [min(xs), min(ys), max(xs)+1, max(ys)+1]