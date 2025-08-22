# Snake_Water_Gun_Game
🐍💧🔫 Snake-Water-Gun Game

This is a simple Python implementation of the Snake-Water-Gun game (similar to Rock-Paper-Scissors).
The game is played between a user and the computer.

🎮 Game Rules

Snake (0) drinks Water (1) → Snake wins.

Water (1) douses Gun (2) → Water wins.

Gun (2) kills Snake (0) → Gun wins.

If both choose the same option → Draw.

⚙️ How it Works

The computer randomly selects a choice (Snake, Water, or Gun).

The user inputs their choice:

0 → Snake 🐍

1 → Water 💧

2 → Gun 🔫

The program compares both choices using game rules.

Result is displayed: Win, Lose, or Draw.

📝 Example Run
0 for Snake, 1 for Water, 2 for Gun
1
User = 1
Computer = 0
You Lose

🚀 How to Run

Make sure Python 3 is installed.

Save the code in a file, e.g., snake_water_gun.py.

Run the program:

python snake_water_gun.py

🔧 Known Issues

There’s a typo in your code:

comp = random.randiant(0,2)  # ❌ wrong
comp = random.randint(0,2)   # ✅ correct


The check() function currently only handles losing conditions.
You can extend it to return 1 when the user wins.
