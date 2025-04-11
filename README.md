# Car Mechanic Simulator 2021 - Automate scrapping

This script automates the scrapping mini-game in CMS 21, utilizing screenshot libraries (pyautogui and mss) and image processing (OpenCV)

### Prerequisites
- Python 3.x
- Game must be running in windowed mode (not minimized)
- Supported resolutions: 1920x1080 or 2560x1440

### Installation

1. Clone the repo
```
git clone https://github.com/vanillashake17/cms21scrapping.git
```   

2. Install the required libraries:
```
pip install pyautogui opencv-python numpy keyboard pygetwindow mss
```

3. Navigate to the correct resolution folder:
```
cd .\cms21scrapping\1920by1080\
```
or
```
cd .\cms21scrapping\2560by1440\
```
4. Make sure you are in the mini-game before starting the script as shown below
   
![Image](https://github.com/user-attachments/assets/1d9697af-ac52-4d27-af67-5d4825f44705)

5. Run the script:
```
python main.py
```

### Stopping the Script

There are two ways to stop the script:
- **Round Limit**: You can set a limit for the desired number of rounds on line 46 of the script.
- **Killswitch**: Press the designated killswitch key (defaults to right-alt) to terminate the script. This can be changed to any valid key on line 55.

## Video demo on a 2560 * 1440 screen

![Video](https://github.com/user-attachments/assets/5d41ec24-8482-4477-96a1-7a54c19cd544)
