import sys
def main_with_file_output():
	output_file = open("fib.csv","w")
	sys.stdout.write("Enter an i value (negative to quit): ")
	entered_i_value = int( sys.stdin.readline() )
	while(entered_i_value>=0):
		fibonacci_value_at_i = get_fib_at_v2(entered_i_value)
		sys.stdout.write ( str(entered_i_value)+","+str(fibonacci_value_at_i)+"\n" )
		output_file.write( str(entered_i_value)+","+str(fibonacci_value_at_i)+"\n" )
		sys.stdout.write("Enter an i value (negative to quit): ")
		entered_i_value = int( sys.stdin.readline() )
	output_file.close()
def get_fib_at_v2(i):
	if ((i==1) or (i==0)):
		return i
	return get_fib_at_v2(i-1) + get_fib_at_v2(i-2)
main_with_file_output()
