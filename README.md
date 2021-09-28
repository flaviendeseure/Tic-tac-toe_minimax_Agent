[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZUXPiV1-kVUIWXV1NPzytN4CJtumsSHE?usp=sharing)

<p align="center">
    <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
    </a>

    <h3 align="center">Tic tac toe minimax Agent</h3>

</p>

## Overview
# Tic-Tac-Toe 4 (12x12 grid)
1. Game rule  
    Tic-Tac-Toe 4 is a combinatorial variation on the classic Tic-tac-toe game. It is a turn-based game for two players.   
    Each player is represented with a markers: X for the first one and O for the second one.  
      
    The goal of the game is to align a sequence of 4 pieces on a grid with 12 columns and 12 rows.  
      
    The winner is the player who first aligns (horizontally, vertically or diagonally) at least four of his pieces in a row. When all the squares of the game grid are filled, if neither player has made such an alignment, the game is declared a draw.   
       
2. Model constraints
    - The model should be based on a Minimax algorithm with ideally an Alpha-Beta pruning
    - It is forbidden to use dictionaries of moves. All decisions must be calculated in real time

3. Search space definition 
    We started by determining our search space to have an idea of the number of operations to perform:
    - There is 144 cases in the grid  
    - At the nth round, there is $(244-(n-1))!$ possibilities
4. Our model implementation
    The main challenge here is not the game complexity but the extremely large search space. In order to decrease the number of nodes that are evaluated by our model we use these variants:
    - We implement alpha-beta pruning
    - 
> *“Give me six hours to chop down a tree and I will spend the first four sharpening the axe.”* - Abraham Lincoln

## Requirements
The requirements.txt file list all Python libraries that the project depends on.  
To install, use the following command:

```
pip install -r requirements.txt
```

## Getting started


## Authors

## References
[1] Ansaf Salleb-Aouissi. Week 4: Adversarial search, games [MOOC lecture]. In Ansaf Salleb-Aouissi, Artificial Intelligence (AI). edX. (https://www.edx.org/course/artificial-intelligence-ai)[https://www.edx.org/course/artificial-intelligence-ai]