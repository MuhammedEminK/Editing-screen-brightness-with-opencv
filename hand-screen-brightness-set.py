
import mediapipe as mp
import cv2
import screen_brightness_control as sbc

mpHands = mp.solutions.hands
Hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)
pTime = 0
while True:
    T, frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hands = Hands.process(imgRGB)
    
    if hands.multi_hand_landmarks:
        for handLms in hands.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                if id == 8:
                    cv2.circle(frame, (cx,cy), 3, (255,0,255), cv2.FILLED)
                    
                    x = (cx *100) / w
                    x = 100 - x
                    sbc.set_brightness(x)
    cv2.imshow("hand", frame)
    cv2.waitKey(1)
     