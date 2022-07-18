import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def detect_text(filepath: str)-> None:
    img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print("WE ARE DETECTING. PLEASE WAIT............")
    # hImg, wImg = img.shape
    boxes = pytesseract.image_to_data(img)
    print("PRESS 0 TO EXIT")
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w+x, h+y), (0,255,50), 2)
                cv2.putText(img, b[11], (x, y+50), cv2.FONT_HERSHEY_PLAIN, 0.95, (17, 17, 237), 2)

    cv2.imshow('Result', img)
    cv2.waitKey(0)