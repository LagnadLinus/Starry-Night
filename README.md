# Starry Night

A Python Turtle Graphics Project by Sunil Dangal

## Overview
The **Starry Night** project is a simulation of a starry night sky using Python's Turtle Graphics and randomness. In this project, stars are randomly generated with varying sizes and positions against a dark background to create the effect of a cosmic sky. 

## Project Objectives
1. **Create Random Stars**: Stars are placed randomly on the screen to mimic a natural night sky.
2. **Use Random Library**: The `random` library is used to vary the size and position of each star.
3. **Use Looping**: A `for` loop is implemented to generate a large number of stars for a fuller sky effect.

## Design
The design phase involves creating diagrams, flowcharts, and pseudocode:
- **Diagram**: Illustrates a dark background with scattered stars.
- **Flowchart**: Lays out the logic flow for star generation and positioning.
- **Pseudocode**: Used to map out steps before coding.

## Implementation
The project is implemented across two files:
- `starry_night.py`: Initial code with basic star generation.
- `final_starry_Night_project.py`: Complete implementation, including additional features like a moon, background color adjustments, and more stars.

### Key Features
1. **Moon**: Adds a moon to the scene for added visual interest.
2. **Dynamic Backgrounds**: Different background colors to simulate dusk or dawn.
3. **Increased Star Count**: A higher star count makes the sky look richer and more complete.

## Troubleshooting
### Common Bug
- **Non-integer argument for `randrange()`**: If you encounter this error, it is due to a non-integer argument in `randrange()` when the window dimensions are odd numbers. To fix, round the width and height values:
  ```python
  x = randrange(round(-width/2), round(width/2))
  y = randrange(round(-height/2), round(height/2))

**Evaluation**

This project successfully demonstrates the creation of a starry night sky using Turtle Graphics, with randomized star sizes and positions for a natural appearance. The loop-based implementation creates an engaging visual, and additional features like the moon enhance the aesthetic of the scene.

**Getting Started**

1. Clone this repository.
2. Run final_starry_Night_project.py to view the completed Starry Night project.

**Author**
Created by Sunil Dangal.
