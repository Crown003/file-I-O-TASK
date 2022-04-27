from colorama import Fore
User_role = "" #role to identify user

def User_role_provider(role,password):
	global User_role
	if role.upper() == "TEACHER" and password == "svm":
		User_role = "Teacher"
	elif role.upper() == "STUDENT" and password == "svms":
		User_role = "Student"
	else:
		print("Please enter the valid credentials.")
	return User_role if User_role else None


def add_student(UserRole,Student_details):
	"""This function is used to add a new student in file."""
	with open("students.txt","a") as f:
		f.write(Student_details)
		f.write(",\n")
	print(User_role)


def remove_student(User_role):
	pass
	


def update_student_details(User_role):
	pass



def get_student_details(user_role):
	with open("students.txt","r") as f:
		a = f.readlines()
		if a == []:
			print("No DATA FOUND")
		else:
			roll_number = input("Enter your roll number: ")
			Class_std = input("Enter class + section.\n(Do not leave space between class & sec)i.e:12b.\n=>")
			print("this is class test ---",f"{Class_std.upper()}")
			secure_num = []
			z = []
			selected_list = 0
			for text in a:
				z.append(text.split())
			for n in range(0,len(z)):
				if z[n][0] == roll_number and z[n][2].upper() == f"{Class_std.upper()}":
					selected_list = n # selected student data.
					b = z[n][3].split(",")
					for i in b:
						if i != "":
							secure_num.append(int(i))
						else:
							pass
					break;
				elif z[n][0] != roll_number and z[n][2].upper() != f"{Class_std.upper()}":
					continue;
				else:
					print("No student with given details")
				print(selected_list)
			if secure_num == []:
				print("No student found.")
			else:
				#M,P,C,Cs,IP,E,H
				if z[selected_list][4].upper() == "PCM," :
						print(f"""\nStudent name: {z[selected_list][1]}\nClass: {z[selected_list][2]}\n""")
						print(f"MARKS OF UNIT 1 =>\n")
						print(f"MATHS: {secure_num[0]}\nPHYSIC: {secure_num[1]}\nChemistry: {secure_num[2]}\nComputer science: {secure_num[3]}\nEnglish: {secure_num[4]}")
						secure_num = []
						z = []
						selected_list = 0
				#B,P,C,E,H
				elif z[selected_list][4].upper() == "PCB," :
						print(f"""\nStudent name: {z[selected_list][1]}\nClass: {z[selected_list][2]}\n""")
						print(f"MARKS OF UNIT 1 =>\n")
						print(f"BIOLOGY: {secure_num[0]}\nPHYSIC: {secure_num[1]}\nChemistry: {secure_num[2]}\nEnglish: {secure_num[3]}\nHindi: {secure_num[4]}")
						secure_num = []
						z = []
						selected_list = 0
				else:
					pass
					