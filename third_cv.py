import cv2
import sys
cap=cv2.VideoCapture("../assets/video.mp4")
if not cap.isOpened():
    sys.exit("파일없음")
captures=[]
while True:
    ret,frame=cap.read()
    if ret:
        cv2.imshow("비디오",frame)
        key=cv2.waitKey(1)
        if key == ord('c'):
            captures.append(frame)
            print(f"{captures}")
        elif key == ord('q'):
            break
    else:
        break

cap.release()

cv2.destroyAllWindows()
if len(captures)>0:
    for i,capture in enumerate(captures):
        cv2.imwrite(f"./outputs/frame_{i}.jpg",capture)