import sys
def main_A_league_scores():
	input_file = open("task512.txt","r")
	sys.stdout.write("Below are the recent A League Results.\n")
	A_league_results = input_file.readline()
	while(A_league_results!=""):
		sys.stdout.write(A_league_results)
		A_league_results = input_file.readline()
	sys.stdout.write("\nThis program is now finished displaying the results")
	input_file.close()

main_A_league_scores()
