import cv2

capture=cv2.VideoCapture(0)  #0은 내장 이후1~##
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)

while True:
    ret,frame1=capture.read()    #ret에는 카메라가 정상 작동하면 True 작동하지 않을경우 false를 반환
    cv2.imshow('frame',frame1)
    if cv2.waitKey(1)==ord('q'):          #cv2.waitkey(time) time이 0일경우 지속적으로 검사하여 프레임이 넘어가지 않음
        break

capture.release()               #카메라 장치에서 받아온 메모리를 해제
cv2.destroyAllWindows()         # 모든 윈도우창을 닫는다.

# cv2.destroyAllWindows('이름')   특정 이름의 창만 닫을 수 있다.