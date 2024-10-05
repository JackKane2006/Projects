matrix = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0]
] #each set of connected 1's is a river
    #the size of the river is equal to the amount of 1's it consists of

def RiverSizes(matrix): #returns a list containing the sizes of each river in matrix
    rivers = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
    riverSize = 0
    mustSearch = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                mustSearch.append((i, j))

                while mustSearch: 
                    current_y, current_x = mustSearch.pop()

                    if matrix[current_y][current_x] == 1:
                        matrix[current_y][current_x] = 0 
                        riverSize += 1

                        for j in dirs: 
                            if 0 <= current_y + j[1] < len(matrix) and 0 <= current_x + j[0] < len(matrix[0]):
                                mustSearch.append((current_y + j[1], current_x + j[0]))

                rivers.append(riverSize)
                riverSize = 0

    return rivers

print(RiverSizes(matrix))