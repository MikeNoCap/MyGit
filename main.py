import random

# Get user input.
original_string = input("Enter something to \"nerdiate:\"\n")
# We need to save the original_string 
# so we can get the indexes for all the characters on line 16.

# Remove duplicates.
string = ''.join(sorted(set(original_string), key=original_string.index));

# Make string a list so we can work with it.
l_string = list(string);

# Randomize the list order so you can't just see the answer.
random.shuffle(l_string)

# Store all the indexes for the different characters in string in a list.
string_indexes = [l_string.index(i) for i in original_string]


# Here we build the final outcome in string format.
char_list = "Characters = " + str(l_string)
message_string = "".join(["{" + f"Characters[{i}]" + "}" for i in string_indexes])
message_string = f"outcome = f'{message_string}'"

outcome = f"{char_list}\n"+ message_string



print(outcome)
