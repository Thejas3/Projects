# Thejas Sreenivas; panther_ID: 002664906
# This is my code for Homework 2 and this program allows the user to see the details of a student and a course that the university provides
# and allows them to edit any part of the table seen below. It provides a menu to begin with so that the user can see their options and can
# choose what they will like to do and how they can proceed with their desired action (which command they should run), then finally they can
# edit it and be able to give their final output after they are finished editing. The user can then click q to quit. 


class Student_and_Course_Database:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.next_id = 1

    def add_record(self, table, record):
        record_id = self.next_id
        self.next_id += 1
        table[record_id] = record
        print(f"Record added successfully with ID: {record_id}")

    def remove_record(self, table, record_id):
        if record_id in table:
            del table[record_id]
            print(f"Record with ID {record_id} removed successfully")
        else:
            print(f"Record with ID {record_id} not found")

    def print_all_records(self, table):
        print(f"All records in the table:")
        for record_id, record in table.items():
            print(f"ID: {record_id}, Record: {record}")

    def print_record(self, table, record_id):
        if record_id in table:
            print(f"Record with ID {record_id}: {table[record_id]}")
        else:
            print(f"Record with ID {record_id} not found")

    def update_record(self, table, record_id, column, new_value):
        if record_id in table:
            if column in table[record_id]:
                table[record_id][column] = new_value
                print(f"Record with ID {record_id} updated successfully")
            else:
                print(f"Column {column} not found in the record")
        else:
            print(f"Record with ID {record_id} not found")


def main():
    database = Student_and_Course_Database()

    while True:
        command = input("Enter a command (add, remove, print, update, quit): ").lower()

        if command == 'quit' or command == 'q':
            break
        elif command == 'add' or command == 'a':
            table_name = input("Enter the table name (students, courses): ").lower()
            if table_name == 'students' or table_name == 's':
                # These will be the columns for the student table that will be used for a student's identification.
                record = {'First Name': str(input("Enter student's first name: ")),
                          'Last Name': str(input("Enter student's last name: ")),
                          'Panther ID ': int(input("Enter student's panther ID: ")),
                          'Major': str(input('Enter your major: ')),
                          'Honors': str(input("Are you in Honors? "))}
                database.add_record(database.students, record)
            elif table_name == 'courses' or table_name == 'c':
                # These will be the columns for the courses that a student will take and the course's information.
                record = {'Course Name': str(input("Enter course name: ")),
                          'Professor': str(input("Enter instructor name: ")),
                          'Credits': int(input("Enter course credits: ")),
                          'Days': str(input('Enter which days the classes are held: ')),
                          'CRN': int(input('Enter the CRN of the class: '))}
                database.add_record(database.courses, record)
            else:
                print("Invalid table name")
            # This command will removed any detail that the user wishes to remove. 
        elif command == 'remove' or command == 'r':
            table_name = input("Enter the table name (students, courses): ").lower()
            record_id = int(input("Enter the ID of the record to remove: "))
            if table_name == 'students' or table_name == 's':
                database.remove_record(database.students, record_id)
            elif table_name == 'courses' or table_name == 'c':
                database.remove_record(database.courses, record_id)
            else:
                print("Invalid table name")
            # This will print the existing column of either the student's information or the course info.
        elif command == 'print' or command == 'p':
            table_name = input("Enter the table name (students, courses): ").lower()
            if table_name == 'students' or table_name == 's':
                database.print_all_records(database.students)
            elif table_name == 'courses' or table_name == 'c':
                database.print_all_records(database.courses)
            else:
                print("Invalid table name")
            # this will update the existing tables, so if there is name it will change it to the new name.
        elif command == 'update' or command == 'u':
            table_name = input("Enter the table name (students, courses): ").lower()
            record_id = int(input("Enter the ID of the record to update: "))
            column = input("Enter the column to update: ").lower()
            new_value = input("Enter the new value: ")
            if table_name == 'students' or table_name == 's':
                database.update_record(database.students, record_id, column, new_value)
            elif table_name == 'courses' or table_name == 'c':
                database.update_record(database.courses, record_id, column, new_value)
            else:
                print("Invalid table name")

        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
