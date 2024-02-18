# This problem was asked by Microsoft.
# Rating: Easy

# Given a clock time in hh:mm format, determine, to the nearest degree, 
# the angle between the hour and the minute hands.

#Bonus: When, during the course of a day, will the angle be zero? 

# 360 degrees in a circle
# 60 minutes on a clock
# 12 hours on a clock 

# 360/60 = 6
# 360/12 = 30

#if the hour is 03:45 the hour would be 90 and the minute would be 270 so the angle is 180

hour, minute = input("What time is it? (using hh:mm format) ").split(":")

angle = abs((int(hour) * 30) - (int(minute) * 6))

print(f"The angle between {hour} hours and {minute} minutes is {angle}")

#Bonus: When, during the course of a day, will the angle be zero? 
    # -> when hour * 30 == minute * 6


# At first I was trying to see if I could use trig to find the angle 
# but then I realized the question was rated easy so I figured there 
# had to be a simpler solution. In an actual interview im not sure 
# there'd be a rating so I have to work on reseting my thought process.