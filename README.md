[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZUXPiV1-kVUIWXV1NPzytN4CJtumsSHE?usp=sharing)

<p align="center">
    <h1 align="center">Tic tac toe minimax Agent</h3>
</p>

## Overview
The objective of this project was to develop a tic-tac-toe 4 agent with some contraints explained below:

**1. Game rule**
    Tic-Tac-Toe 4 is a combinatorial variation on the classic Tic-tac-toe game. It is a turn-based game for two players.   
    Each player is represented with a markers: X for the first one and O for the second one.  
      
    The goal of the game is to align a sequence of 4 pieces on a grid with 12 columns and 12 rows.  
      
    The winner is the player who first aligns (horizontally, vertically or diagonally) at least four of his pieces in a row. When all the squares of the game grid are filled, if neither player has made such an alignment, the game is declared a draw.   
 
**2. Model constraints**
    - The model should be based on a Minimax algorithm with ideally an Alpha-Beta pruning
    - It is forbidden to use dictionaries of moves. All decisions must be calculated in real time

**3. Search space definition**
    I started by determining our search space to have an idea of the number of operations to perform:
    - There is 144 cases in the grid  
    - At the nth round, there is $(244-(n-1))!$ possibilities

<details open="open">
  <summary>4. Our Implementation</summary>
  <p>
    The main challenge here is not the game complexity but the extremely large search space. In order to decrease the number of nodes that are evaluated by our model I use these variants:
    - Methods for search tree length reduction:
        - alpha-beta pruning
        - maximum depth limitation
    - Method for search tree width reduction:
        - Reduce the board size when it's possible in a sub-board
    - I add an heuristic that looks at each group of adjacent marker locations in a (horizontal, vertical, or diagonal) line and assigns:
        - For diagonal alignment
            - 100000: if the agent has 4 markers in a row (the agent won),
            - 500: if the agent has 3 markers in a row,
            - 120: if the agent has 2 markers in a row,
            - 10: if the agent has 1 markers in a row,
            - -2: if the opponent has 1 markers in a row,
            - -20: if the opponent has 2 markers in a row,
            - -2000: if the opponent has 3 markers in a row,
            - -15000: if the opponent has 4 markers in a row,
        - For non-diagonal alignment
            - 100000: if the agent has 4 markers in a row (the agent won),
            - 250: if the agent has 3 markers in a row,
            - 60: if the agent has 2 markers in a row,
            - 5: if the agent has 1 markers in a row,
            - -1: if the opponent has 1 markers in a row,
            - -10: if the opponent has 2 markers in a row,
            - -800: if the opponent has 3 markers in a row,
            - -7000: if the opponent has 4 markers in a row,    
  </p>
</details>


> *“Give me six hours to chop down a tree and I will spend the first four sharpening the axe.”* - Abraham Lincoln

## Requirements
The requirements.txt file list all Python libraries that the project depends on.  
To install, use the following command:

```
pip install -r requirements.txt
```

## Getting started
There are two ways to use this project:
#### Google colab 
Simply use the link located at the top of this page  
#### Locally, on your computer  
1. Clone this repository  
2. Install the associate libraries (see requirements)
3. Two options:
    1. Open the notebook
    2. Launch the python program on your command prompt
    ```
    python path/to/cloned/repository/Tic-Tac-Toe_4.py
    ```

## Authors
Flavien DESEURE--CHARRON - flavien.deseure@gmail.com - [![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/flavien-deseure--charron/)


## References
[1] Ansaf Salleb-Aouissi. Week 4: Adversarial search, games [MOOC lecture]. In Ansaf Salleb-Aouissi, Artificial Intelligence (AI). edX. (https://www.edx.org/course/artificial-intelligence-ai)[https://www.edx.org/course/artificial-intelligence-ai]