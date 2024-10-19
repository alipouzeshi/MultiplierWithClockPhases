his repository implements two different algorithms for binary multiplication: Shift and Add and Booth's Algorithm. The code showcases detailed intermediate calculations and emphasizes the clock phases for each step of the multiplication process.

Features
Two Multiplication Methods:

Shift and Add: A straightforward approach for multiplying binary numbers using bit shifting and addition.
Booth's Algorithm: An efficient algorithm that handles both signed and unsigned numbers with fewer operations.
Clock Phase Representation:

Each multiplication process is thoroughly documented with clock phases, illustrating how the algorithms progress through each cycle, making it easier to understand the sequence of operations.
Two's Complement Conversion:

The code includes a function for converting decimal numbers to their two's complement binary representation, essential for handling negative numbers in signed multiplication.
Input/Output
The program reads from a text file (in.txt) which contains multiple batches of data for multiplication, including:

The number of test cases
Algorithm type (0 for Shift & Add, 1 for Booth)
Bit length of the numbers
Signed or unsigned indication
The two integers (A and B) to multiply
Outputs are written to a text file (out.txt), showing:

Two's complement representations of inputs
Intermediate values at each step of multiplication
Final product in decimal
