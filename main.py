from manager import *
from colorama import Fore


Role_of_user = ""
def start():
	global Role_of_user
	Role_of_user = User_role_provider(input("Enter your role i.e(teacher/student): "),input("Enter your password: "))

start()
chance_left = 3
def submit_data(Role_of_user):
	Task = ""
	if Role_of_user == "Teacher":
		print("\n" + Fore.YELLOW + "Namaste sir/mam ! Please choose your task: ")
		print("""Type a for - Add a new student\n\tu for - Update Student details\n\tr for - Remove Student\n\tg for - Get student Details\n""" )
		print("""Type 'q' to exit.""")
		while True:
			Task = input("》》》》")
			if Task.upper() == "A":
				print("Please input student details.\n")
				std_name = str(input("Enter the student Name: "))
				std_class = str(input("Enter class + section: "))
				std_rollno = str(input("Enter roll number: "))
				std_stream = str(input("Enter the stream i.e (PCM,PCB):  "))
				for i in range(2,0,-1):
					if std_stream.upper() == "PCM":
						mrk_of_std_Unit_1 = input("Enter marks of Unit 1 \n(seperated by',' & format => M,P,C,Cs,IP,E,H: \n")
						break
					elif std_stream.upper() == "PCB":
						mrk_of_std_Unit_1 = input("Enter marks of Unit 1  \n(seperated by',' & format => B,P,C,E,H: \n")
						break;
					else:
						print(Fore.RED+"Please enter valid option.")
						continue;
						
				student_details = std_rollno+" "+std_name+" "+std_class+" "+mrk_of_std_Unit_1+" "+std_stream
				print(Fore.BLUE + f"""\n\nNAME: {std_name}\nClass: {std_class}\nRoll no: {std_rollno}\nStream: {std_stream}\n Marks of unit 1st Test:\n {mrk_of_std_Unit_1}""")
				a = input(Fore.YELLOW+ "Please check the details. And type 's' to save and 'c' to cancel.\n")
				if a.upper() == "S":
					add_student(Role_of_user,Student_details = student_details)
					print(Fore.GREEN+"Data Added data successfully.")
				elif a.upper() == "C":
					continue;
				else:
					print("invalid input.")
				last_decision = input("Enter 'menu' to go back to menu  and 'q' to quit.")
				for i in range(2):
					if last_decision.upper() == "MORE":
						submit_data("Teacher")
					elif last_decision.upper() == "Q":
						break
					else:
						print("Enter valid option.")
						if i<2:
							continue
						else:
							break
			elif Task.upper() == "U":
				pass
				break;
			elif Task.upper() == "R":
				pass
				break;
			elif Task.upper() == "G":
				get_student_details(Role_of_user)
			elif Task.upper() == "Q":
				break;
			else:
				chance_left -= 1
				print(f"Invalid input. Please choose the correct value. You have only {chance_left} try left.")
				continue
	elif Role_of_user == "Student":
		print("Hello ! Please choose your task: ")
		print("""Type P for - Profile view R for - Result\n""" )
		Task = input("=> ")

submit_data(Role_of_user)
