import heapq
from typing import List
from collections import defaultdict


def dijkstra(edges: List[List[int]], start: int, end: int):
	graph = defaultdict(list)
	for src, dst, weight in edges:
		graph[src].append((weight, dst))

	queue, visited = [[0, start]], {}

	while queue:
		dist, node = heapq.heappop(queue)
		if node in visited:
			continue
		visited[node] = dist

		if node == end:
			return dist

		for cost, neighbor in graph[node]:
			if neighbor not in visited:
				heapq.heappush(queue, (dist + cost, neighbor))

	return float("inf")



def main():
	edges = [[0, 1, 4], [0, 2, 1], [2, 1, 2], [1, 3, 1], [2, 3, 5]]
	start, end = 0, 3
	print(dijkstra(edges, start, end))  #


if __name__ == "__main__":
	main()
