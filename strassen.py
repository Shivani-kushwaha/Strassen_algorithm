import time
import argparse

def brut_force(A,B):
    """
    This function performs matrix multiplication using brute force method
    Arguments:
    A: First matrix
    B: Second matrix
    Returns:
    C: Resultant matrix
    count: Number of multiplications
    """
    # Get the dimensions of the matrices
    m, n = len(A), len(A[0])
    _, p = len(B), len(B[0])
    
    # Initialize the resultant matrix with zeros
    C = [[0 for i in range(p)] for j in range(m)]
    
    # Initilaize counter to count for multiplications 
    count = 0
    
    # Compute the matrix multiplication using brute force method
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
                count += 1
    return C,count


def add(A, B):
    """
    This function performs matrix addition
    Arguments:
    A: First matrix
    B: Second matrix
    Returns:
    C: Resultant matrix
    """
    # Get the dimensions of the matrices
    m, n = len(A), len(A[0])
    
    # Initialize the resultant matrix with zeros
    C = [[0 for i in range(n)] for j in range(m)]
    
    # Add the matrices
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract(A, B):
    """
    This function performs matrix subtraction
    Arguments:
    A: First matrix
    B: Second matrix
    Returns:
    C: Resultant matrix
    """
    # Get the dimensions of the matrices
    m, n = len(A), len(A[0])
    
    # Initialize the resultant matrix with zeros
    C = [[0 for i in range(n)] for j in range(m)]
    
    # Subtract the matrices
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def split(M):
    """
    This function splits a matrix into quadrants
    Arguments:
    M: Matrix to be split
    Returns:
    c11: Quadrant 1
    c12: Quadrant 2
    c21: Quadrant 3
    c22: Quadrant 4
    """
    mid = len(M) // 2   
    c11 = [row[:mid] for row in M[:mid]]
    c12 = [row[mid:] for row in M[:mid]]
    c21 = [row[:mid] for row in M[mid:]]
    c22 = [row[mid:] for row in M[mid:]]
    return c11, c12, c21, c22

def strassen(A,B):
    """
    This function performs matrix multiplication using Strassen's algorithm
    Arguments:
    A: First matrix
    B: Second matrix
    Returns:
    C: Resultant matrix
    count: Number of multiplications
    """
    n = len(A)
    multiply_ops = 0
    # Base case: 1x1 matrix
    if n == 1:
      multiply_ops = 1
      return [[A[0][0] * B[0][0]]], multiply_ops
    
    # Splitting the matrices into quadrants
    a11, a12, a21, a22 = split(A)
    b11, b12, b21, b22 = split(B)
    
    # Strassen's 7 recursive multiplications
    m1, m1_ops = strassen(add(a11, a22), add(b11, b22))
    m2, m2_ops = strassen(add(a21, a22), b11)
    m3, m3_ops = strassen(a11, subtract(b12, b22))
    m4, m4_ops = strassen(a22, subtract(b21, b11))
    m5, m5_ops = strassen(add(a11, a12), b22)
    m6, m6_ops = strassen(subtract(a21, a11), add(b11, b12))
    m7, m7_ops = strassen(subtract(a12, a22), add(b21, b22))
    
    count = m1_ops+ m2_ops+ m3_ops+ m4_ops+ m5_ops+ m6_ops+ m7_ops
    
    # Calculating the result matrix
    c11 = add(subtract(add(m1, m4), m5), m7)
    c12 = add(m3, m5)
    c21 = add(m2, m4)
    c22 = add(subtract(add(m1, m3), m2), m6)
    
    # Constructing the result matrix from the quadrants
    C = [[0 for i in range(n)] for j in range(n)]
    mid = n//2
    for i in range(mid):
      for j in range(mid):
          C[i][j] = c11[i][j]
          C[i][j + mid] = c12[i][j]
          C[i + mid][j] = c21[i][j]
          C[i + mid][j + mid] = c22[i][j]

    return C, count

def check_power_of_2(n):
    """
    This function checks if the number is a power of 2
    Arguments:
    n: Number to check
    Returns:
    True if n is a power of 2, False otherwise
    """
    if n <= 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1

def read_matrices_from_file(filename):
    """ 
    This function reads the matrices from the file and returns them as a list of tuples.
    Arguments:
    filename: Name of the file containing the matrices
    Returns:
    A list of tuples containing the matrices. Each tuple contains two matrices A and B.
    """
    matrices = []

    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            if not line:  # End of file
                break
            elif line.strip() == '':
                continue
            try:
                n = int(line.strip())
                
                if not check_power_of_2(n):
                    print(f"Error: {n} is not a power of 2. Skipping matrices.")
                    #Skip the next 2n lines
                    for i in range(2*n):
                        f.readline()
                    continue
                try: 
                    A = [list(map(int, f.readline().split())) for i in range(n)] 
                except:
                    print(f"Non numeric entity detected in input at n: {n}")
                    exit(0)
                try: 
                    B = [list(map(int, f.readline().split())) for i in range(n)]
                except:
                    print(f"Non numeric entity detected in input at n: {n}")
                    exit(0)
                # Check if A and B are square matrices
                if any(len(row) != n for row in A) or any(len(row) != n for row in B):
                    print("Error: Non-square matrix detected. Skipping matrices.")
                    continue
                
                matrices.append((A, B))
            
            except ValueError:
                # Errors arising from incorrect file formatting
                print(f"Error reading matrices from file. Correct input and run again")
                exit(1)

    return matrices


if __name__ == "__main__":
    # Reading input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default='LabStrassenInput.txt', help="Input file name, $file_path/$input_filename.txt or input_filename.txt if input file in same directory as source.py")
    parser.add_argument("--output", default='LabStrassenOutput.txt', help="Output file name, $file_path/$output_filename.txt or output_filename.txt if input file in same directory as source.py")
    args = parser.parse_args()
    # Reading the matrices from the file
    matrices = read_matrices_from_file(args.input)
    # Initializing dicts To record processing time
    time_normal = {}
    time_strassen = {}
    # Writing the results to output file
    with open(args.output, 'w') as f:
      # Computing multiplications for each set in the input file and writing the results to output file
      # Iterating over each set in the list of matrix and saving the results 
      
      for i, (A, B) in enumerate(matrices):
        f.write("\n########\n")
        f.write("\nComparing Brute Force (Ordinary) and Strassen Multiplication for Matrix Order "+str(len(A))+"\n")
        f.write("\n########\n")
        
        f.write("\nMatrix Multiplication Method: Strassen")
        
        st = time.time()
        C,count = strassen(A,B)
        time_strassen[len(A)] = time.time()-st
        
        f.write("\nNo. of Multiplications: "+str(count))
        f.write('\nTime taken to compute: ' +str(time_strassen[len(A)]))
        
        f.write('\nResult:\n')
        for row in C:
            f.write(str(row)+'\n')
        
        f.write("\n------\n")
        f.write("\n------\n")
        
        f.write("Matrix Multiplication Method: Ordinary")
        
        st = time.time()
        C,count = brut_force(A,B)
        time_normal[len(A)] = time.time()-st
        
        f.write("\nNo. of Multiplications: "+str(count))
        f.write('\nTime taken to compute: ' +str(time_normal[len(A)]))

        f.write('\nResult:\n')
        for row in C:
            f.write(str(row)+'\n')

    f.close()
    print(time_strassen, time_normal)