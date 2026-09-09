# Real-Life Applications of Depth First Search (DFS) & A* Search Algorithm

**Student Details:**
- **Student Name:** Santhosh S
- **Roll Number:** 25AD149
- **Department:** Artificial Intelligence and Data Science (AI & DS)
- **Institution:** KPR Institute of Engineering and Technology
- **Repository:** [https://github.com/Sant-spec/algorithm-real-life-applications](https://github.com/Sant-spec/algorithm-real-life-applications)

---

## Project Overview

This repository demonstrates the practical engineering implementation and academic analysis of two essential graph search algorithms:
1. **Depth First Search (DFS)** — An uninformed search algorithm applied to **Campus and Building Connectivity & Facility Exploration**.
2. **A* Search Algorithm** — An informed heuristic search algorithm applied to **Optimal Campus Walkway Shortest Path Navigation**.

Both algorithms are formulated using real-world scenarios on the campus of **KPR Institute of Engineering and Technology**. The implementations are written in beginner-friendly, readable, standard Python (requiring no third-party libraries) and produce deterministic execution traces suitable for visual verification via Python Tutor.

---

## Real-World Problems

### 1. DFS: Campus Facility Connectivity & Exploration
- **Problem:** Campus management and automated tour systems need to determine whether all campus facilities (academic blocks, laboratories, hostels, auditoriums, and cafeterias) are interconnected via pedestrian pathways, ensuring zero unreachable locations and tracing exploration pathways.
- **Solution:** DFS traverses the campus graph deeply along each pathway using a Last-In First-Out (LIFO) recursive stack mechanism, marking visited locations and backtracking whenever dead ends or previously visited buildings are encountered.

### 2. A* Search: Campus Route & Shortest Path Navigation
- **Problem:** Students and autonomous electric shuttles need the shortest walking route between landmark destinations (e.g., from `Main Gate` to `Hostel`) across campus walkways of varying physical distances.
- **Solution:** A* evaluates nodes using an objective function $f(n) = g(n) + h(n)$ combining exact walkway walking distance $g(n)$ with straight-line Euclidean distance heuristic $h(n)$ to destination coordinates. This guarantees the lowest-cost physical route while minimizing state exploration.

---

## Algorithmic Theory

### Depth First Search (DFS)
- **Paradigm:** Uninformed (Blind) Graph Traversal.
- **Mechanism:** Explores as deep as possible along each branch before backtracking.
- **Data Structure:** LIFO Stack (implemented via function recursion).
- **Time Complexity:** $\mathcal{O}(V + E)$, where $V$ is the number of campus buildings and $E$ is the number of connecting pathways.
- **Space Complexity:** $\mathcal{O}(V)$, bounded by the recursion stack depth and the visited set.

### A* Search Algorithm
- **Paradigm:** Informed (Heuristic) Best-First Search.
- **Evaluation Function:**
  $$f(n) = g(n) + h(n)$$
  - $g(n)$: Exact path cost from the origin to node $n$.
  - $h(n)$: Estimated cost from node $n$ to the goal.
  - $f(n)$: Projected total cost of a path passing through node $n$.
- **Heuristic Admissibility & Consistency:**
  - In a 2D Euclidean coordinate plane, straight-line distance is $h(n) = \sqrt{(x_{\text{goal}} - x_n)^2 + (y_{\text{goal}} - y_n)^2}$.
  - Because physical walkways have distances $w(u, v) \ge \text{Euclidean}(u, v)$, the heuristic never overestimates the true remaining distance ($h(n) \le h^*(n)$). This guarantees **mathematical optimality**.
- **Data Structure:** Priority Queue (Min-Heap using Python's `heapq`) + Closed Set.
- **Time Complexity:** $\mathcal{O}(b^d)$ worst-case, pruned effectively towards $\mathcal{O}(d)$ with accurate heuristics.
- **Space Complexity:** $\mathcal{O}(b^d)$ storing generated states in memory.

---

## DFS Application: Campus Connectivity & Exploration

### Graph Representation (Adjacency List)
```python
campus_network = {
    "Main Block": ["AI & DS Lab", "Library", "Auditorium"],
    "AI & DS Lab": ["Main Block", "CSE Block", "Seminar Hall"],
    "Library": ["Main Block", "Cafeteria"],
    "CSE Block": ["AI & DS Lab", "Hostel"],
    "Auditorium": ["Main Block", "Seminar Hall"],
    "Cafeteria": ["Library", "Hostel"],
    "Seminar Hall": ["AI & DS Lab", "Auditorium"],
    "Hostel": ["CSE Block", "Cafeteria"]
}
```

### Approach
1. Begin traversal at `Main Block`.
2. Maintain an active `visited` list to record discovered buildings.
3. Recursively visit the first unvisited neighbor, diving deeper down the campus network.
4. When reaching a node with no unvisited neighbors (e.g. `Library`), backtrack to the prior decision junction.
5. Report total coverage and confirm network connectivity status.

### Sample Output
```text
=== DFS - Campus Exploration & Connectivity ===
Starting Location: Main Block

Step 1: Visiting [Main Block]
  Visited Set : ['Main Block']
  -> Branch : Main Block -> AI & DS Lab
Step 2: Visiting [AI & DS Lab]
  Visited Set : ['Main Block', 'AI & DS Lab']
  -> Branch : AI & DS Lab -> CSE Block
Step 3: Visiting [CSE Block]
  Visited Set : ['Main Block', 'AI & DS Lab', 'CSE Block']
  -> Branch : CSE Block -> Hostel
Step 4: Visiting [Hostel]
  Visited Set : ['Main Block', 'AI & DS Lab', 'CSE Block', 'Hostel']
  -> Branch : Hostel -> Cafeteria
Step 5: Visiting [Cafeteria]
  Visited Set : ['Main Block', 'AI & DS Lab', 'CSE Block', 'Hostel', 'Cafeteria']
  -> Branch : Cafeteria -> Library
Step 6: Visiting [Library]
  Visited Set : ['Main Block', 'AI & DS Lab', 'CSE Block', 'Hostel', 'Cafeteria', 'Library']
  <- Backtracked to : Cafeteria
  <- Backtracked to : Hostel
  <- Backtracked to : CSE Block
  <- Backtracked to : AI & DS Lab
  -> Branch : AI & DS Lab -> Seminar Hall
Step 7: Visiting [Seminar Hall]
  Visited Set : ['Main Block', 'AI & DS Lab', 'CSE Block', 'Hostel', 'Cafeteria', 'Library', 'Seminar Hall']
  -> Branch : Seminar Hall -> Auditorium
Step 8: Visiting [Auditorium]
  Visited Set : ['Main Block', 'AI & DS Lab', 'CSE Block', 'Hostel', 'Cafeteria', 'Library', 'Seminar Hall', 'Auditorium']
  <- Backtracked to : Seminar Hall
  <- Backtracked to : AI & DS Lab
  <- Backtracked to : Main Block

=== Campus Exploration Summary ===
Total Buildings Explored: 8
Traversal Order         : Main Block -> AI & DS Lab -> CSE Block -> Hostel -> Cafeteria -> Library -> Seminar Hall -> Auditorium
Network Status          : FULLY CONNECTED (All facilities reachable)
```

---

## A* Application: Shortest Path Route Navigation

### Metric 2D Coordinates & Walkway Distances
- **Campus Coordinates $(x, y)$ in meters:**
  - `Main Gate`: $(0, 0)$
  - `Parking`: $(40, 60)$
  - `Main Block`: $(120, 50)$
  - `AI & DS Block`: $(220, 80)$
  - `Library`: $(160, 160)$
  - `Auditorium`: $(280, 180)$
  - `Canteen`: $(180, 260)$
  - `Sports Ground`: $(320, 300)$
  - `Hostel`: $(240, 380)$

- **Walkway Segments:**
  - Main Gate $\leftrightarrow$ Parking: 80m
  - Main Gate $\leftrightarrow$ Main Block: 140m
  - Parking $\leftrightarrow$ Main Block: 90m
  - Main Block $\leftrightarrow$ AI & DS Block: 110m
  - Main Block $\leftrightarrow$ Library: 125m
  - AI & DS Block $\leftrightarrow$ Auditorium: 125m
  - Library $\leftrightarrow$ Auditorium: 130m
  - Library $\leftrightarrow$ Canteen: 110m
  - Auditorium $\leftrightarrow$ Sports Ground: 135m
  - Canteen $\leftrightarrow$ Sports Ground: 155m
  - Canteen $\leftrightarrow$ Hostel: 145m
  - Sports Ground $\leftrightarrow$ Hostel: 125m

### Approach
1. Enqueue origin `Main Gate` into min-heap with $f = 0 + h(\text{Main Gate})$.
2. Repeatedly extract node with lowest $f(n)$.
3. For each unvisited neighbor, compute tentative $g = g(\text{current}) + \text{walkway\_cost}$.
4. If tentative $g < g(\text{neighbor})$, update $g$-score, assign parent pointer in `came_from`, and enqueue with $f = g + h$.
5. When `Hostel` is reached, backtrack through `came_from` to reconstruct optimal route.

### Sample Output
```text
=== A* SEARCH - Campus Shortest Path ===
Start: Main Gate -> Goal: Hostel

Step 1: Expanding [Main Gate] (g=0, h=449.4, f=449.4)
  -> Added neighbor: Parking (g=80, h=377.4, f=457.4)
  -> Added neighbor: Main Block (g=140, h=351.1, f=491.1)
Step 2: Expanding [Parking] (g=80, h=377.4, f=457.4)
Step 3: Expanding [Main Block] (g=140, h=351.1, f=491.1)
  -> Added neighbor: AI & DS Block (g=250, h=300.7, f=550.7)
  -> Added neighbor: Library (g=265, h=234.1, f=499.1)
Step 4: Expanding [Library] (g=265, h=234.1, f=499.1)
  -> Added neighbor: Auditorium (g=395, h=204.0, f=599.0)
  -> Added neighbor: Canteen (g=375, h=134.2, f=509.2)
Step 5: Expanding [Canteen] (g=375, h=134.2, f=509.2)
  -> Added neighbor: Sports Ground (g=530, h=113.1, f=643.1)
  -> Added neighbor: Hostel (g=520, h=0.0, f=520.0)
Step 6: Expanding [Hostel] (g=520, h=0.0, f=520.0)
  Goal reached successfully!

=== Optimal Route Navigation ===
Shortest Path : Main Gate -> Main Block -> Library -> Canteen -> Hostel
Total Distance: 520 meters
```

---

## Project Structure

```text
algorithm-real-life-applications/
│
├── DFS/
│   └── dfs.py                  # Depth First Search campus connectivity exploration
│
├── A_Star/
│   └── a_star.py               # A* Search campus shortest path navigation
│
├── Screenshots/
│   ├── dfs_pytutor.png         # Python Tutor execution state for DFS
│   └── a_star_pytutor.png      # Python Tutor execution state for A* Search
│
├── Assignment_Report/
│   └── 25AD149_Santhosh_S.pdf  # Comprehensive academic assignment report (PDF)
│
└── README.md                   # Project documentation
```

---

## How to Run

Ensure Python 3.8+ is installed on your system. Run both programs from the repository root:

```bash
# Execute DFS Campus Exploration
python DFS/dfs.py

# Execute A* Campus Shortest Path Navigation
python A_Star/a_star.py
```

---

## Visual Demonstration

High-resolution Python Tutor execution screenshots showing code lines, active call stack frames, variable states, and terminal outputs:
- **DFS Visualization:** [`Screenshots/dfs_pytutor.png`](Screenshots/dfs_pytutor.png)
- **A* Visualization:** [`Screenshots/a_star_pytutor.png`](Screenshots/a_star_pytutor.png)

---

## Assignment Report

The full, comprehensive academic project report is available in PDF format:
- **Report Location:** [`Assignment_Report/25AD149_Santhosh_S.pdf`](Assignment_Report/25AD149_Santhosh_S.pdf)

The report includes detailed algorithmic definitions, mathematical formulation of $g(n)$, $h(n)$, and $f(n)$, Euclidean admissibility proof, step-by-step trace tables, time/space complexity derivations, Python Tutor execution logs, an 8-dimension comparative analysis, and an 8-question Viva-Voce defense guide.

---

## GitHub Repository

Official project repository:
**[https://github.com/Sant-spec/algorithm-real-life-applications](https://github.com/Sant-spec/algorithm-real-life-applications)**
