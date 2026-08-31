class Solution:
    def nodesBetweenCriticalPoints(self, head):
        points = []
        pos = 1
        prev = head
        curr = head.next
        while curr.next:
            if curr.val > prev.val and curr.val > curr.next.val:
                points.append(pos)
            elif curr.val < prev.val and curr.val < curr.next.val:
                points.append(pos)
            prev = curr
            curr = curr.next
            pos += 1
        if len(points) < 2:
            return [-1, -1]
        mini = points[1] - points[0]
        for i in range(2, len(points)):
            mini = min(mini, points[i] - points[i - 1])
        maxi = points[-1] - points[0]
        return [mini, maxi]