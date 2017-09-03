# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotateMatrix(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):

        #save top
        top = matrix[layer][i]

        #left -> top
        matrix[layer][i] = matrix[-i - 1][layer]

        #bottom -> left
        matrix[-i - 1][layer] = matrix[-layer - 1][-i -1]

        #right -> bottom
        matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

        #top -> right
        matrix[i][-layer - 1] = top
    return matrix