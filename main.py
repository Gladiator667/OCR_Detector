import detector
import fileExplorer
import screenshot
import cv2
import sys

print("Choose what you want?")
print("1: Take a screenshot")
print("2: Upload a file")
i = int(input())

if i == 1:
    filepath = screenshot.screenshot_path()
    detector.detect_text(filepath=filepath)
    print("PRESS 0 TO EXIT")
    if cv2.waitKey(0) or 0xff == ord('e'):
        sys.exit()
elif i == 2:
    filepath = fileExplorer.file_path()
    detector.detect_text(filepath=filepath)
    if cv2.waitKey(0) or 0xff == ord('e'):
        sys.exit()
else:
    print("INVALID INPUT. PLEASE TRY AGAIN.......")
    sys.exit()
