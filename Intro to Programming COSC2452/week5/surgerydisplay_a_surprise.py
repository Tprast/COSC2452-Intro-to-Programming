import sys
#patients=["Tim","David","Sam"]

#doctors=["Dr Smith","Dr Hughes","Dr Klein"]

#for p,d in zip(patients,doctors):
   # print('{0} will see {1}.' .format(p,d))





patientDoctor={"Tim":"Dr Smith","David":"Dr Hughes","Sam":"Dr Klein"}
def display_queue():
    for p,d in patientDoctor.items():
        print(d, "will see",p)

def surprise():
    sys.stdout.write("\nThe patients listed below are currently in line:\n... #$%^#$%...\nsystem malfunction\n\
\nYour position is arbitary.. the Doctors obey no queue rules...\n\
Welcome to polite waiting purgatory.\n\
Remember to wear your mask.\n\
\nWe thank-you for your patience\n\
------------------------------------------------------------------------------")

