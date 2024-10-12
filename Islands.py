leetcode medium difficulty problem, https://leetcode.com/problems/number-of-islands/description/
def Islands(matrix):
    islands = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
    mustSearch = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "1":
                islands += 1
                mustSearch.append((i, j))

                while mustSearch: 
                    current_y, current_x = mustSearch.pop()

                    if matrix[current_y][current_x] == "1":
                        matrix[current_y][current_x] = "0"

                        for j in dirs: 
                            if 0 <= current_y + j[1] < len(matrix) and 0 <= current_x + j[0] < len(matrix[0]):
                                mustSearch.append((current_y + j[1], current_x + j[0]))

    return islands
