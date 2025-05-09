Strassen Matrix Multiplication Benchmark 🚀
This Python project compares the performance of the Strassen matrix multiplication algorithm with the standard matrix multiplication algorithm. It reads matrices from a file, performs multiplications using both methods, measures execution times, and outputs results to the console and a CSV file. 📊
✨ Features

📥 Reads pairs of matrices from a text file (matrices.txt).
🔢 Implements standard matrix multiplication.
🌟 Implements Strassen's algorithm for matrix multiplication.
✅ Verifies that both algorithms produce identical results.
⏱ Benchmarks execution times for both algorithms.
📋 Outputs results in a formatted table and saves them to results.csv.

🛠 Prerequisites

🐍 Python 3.7 or higher
🚫 No external libraries required (uses standard library module: time)


⚙️ Setup

Clone or Download 📥

Obtain the project files from the repository.


Prepare Input File 📝

Create a matrices.txt file in the project root with matrices in the following format:
Each matrix is represented by rows of space-separated integers.
Matrices are separated by a blank line.
Example:
```
1 2
3 4

5 6
7 8
```
This represents two 2x2 matrices to be multiplied.




Ensure Python is Installed 🐍

Verify Python 3.7+ is installed by running:python --version





🚀 Usage

Place matrices.txt in the project directory.
Run the script from the terminal:python main.py



The program will:

📖 Read pairs of matrices from matrices.txt.
🔢 Compute matrix products using both standard and Strassen algorithms.
📊 Display a table of matrix sizes and execution times.
💾 Save results to results.csv.

📈 Example Output
Console Output:
```
Calculating for 2x2 matrices... 🟢
Calculating for 4x4 matrices... 🟢
Matrix Size  Standard Time (s)  Strassen Time (s)
2            0.000123          0.000456
4            0.001234          0.002345

results.csv Content:
Matrix Size,Standard Time (s),Strassen Time (s)
2,0.000123,0.000456
4,0.001234,0.002345 
```
📝 Notes

Modularity 🧩: The code is organized into modules for file handling, matrix operations, Strassen algorithm, and benchmarking for better maintainability.
Input Validation ⚠️: The script assumes matrices.txt is correctly formatted and matrices are compatible for multiplication.
Matrix Size 📏: Strassen’s algorithm is recursive and optimized for larger matrices, so performance benefits may be more noticeable with bigger inputs.
Error Handling 🚨: If results from standard and Strassen methods differ, a warning is printed.

🚧 Limitations

The Strassen algorithm assumes square matrices with dimensions that are powers of 2 for simplicity.
No padding is implemented for non-power-of-2 dimensions.
The script does not handle invalid input files robustly.


Happy benchmarking! 🎉 Feel free to contribute or open issues on GitHub! 😄
