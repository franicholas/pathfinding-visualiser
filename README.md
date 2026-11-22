# A* Pathfinding Visualiser

A Python-based pathfinding visualiser built using Pygame. The application allows users to create a grid, place obstacles, choose a starting point and destination, and watch different pathfinding algorithms search for a route.

The project implements Breadth-First Search (BFS) and A, allowing their behaviour and performance to be explored visually.

## Motivation

I wanted to build a project that would let me explore algorithms beyond implementing them for coursework. Having studied algorithms and data structures, I wanted to understand more deeply how they behave when applied to a practical problem.

Pathfinding interested me because it brings together graph theory, data structures and algorithmic efficiency. I decided to build a visualiser so I could see how algorithms such as BFS and A* explore a search space, compare their behaviour, and understand how the choice of heuristic affects the search.

My goal was to create something interactive that demonstrates not only that an algorithm works, but also why it works and what trade-offs it makes.

## Features

- Interactive grid with configurable start and goal positions
- Ability to place and remove obstacles
- Breadth-First Search (BFS) pathfinding
- A* pathfinding using Manhattan distance as its heuristic
- Animated visualisation of explored cells and the resulting path
- Statistics displaying path length, explored cells and execution time

## Technologies

- Python
- Pygame

## Controls

| Input | Action |
|---|---|
| Left-click | Place or remove a wall |
| Right-click | Set the starting position |
| Middle-click | Set the goal position |
| B | Run Breadth-First Search |
| A | Run A* |
| R | Reset the grid |

## Algorithms

### Breadth-First Search (BFS)

BFS explores the grid using a queue, processing cells in the order they are discovered.

Because every movement has the same cost, BFS guarantees a shortest path when one exists.

### A* Search

A* uses the evaluation function:

\[
f(n) = g(n) + h(n)
\]

Where:
- \(g(n)\) is the actual cost from the starting position to the current cell.
- \(h(n)\) is the estimated cost from the current cell to the goal.

This project uses Manhattan distance as its heuristic, which is suitable for movement in four directions on a grid.

A* uses this estimate to guide its search towards the goal while still finding an optimal path under these movement conditions.

## Performance Comparison

The application displays the path length, number of explored cells and execution time for each algorithm.

This allows the algorithms to be compared on the same grid and demonstrates how heuristic information can influence the search process.

## Installation and Running

1. Clone the repository:

   ```bash
   git clone https://github.com/franicholas/pathfinding-visualiser.git
   cd pathfinding-visualiser
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   **Windows PowerShell:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## What I Learned

Through this project, I developed a practical understanding of graph traversal and informed search algorithms. I also gained experience with:

- Implementing BFS and A* from scratch
- Using data structures such as queues, sets and dictionaries
- Applying heuristic functions to guide search
- Visualising algorithm behaviour using Pygame
- Measuring and comparing algorithm execution time
