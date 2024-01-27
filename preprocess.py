import os
import string
from underthesea import word_tokenize


# Define the preprocessing function
def lower_case_and_remove_punctuation(line):
    # return line.translate(str.maketrans('', '', string.punctuation))
    return line.lower().translate(str.maketrans('', '', string.punctuation))


def process(lines):
    
    # Remove the digits
    processed_lines = [''.join([c for c in line if not c.isdigit()]) for line in lines]
    
    
    # Remove the punctuation
    processed_lines = [lower_case_and_remove_punctuation(line) for line in processed_lines]
    
    
    
    return processed_lines
   

# Paths for the source and destination folders
source_folder = 'parallel/vi'
destination_folder = 'processed/vi'

# Check if destination folder exists, if not, create it
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Process each file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(source_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        processed_lines = process(lines)
            

        # Save the processed text in the destination folder
        output_file_path = os.path.join(destination_folder, filename)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.writelines(processed_lines)
