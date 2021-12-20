import sys
countries=["New Zealand", "Greenland", "America", "Hawaii", "Japan"]
hobbies=["Yoga", "Video games", "Reading", "Movies", "Hiking"]
for c in countries:
    sys.stdout.write(c+" "+str(len(c)))
