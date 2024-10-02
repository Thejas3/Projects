import Thejas_Sreenivas_LAB12_FileProcessor as FileProcessor

with open("file1.txt", 'w') as file:
    file.write("Content of file1.txt\n")

with open("file2.txt", 'w') as file:
    file.write("Content of file2.txt\n")

with open("text_file.txt", 'w') as file:
    file.write("Line 1\nLine 2\Line 3\n")

def test_file_processor():
    FileProcessor.merge("file1.txt", 'file2.txt', "result.txt")

    FileProcessor.copy("file1.txt", 3)

    FileProcessor.convert_to_csv("text_file.txt", "csv_file.csv")

    FileProcessor.file_statistics('file1.txt')




if __name__ == "__main__":
    test_file_processor()
