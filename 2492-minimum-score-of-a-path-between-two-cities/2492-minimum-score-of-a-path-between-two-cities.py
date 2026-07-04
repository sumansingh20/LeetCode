class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for city1, city2, distance in roads:
            graph[city1].append((city2, distance))
            graph[city2].append((city1, distance))
        visited_cities = set()
        visited_cities.add(1)
        queue = [1]
        minimum_score = float('inf')
        while len(queue) > 0:
            current_city = queue.pop(0)
            for next_city, distance in graph[current_city]:
                if distance < minimum_score:
                    minimum_score = distance
                if next_city not in visited_cities:
                    visited_cities.add(next_city)
                    queue.append(next_city)
        return minimum_score

