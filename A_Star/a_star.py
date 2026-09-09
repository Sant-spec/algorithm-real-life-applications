# A* Search Algorithm - Campus Route Navigation
# Institution: KPR Institute of Engineering and Technology
# Student: Santhosh S (Roll No: 25AD149)
# Department: Artificial Intelligence and Data Science

import heapq
import math

# Metric 2D Coordinates (x, y) in meters on campus plane
coordinates = {
    "Main Gate": (0, 0),
    "Parking": (40, 60),
    "Main Block": (120, 50),
    "AI & DS Block": (220, 80),
    "Library": (160, 160),
    "Auditorium": (280, 180),
    "Canteen": (180, 260),
    "Sports Ground": (320, 300),
    "Hostel": (240, 380),
}

# Campus walkway network with realistic walking distances (meters)
walkways = {
    "Main Gate": [("Parking", 80), ("Main Block", 140)],
    "Parking": [("Main Gate", 80), ("Main Block", 90)],
    "Main Block": [
        ("Main Gate", 140),
        ("Parking", 90),
        ("AI & DS Block", 110),
        ("Library", 125),
    ],
    "AI & DS Block": [("Main Block", 110), ("Auditorium", 125)],
    "Library": [("Main Block", 125), ("Auditorium", 130), ("Canteen", 110)],
    "Auditorium": [
        ("AI & DS Block", 125),
        ("Library", 130),
        ("Sports Ground", 135),
    ],
    "Canteen": [("Library", 110), ("Sports Ground", 155), ("Hostel", 145)],
    "Sports Ground": [("Auditorium", 135), ("Canteen", 155), ("Hostel", 125)],
    "Hostel": [("Canteen", 145), ("Sports Ground", 125)],
}


def heuristic(node, goal):
  """Computes straight-line Euclidean distance from node to goal."""
  x1, y1 = coordinates[node]
  x2, y2 = coordinates[goal]
  return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 1)


print("=== A* SEARCH - Campus Shortest Path ===")
start = "Main Gate"
goal = "Hostel"
print(f"Start: {start} -> Goal: {goal}\n")

# Priority Queue stores: (f_score, counter, node)
counter = 0
open_queue = [(heuristic(start, goal), counter, start)]
g_score = {start: 0}
came_from = {}
closed_set = set()
step = 1

while open_queue:
  f, _, curr = heapq.heappop(open_queue)
  if curr in closed_set:
    continue
  closed_set.add(curr)

  g = g_score[curr]
  h = heuristic(curr, goal)
  print(f"Step {step}: Expanding [{curr}] (g={g}, h={h}, f={f})")
  step += 1

  if curr == goal:
    print("  Goal reached successfully!")
    break

  for neighbor, cost in walkways.get(curr, []):
    if neighbor in closed_set:
      continue

    new_g = g + cost
    if neighbor not in g_score or new_g < g_score[neighbor]:
      g_score[neighbor] = new_g
      came_from[neighbor] = curr
      h_nb = heuristic(neighbor, goal)
      f_nb = new_g + h_nb
      counter += 1
      heapq.heappush(open_queue, (f_nb, counter, neighbor))
      print(
          f"  -> Added neighbor: {neighbor} (g={new_g}, h={h_nb},"
          f" f={round(f_nb, 1)})"
      )

# Reconstruct optimal path
path = []
curr = goal
while curr in came_from:
  path.append(curr)
  curr = came_from[curr]
path.append(start)
path.reverse()

print()
print("=== Optimal Route Navigation ===")
print("Shortest Path :", " -> ".join(path))
print("Total Distance:", g_score[goal], "meters")
