def merge(file1_path, file2_path, result_path):
    try:
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(result_path, 'w') as result_file:
            result_file.write(file1.read())
            result_file.write(file2.read())
        print(f"Merged files '{file1_path}' and '{file2_path}' successfully. Result saved to '{result_path}'.")
    except FileNotFoundError:
        print("One of the input files does not exist.")
    except Exception as e:
        print(f"An error occurred while merging files: {e}")

def copy(file1_path, num_copies):
    try:
        if os.path.isfile(file1_path):
            file_dir = os.path.dirname(file1_path)
            file_name = os.path.basename(file1_path)
            for i in range(num_copies):
                copy_path = os.path.join(file_dir, f"copy_{i+1}_{file_name}")
                with open(file1_path, 'r') as original, open(copy_path, 'w') as copy_file:
                    copy_file.write(original.read())
                print(f"Copy {i+1} of '{file1_path}' created successfully at '{copy_path}'.")
        else:
            print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred while copying the file: {e}")

def convert_to_csv(text_file_path, csv_file_path):
    try:
        with open(text_file_path, 'r') as text_file, open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for line in text_file:
                writer.writerow([line.strip()])
        print(f"Conversion from '{text_file_path}' to CSV '{csv_file_path}' successful.")
    except Exception as e:
        print(f"An error occurred while converting to CSV: {e}")

def file_statistics(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
        print(f"Statistics for file '{file_path}':")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred while processing file statistics: {e}")
