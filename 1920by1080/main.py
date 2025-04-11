import pyautogui # type: ignore
import time # type: ignore
import mss
import mss.tools
import cv2
import numpy as np 
import keyboard
import pygetwindow as gw

#navigate to the game window
cms21 = gw.getWindowsWithTitle('Car Mechanic Simulator 2021')
cms21[0].activate()

time.sleep(2)

# locate the gamebar on the screen
barregion = pyautogui.locateOnScreen('gamebar.png', confidence=0.8)
if barregion is None:
    print("Error: Could not find gamebar.png on the screen.")
    exit(1)

#define region for mss capture
bar_region_mss = {'top': barregion.top, 'left': barregion.left, 'width': barregion.width, 'height': barregion.height}

#coords of the top left corner of the barregion relative to the screen
bar_offset_x = barregion.left
bar_offset_y = barregion.top 

print("Game start, moving cursor.....")
pyautogui.press('space') # starts the game

is_round_active = True 
locate_cyanblock = True

arrowimg = cv2.imread('arrow.png',cv2.IMREAD_GRAYSCALE) #convert to grayscale
if arrowimg is None:
    print("Error: Could not read arrow2.png")
    exit(1)
aH,aW = arrowimg.shape[:2]

bigbonusimg = cv2.imread('bigbonus2.png',cv2.IMREAD_GRAYSCALE) #convert to grayscale

print("\nStarting real-time arrow tracking. Press R-Alt to quit")
print("-" * 30)
round_no = 0 #tracks the current round number
limit = 30  #how many rounds we want
success = 0 #how manu times we hit the cyanblock
count = 0   #how many iterations it took to complete the round
with mss.mss() as sct:
    try:
        while True:
            time_start = time.time()
            count += 1
            # --- Check for exit key ---
            if keyboard.is_pressed('right alt') or round_no >= limit:
                print("\nExiting loop.")
                break
            
            if is_round_active:
                # Locate cyanblock once a round
                if locate_cyanblock: 
                    cyanblock = pyautogui.locateOnScreen('cyanblock.png', region=barregion, confidence=0.8) 
                    target_x_start = cyanblock.left # left edge of the cyanblock
                    target_x_end = cyanblock.left + cyanblock.width
                    print(f"Bar is between X = {target_x_start} and X = {target_x_end}")
                    locate_cyanblock = False 
                

                img_bgr = np.array(sct.grab(bar_region_mss)) # use mss to capture in real time

                if img_bgr.shape[2] == 4: # remove alpha channel if present
                    img_bgr = cv2.cvtColor(img_bgr, cv2.COLOR_BGRA2BGR)

                img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY) # convert to grayscale

                result = cv2.matchTemplate(img_gray, arrowimg, cv2.TM_CCOEFF_NORMED) # find the arrow in the image
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) # max_loc is the top-left corner of the best match. It returns in the form of (x,y)
                time_end = time.time()
                time_taken = time_end - time_start
                #print(f"{time_taken*1000} ms") 
                if max_val >= 0.85:
                    arrow_relative_x = max_loc[0] # arrow_relative_x is the x coordinate of the arrow with respect to the left edge of the barregion
                    arrow_coords = bar_offset_x + arrow_relative_x + (aW//2)  # Center of the arrow in screen coordinates
        
                    text_to_print = f"Arrow Found at X={arrow_coords}"
                    print(f"{text_to_print:<23}", end='\r', flush=True) # print the x coordinate of the arrow

                    if target_x_start<= arrow_coords <= target_x_end : 
                        # arrow is within the target zone and we are allowed to press space
                            pyautogui.press('space')
                            time.sleep(0.3)
                            #determind if we hit the cyanblock
                            im1 = pyautogui.screenshot()
                            im1 = np.array(im1) 
                            im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY) 
                            result = cv2.matchTemplate(im1, bigbonusimg, cv2.TM_CCOEFF_NORMED) 
                            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) 
                            print() 
                            if max_val >= 0.85:
                                print("Hit")
                                success += 1
                                
                            else:
                                print("No Hit")        

                            is_round_active = False
                            round_no += 1
                            print(f"Round {round_no} completed. Hit {success} out of {round_no}. Success rate: {float(success)/float(round_no):.2%}")
                            #print (f"{count} iterations required for round {round_no}")
                            print("Waiting for next round...")
                            count = 0
                        
            else:
                time.sleep(0.7)
            
                print("-" *20)
                print("Pressing space to start next round")
                try:
                    pyautogui.press('space')
                    is_round_active = True  
                    locate_cyanblock = True
                except Exception as e:
                    print(f"Error pressing space: {e}")
                    break


    finally:
        print("\nExiting...")
