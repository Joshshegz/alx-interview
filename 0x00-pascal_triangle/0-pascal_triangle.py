def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    triangle = []  # Initialize an empty list to hold the rows of Pascal's Triangle

    for row_num in range(n):
        # Start each row with a list containing only the number 1
        row = [1] * (row_num + 1)  # Each row has `row_num + 1` elements, all initialized to 1
        
        # Calculate the values for the middle elements of the row (if any)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        
        triangle.append(row)  # Append the row to the triangle
    
    return triangle  # Return the complete triangle


pascal_triangle(n=10)

