# Strassen_algorithm
Comparison of Strassen matrix multiplication algorithm with brute force algorithm

This project focuses on implementing and comparing the standard matrix multiplication algorithm with the Strassen algorithm. The project consists of the following files:

Analysis_Strassen_SK.pdf
README.txt
My code: strassen.py
Provided Input file: LabStrassenInput.txt
Provided Output file: LabStrassenoutput.txt
Custom input file: custom_input.txt
Custom output file: custom_output.txt
Custom input file with error: custom_input_w_error.txt

The code starts with Strassen's multiplication and then moves on to the standard multiplication, in this case, I used brute force matrix multiplication. The Strassen multiplication function was the first thing I created. As inputs, it takes matrix A, B, and the order of the matrix. This function divides the matrix into smaller components and performs the necessary calculations to produce the final matrix. It employs seven multiplication formulas and four formulas for combining small matrices.

Next, I created a brute-force matrix multiplication code with three loops. I also created a function called check_power_of_2 to determine whether a matrix is a power of two in size or if its row and columns are not aligned or matrices with non-integer values. If the file contains any non-number entries, the program will terminate. 

The data was then arranged into matrices using the code to read the input file. The size of the matrix should be listed first in the input file, followed by the two matrices with no blank lines in between. Before or after this order, blank lines can be handled by the code. Finally, I stored my results in the output file. There are several comments throughout my code that make it easy to understand.

Running the code:

- To run the code, download the zip file, and uncompress it. 
- Go to the working directory and use the following commands to run the source.py file.
- To run the LabStrassenInput.txt file:
	python3 source.py --input LabStrassenInput.txt --output LabStrassenOutput.txt
- To run the custom_input_file:
	python3 source.py --input custom_input.txt --output custom_output.txt
- To run the custom_input_w_error_file:
	python3 source.py --input custom_input_w_error.txt --output custom_error_test.txt

When we run the custom_input_w_error_file, one will get the following error as I have introduced non-numeric digits and a digit which is not power of 2 in the input file.

Error: 3 is not a power of 2. Skipping matrices.
Non-numeric entity detected in input at n: 
