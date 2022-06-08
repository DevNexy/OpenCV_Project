# 사용자 인터페이스
# 1번 gray 필터
# 2번 RGB 필터
# 3번 HSV 필터
# 4번 Canny 엣지 필터 ->(-키 어둡게, +키 밝게)
# 5번 GaussianBlur 필터
# 6번 내가 만든 필터 (bit연산 이용)
# "m"키 실시간 얼굴 영역 모자이크
# "i"키 원본 사진

import cv2
image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/Myphoto.jpg", cv2.IMREAD_COLOR)

xml = 'C:/Users/we726/PycharmProjects/pythonProject/source/xmlFile/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml)

cv2.imshow('image', image)

while True:
    key = cv2.waitKey()

    if key == ord("i"): # i
        image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/Myphoto.jpg", cv2.IMREAD_COLOR) #원본 불러오기

    elif key == 49: #1
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #GRAY 필터
        # cv2.imshow('filter program', image)

    elif key == 50: #2
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #RGB 필터

    elif key == 51: #3
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #HSV 필터
        
    elif key == 52: #4
        image = cv2.Canny(image, 50, 100) #Canny 엣지

    elif key == 53: #5
        image = cv2.GaussianBlur(image, (0,0), 2) #GaussianBlur

    elif key == 54: #6
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #GRAY 필터
        ret, out = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY) #임계값 처리
        image = cv2.bitwise_not(out) #비트 연산 not
   
    elif key == ord("+"): #+버튼
        image += cv2.add(image, 100)  # 영상 밝게

    elif key == ord("-"): #-버튼
        image += cv2.subtract(image, 100) #영상 어둡게

    elif key == ord("m"): #m
        cap = cv2.VideoCapture(0)  #노트북 웹캠을 카메라로 사용
        cap.set(3, 640)  # 너비
        cap.set(4, 480)  # 높이i

        while (True):
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)  #좌우대칭
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.05, 5)
            if len(faces):
                for (x, y, w, h) in faces:
                    face_img = frame[y:y + h, x:x + w]  #탐지된 얼굴 이미지 crop
                    face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04)  #축소
                    face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)  #확대
                    frame[y:y + h, x:x + w] = face_img  #탐지된 얼굴 영역 모자이크 처리

            cv2.imshow('mosaic_cam', frame) #cam 불러오기i

            k = cv2.waitKey(30) & 0xff
            if k == 27:  # Esc 키를 누르면 종료
                cv2.destroyWindow('mosaic_cam') #cam 이름의 윈도우 창 닫기
                break

    elif key == 27: #ESC
        cv2.destroyWindow('filter_program')
        break

    cv2.imshow('filter_program', image)