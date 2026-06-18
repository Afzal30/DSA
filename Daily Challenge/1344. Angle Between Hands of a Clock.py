class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        angle = abs((60*hour - 11*minutes)/2)
        
        return angle if angle<=180 else 360-angle


#another mathematical formula

"""
Approach
compute the angle at which the minute hand is present.
angle in 1 minute = 360/60 = 6 degree
minuteAngle = 6* minutes
compute the angle at which the hour hand is present.
angle in 1 hour = 360/12 = 30 degree
angle in 1 minute = 360/720 = 0.5 degree
hourAngle = 30* (hours%12) + 0.5 * minutes
now find the difference in angles, diff = abs(minuteAngle , hourAngle)
return the min angle, min(diff, 360-diff)
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 6.0 * minutes
        hour_angle = 30.0 * (hour % 12) + 0.5 * minutes

        diff = abs(hour_angle - minute_angle)

        return min(diff, 360.0 - diff)
