import sys
def getFibAt(i): #return Fibonacci series value at i
   a, b=0, 1
   while i>0:
      a, b = b, a+b
      i-=1
   return a
sys.stdout.write("Enter a position in the Fibonacci sequence: ")
i = int( sys.stdin.readline() )
answer = getFibAt(i)
sys.stdout.write( str(answer)+" is at "+str(i))
