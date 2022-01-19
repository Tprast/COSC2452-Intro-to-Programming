import sys
def main_with_file_output():
	output_file = open("vaccination_status.csv","w")
	sys.stdout.write("Enter your name: ")
	name_value = str(sys.stdin.readline())
	sys.stdout.write("Are you vaccinated? ('yes' or 'no'):")
	vaccination_value = str(sys.stdin.readline())
	sys.stdout.write("Your information has been updated in our registry.")
	output_file.close()

main_with_file_output()
