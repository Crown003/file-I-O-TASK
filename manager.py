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

# for teacher role #
def add_student(UserRole,Student_details):
	"""This function is used to add a new student in file."""
	with open("students.txt","a") as f:
		f.write(Student_details)
		f.write(",\n")
	print(User_role)


def remove_student(User_role):
	pass
	

def update_student_details():
	with open("students.txt","r+") as f:
		a = f.readlines()
		if a == []:
			print("No DATA FOUND")
		else:
			roll_number = input("Enter student roll number: ")
			Class_std = input("Enter class + section.\n(Do not leave space between class & sec)i.e:12b.\n")
			z = []
			print("\nWhat u wants to update ?")
			print("Type \nN for - Name\nC for - Class\nR for - Rollnumber\nS for - Stream\n")
			choice = input("=> ")
			for text in a:
				z.append(text.split())
			for n in range(0,len(z)):
				if z[n][0] == roll_number and z[n][2].upper() == Class_std.upper():
					if choice.upper() == "N":
						new_name = input("Enter new name of Student: ")
						z[n][1] = new_name
						for k in z:
							if k[n][0] == roll_number:
								continue
							else:
								for x in z:
									for c in range(0,len(x)):
										print(x[c])
										#f.write(x[c])
					elif choice.upper() == "C":
						pass
					elif choice.upper() == "R":
						pass
					elif choice.upper() == "S":
						pass
				elif z[n][0] != roll_number and z[n][2].upper() != Class_std.upper():
					continue
				else:
					pass
# for student role #
def Show_profile():
	with open("students.txt","r") as f:
		a = f.readlines()
		if a == []:
			print("No DATA FOUND")
		else:
			roll_number = input("Enter student roll number: ")
			Class_std = input("Enter class + section.\n(Do not leave space between class & sec)i.e:12b.\n")
			secure_num = []
			z = []
			selected_list = -1
			for text in a:
				z.append(text.split())
			for n in range(0,len(z)):
				if z[n][0] == roll_number and z[n][2].upper() == f"{Class_std.upper()}":
					selected_list = n # selected student data.
					break;
				elif z[n][0] != roll_number and z[n][2].upper() != f"{Class_std.upper()}":
					continue;
				else:		
					continue
				#M,P,C,Cs,IP,E,H
			if selected_list > -1:
				if z[selected_list][4].upper() == "PCM," :
					print(Fore.YELLOW + f"""\nStudent name: {z[selected_list][1]}\nClass: {z[selected_list][2]}\n""")
					selected_list = -1
				elif z[selected_list][4].upper() == "PCB," :
					print(Fore.YELLOW +f"""\nStudent name: {z[selected_list][1]}\nClass: {z[selected_list][2]}\n""")
					selected_list = -1
				else:
					pass
			else:
				print(Fore.RED + "NO DATA FOUND\n")


# main function #
def get_student_details(user_role):
	with open("students.txt","r") as f:
		a = f.readlines()
		if a == []:
			print("No DATA FOUND")
		else:
			roll_number = input("Enter student roll number: ")
			Class_std = input("Enter class + section.\n(Do not leave space between class & sec)i.e:12b.\n=>")
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
					pass
			if secure_num == []:
				print(Fore.RED + "\nNo student found.\n")
			else:
				#M,P,C,Cs,IP,E,H
				if z[selected_list][4].upper() == "PCM," :
						print(Fore.YELLOW +f"""\nStudent name: {z[selected_list][1]}\nClass: {z[selected_list][2]}\n""")
						print(f"MARKS OF UNIT 1 =>\n")
						print(f"MATHS: {secure_num[0]}\nPHYSIC: {secure_num[1]}\nChemistry: {secure_num[2]}\nComputer science: {secure_num[3]}\nEnglish: {secure_num[4]}\n")
						secure_num = []
						z = []
						selected_list = 0
				#B,P,C,E,H
				elif z[selected_list][4].upper() == "PCB," :
						print(Fore.YELLOW +f"""\nStudent name: {z[selected_list][1]}\nClass: {z[selected_list][2]}\n""")
						print(f"MARKS OF UNIT 1 =>\n")
						print(f"BIOLOGY: {secure_num[0]}\nPHYSIC: {secure_num[1]}\nChemistry: {secure_num[2]}\nEnglish: {secure_num[3]}\nHindi: {secure_num[4]}")
						secure_num = []
						z = []
						selected_list = 0
				else:
					pass
								
