import sys
class MyClass:
    vall=0
    sys.stdout.write("Hello from MyClass\n")

sys.stdout.write("Before creation of objects\n")
some_object1=MyClass()
some_object1.vall=3
some_object2=MyClass()
some_object2.vall=7
sys.stdout.write("After creation of objects\n")
print(some_object1.vall)
print(some_object2.vall)

sys.stdout.write(str(some_object1)+"\n")
sys.stdout.write(str(some_object2)+"\n")
