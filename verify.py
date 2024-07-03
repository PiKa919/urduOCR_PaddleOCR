import os
import argparse

def verify_image_files(label_file, data_dir, delimiter='\t'):
    missing_files = []
    total_files = 0
    
    with open(label_file, 'r', encoding='utf-8') as f:
        for line in f:
            total_files += 1
            parts = line.strip().split(delimiter)
            if len(parts) < 2:
                print(f"Warning: Incorrectly formatted line: {line.strip()}")
                continue
            
            image_file = parts[0]
            full_path = os.path.join(data_dir, image_file)
            
            if not os.path.exists(full_path):
                missing_files.append(image_file)
    
    return missing_files, total_files

def main():
    parser = argparse.ArgumentParser(description="Verify existence of image files listed in a label file.")
    parser.add_argument("label_file", help="Path to the label file")
    parser.add_argument("data_dir", help="Path to the data directory containing images")
    parser.add_argument("--delimiter", default='\t', help="Delimiter used in the label file (default: tab)")
    
    args = parser.parse_args()
    
    missing_files, total_files = verify_image_files(args.label_file, args.data_dir, args.delimiter)
    
    print(f"Total files in label file: {total_files}")
    print(f"Number of missing files: {len(missing_files)}")
    
    if missing_files:
        print("\nMissing files:")
        for file in missing_files:
            print(file)
    else:
        print("\nAll image files exist!")

if __name__ == "__main__":
    main()