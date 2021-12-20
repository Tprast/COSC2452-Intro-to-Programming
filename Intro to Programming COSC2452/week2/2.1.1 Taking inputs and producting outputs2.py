import sys
sys.stdout.write("Enter ID: ")
roleID=int(sys.stdin.readline())
sys.stdout.write("Enter ID "+str(roleID)+" 's role: ")
role=sys.stdin.readline().strip()
sys.stdout.write("Hello "+role+" 00"+str(roleID))
