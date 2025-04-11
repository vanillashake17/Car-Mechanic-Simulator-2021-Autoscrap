# Car Mechanic Simulator 2021 - Automate scrapping

This script automates the scrapping mini-game in CMS 21, utilizing screenshot libraries (pyautogui and mss) and image processing (OpenCV)

### Prerequisites
- Python 3.x
- Game must be running in windowed mode (not minimized)
- Supported resolutions: 1920x1080 or 2560x1440

### Installation

1. Install the required libraries:
```
pip install pyautogui opencv-python numpy keyboard pygetwindow mss
```

2. Navigate to the correct resolution folder:
```
cd .\1920by1080\
```
or
```
cd .\2560by1440\
```
3. Make sure you are in the mini-game as shown below
```
![Image](https://github.com/user-attachments/assets/1d9697af-ac52-4d27-af67-5d4825f44705)
```
4. Run the script:
```
python main.py
```

## Usage

The script will run in the background while your game is open. It uses computer vision to detect targets and automate actions.

### Stopping the Script

There are two ways to stop the script:
- **Round Limit**: You can set a limit for the desired number of rounds on line 46 of the script.
- **Killswitch**: Press the designated killswitch key (defaults to right-alt) to terminate the script. This can be changed to any valid key on line 55.

## Performance Statistics

The script was tested for 50 rounds, three separate times:

| Attempt | Hits | Total | Success Rate |
|---------|------|-------|-------------|
| First   | 48   | 50    | 96.00%      |
| Second  | 50   | 50    | 100.00%     |
| Third   | 49   | 50    | 98.00%      |

Average success rate: 98.00%
