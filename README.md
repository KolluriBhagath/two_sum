This Python program reads a list of integers and a target number, then finds the indices of the two numbers in the list that add up to the target.
It uses a dictionary to store previously seen numbers for fast lookup, making the solution efficient.

🔧 How It Works:
Input:
The user enters a list of space-separated integers.
The user enters a target integer.

Processing:
Iterate over the list using enumerate() to access both the index i and value num.
For each number, calculate its complement: target - num.
Check if this complement already exists in the dictionary lst.
If it does, return the indices of the complement and the current number.
If not, store the current number and its index in the dictionary for future reference.

Output:
Prints the pair of indices that correspond to the two numbers adding up to the target.

