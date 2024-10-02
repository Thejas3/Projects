class EmptyRosterError(Exception):
  pass

class Student:
  def __init__(self, first_name, last_name, gpa):
      self.first_name = first_name
      self.last_name = last_name
      self.gpa = gpa
  def get_first(self):
      return self.first_name
  def get_last(self):
      return self.last_name
  def get_gpa(self):
      return self.gpa


class Course:
  def __init__(self):
      self.roster = []
  def add_student(self, student):
      return self.roster.append(student)
  def course_size(self):
      return len(self.roster)
  def find_student_highest_gpa(self, key_function):
      if not self.roster:
          raise EmptyRosterError("Error: Course Roster is Empty")

      highest_gpa_student = max(self.roster, key=key_function)
      return highest_gpa_student

def get_gpa(student):
  return student.get_gpa()

def main():
  course = Course()

  quit_list = ['q', 'quit']

  print('Welcome to CSC/DSC1 1301: Principles in CS/DS1')
  while True:
      user_command = input("Please Add Students to the Course: (quit or q to exit): ")
      if user_command in quit_list:
          break
      else:
          first_name = input("Enter the First Name: ")
          last_name = input("Enter the Last Name: ")
          try:
              gpa = float(input("Enter the GPA: "))
          except ValueError:
              print("Error: Enter a Numerical GPA ")
              continue


          student = Student(first_name, last_name, gpa)
          course.add_student(student)

  print(f"\nNumber of students enrolled: {course.course_size()}")
  try:
      highest_student_gpa = course.find_student_highest_gpa(key_function=get_gpa)
      print(f"Top Student: {highest_student_gpa.get_first()} {highest_student_gpa.get_last()} ({highest_student_gpa.get_gpa()})")
      quit()
  except EmptyRosterError as error:
      print(error)

main()
  