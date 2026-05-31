# Write code below 💖

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

# Define the two variables
item_to_find = 'ACG'
item_found = False

# Loop through each item in the list
for item in dna_sequence:
    if item == item_to_find:
        item_found = True

# Check result outside the loop
if item_found:
    print("Item Found!")
else:
    print("Item not found.")
