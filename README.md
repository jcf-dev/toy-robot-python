# Toy Robot Python

## Project Setup

1. Install Poetry https://python-poetry.org/docs/#installation
2. Run `poetry install` to install project dependencies into a Poetry virtual environment.

## Running The Program
Go to the root of the project and run `python3 main.py` on Linux/Mac or `python main.py` on Windows.

## Commands
- `PLACE X,Y,F` - Place the robot on a specific coordinate. 
  - `X` (integer) - Location on x-axis 
  - `Y` (integer) - Location on y-axis
  - `F` (string) - Direction of the robot, possible values: `NORTH`, `SOUTH`, `WEST`, or `EAST`
  - Example `PLACE 0,0,NORTH` (please note the whitespaces)
- `MOVE` - Will move the robot 1-step to the direction it is facing.
- `RIGHT` - Will rotate the robot's face direction 90° to the right
- `LEFT` -  Will rotate the robot's face direction 90° to the left
- `REPORT` - Will return the robot's last coordinate and direction. Also quits then program