import sys
isCaffeinated=False
isCupEmpty=False
if isCaffeinated and isCupEmpty:
    sys.stdout.write("You are jittery!")
if isCaffeinated or isCupEmpty:
    sys.stdout.write (" I probably need more coffee..")
#if not isCupEmpty:
 #   sys.stdout.write("Seems like you aren't fully caffinated yet...")
if not isCupEmpty and isCaffeinated:
    pass
