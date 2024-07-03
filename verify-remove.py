import os

def verify_and_clean_label_file(label_file_path, data_directory, output_file_path):
    """
    Verifies that all image files mentioned in the label file exist in the data directory.
    Removes incorrectly formatted lines and writes the cleaned data to a new file.

    Args:
        label_file_path (str): Path to the label file.
        data_directory (str): Directory where the image files are stored.
        output_file_path (str): Path to the output file where cleaned data will be saved.
    """
    with open(label_file_path, 'r', encoding='utf-8') as label_file:
        lines = label_file.readlines()
    
    valid_lines = []
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) < 2:
            print(f"Skipping incorrectly formatted line: {line.strip()}")
            continue
        
        image_file = parts[0]
        image_path = os.path.join(data_directory, image_file)
        
        if os.path.exists(image_path):
            valid_lines.append(line)
        else:
            print(f"Image file does not exist: {image_file}")

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(valid_lines)

    print(f"Cleaned label file saved to: {output_file_path}")

# Example usage
label_file_path = 'UTRSet-Real/UTRSet-Real/train/gt.txt'
data_directory = 'UTRSet-Real/UTRSet-Real/train/'
output_file_path = './cleaned_gt.txt'

verify_and_clean_label_file(label_file_path, data_directory, output_file_path)
