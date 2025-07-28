# Q1 write a LC program, to create an output dictionary which contain only the odd numbers that are present in the 
# input list = [1,2,3,4,5,6,7] as a key and their cubes as values.

input_list = [1, 2, 3, 4, 5, 6, 7]
output_list = {num : num**3 for num in input_list if num % 2 != 0}
print(output_list)

# Q2 make a dictionary of the 26 english alphabets mapping each with corresponding integer

alphabet_dict = {chr(i) : i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
print(alphabet_dict)
