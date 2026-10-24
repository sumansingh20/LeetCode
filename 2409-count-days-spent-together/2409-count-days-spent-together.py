class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)
        
        if arrive > leave:
            return 0
            
        m1 = int(arrive[:2])
        d1 = int(arrive[3:])
        day1 = d1
        for i in range(m1 - 1):
            day1 = day1 + days[i]
            
        m2 = int(leave[:2])
        d2 = int(leave[3:])
        day2 = d2
        for i in range(m2 - 1):
            day2 = day2 + days[i]
            
        return day2 - day1 + 1