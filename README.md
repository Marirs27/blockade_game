# **Blockade**

### **What is it?**
**Blockade** is a 2D game inspired by the classic **Tetris**, developed using **Python** and the **Pygame** library.  
Tetris, originally created in 1984, is a tile-matching puzzle game where players manipulate falling blocks (tetrominoes) to form complete rows, which are then cleared. In this project, I recreated the core mechanics of Tetris, adding my own logic and implementation for rotation, block placement, and gameplay.

---

### **The Assignment and Implementation**
The goal of this project was to develop a fully functional Tetris-like game using Python. I utilized the **Pygame** library for rendering, handling inputs, and managing the game loop.

**Key Mechanics and Features**:
1. **Block Rotation**: Implemented block rotations using custom mathematical formulas derived from logical patterns (detailed below).
2. **Gameplay Flow**: Blocks fall in real-time, and players can rotate or move them horizontally to fit them into rows.
3. **Row Clearing**: Complete rows are detected and cleared, earning points for the player.
4. **Game Over Condition**: The game ends when blocks stack to the top of the screen.

---

### **Installation Requirements and Instructions**

#### **Requirements**:
- Python 3.7 or higher
- Pygame library

#### **Instructions**:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Marirs27/blockade_game.git
   cd blockade
2. **Install Dependencies**: Install Pygame using pip if it's not already installed:
   ```bash
   pip install pygame
3. **Run the Game**: Execute the game script:
   ```bash
   python blockade.py
   
### **Block Rotation Logic**
The rotation of blocks (tetrominoes) was a key challenge in implementing the game. I derived mathematical formulas to determine how blocks should rotate while staying within the grid.

Here is an image illustrating the logic and formulas behind the block rotation:
![Rotation_logic](https://github.com/user-attachments/assets/cc322933-2297-495f-be96-47f62bb4c382)

### **Demo of the Game**
Here is a short snippet of the game in action:

https://github.com/user-attachments/assets/f1832b18-1fa5-46a2-90ee-aae9453cc522

### **Future Enhancements**
There is potential to expand the game further with additional features, such as:
1. **New Game Modes**: Adding time challenges, survival mode, or multiplayer options.
2. **Enhanced Graphics**: Improving visuals with animations, particle effects, and better UI design.
3. **Customizable Controls**: Allowing players to remap controls to their preferences.
4. **Sound Effects and Music**: Integrating background music and sound effects for a richer gaming experience.
5. **High Score System**: Implementing a leaderboard to track top scores.

### **Credits**
- Developed by: **Sriram Kannan**
- Tools Used: Python, Pygame
