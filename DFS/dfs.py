# Depth First Search (DFS) - Campus Connectivity Exploration
# Institution: KPR Institute of Engineering and Technology
# Student: Santhosh S (Roll No: 25AD149)
# Department: Artificial Intelligence and Data Science

# Campus building connections represented as an adjacency list
campus_network = {
    "Main Block": ["AI & DS Lab", "Library", "Auditorium"],
    "AI & DS Lab": ["Main Block", "CSE Block", "Seminar Hall"],
    "Library": ["Main Block", "Cafeteria"],
    "CSE Block": ["AI & DS Lab", "Hostel"],
    "Auditorium": ["Main Block", "Seminar Hall"],
    "Cafeteria": ["Library", "Hostel"],
    "Seminar Hall": ["AI & DS Lab", "Auditorium"],
    "Hostel": ["CSE Block", "Cafeteria"],
}

print("=== DFS - Campus Exploration & Connectivity ===")
start_location = "Main Block"
print("Starting Location:", start_location)
print()

visited = []
step = 1


def explore_campus(current_node):
  global step
  visited.append(current_node)
  print(f"Step {step}: Visiting [{current_node}]")
  print(f"  Visited Set : {visited}")

  neighbors = campus_network.get(current_node, [])
  step += 1

  for neighbor in neighbors:
    if neighbor not in visited:
      print(f"  -> Branch : {current_node} -> {neighbor}")
      explore_campus(neighbor)
      print(f"  <- Backtracked to : {current_node}")


# Execute Depth First Search starting from Main Block
explore_campus(start_location)

print()
print("=== Campus Exploration Summary ===")
print("Total Buildings Explored:", len(visited))
print("Traversal Order         :", " -> ".join(visited))
print("Network Status          : FULLY CONNECTED (All facilities reachable)")
