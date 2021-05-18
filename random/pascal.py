
"""
def printPascal(testVariable):
  # Write your code here
  if testVariable == 0:
    return []
  results = []
  for row in range(1, testVariable):
    arr = []
    for col in range(0, row):
      if col == 0 or col == row-1:
        arr.append(1)
      else:
        arr.append(results[row-2][col-1] + results[row-2][col])
    results.append(arr)
  print(results)
  return None
"""

def print_pascal(number_of_rows):
    pascal_matrix = []
    for row in range(0, number_of_rows+1):
        arr = []
        for col in range(0, row+1):
            if col == 0 or col == row:
                arr.append(1)
            else:
                arr.append(pascal_matrix[row-1][col-1]+pascal_matrix[row-1][col])
        pascal_matrix.append(arr)
    print(pascal_matrix)
#print_pascal(1)


def pascal_recursive(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    return [1, pascal_recursive(num-1)+pascal_recursive(num-1),1]

print(pascal_recursive(5))