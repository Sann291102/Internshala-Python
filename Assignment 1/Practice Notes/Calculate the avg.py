## Calculate the average.
day = 0
squats = 0
total = 0
print("Enter the no.of sqauts you did on each day for a week")
while day<=6:
    day=day+1
    squats = int(input("squats on day {} : ".format(day)))
    total = total + squats
avg = total/day
print("in the last {} days you did an avg {} of squats!".format(day , avg))