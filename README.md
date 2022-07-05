# OpenCV_Project
## 2022-1 OpenCV final project
## (2022-1 영상처리 프로그래밍 기말 프로젝트)
---
## <개요>
* 프로젝트 주제 : 다양한 필터 프로그램
* 활용목적   
오늘날 우리는 사진을 찍기 위해 또는 사진을 찍은 후 다양한 필터를 사진에 적용한다.   
예를 들어, 유라이크, 스노우와 같은 앱이나 인스타그램 필터들 중 감성적인 필터, 웃긴 필터 등이 있다.   
많은 사용자들이 있고, 관심있어 하는 부분이기에 해당 주제를 선택하게 되었다.   
영상처리 프로그래밍 수업에서 배운 다양한 필터링 기법으로 나만의 사진 필터 프로그램을 만들고자 했다.   
* 초기 계획 
<img src="https://user-images.githubusercontent.com/92451281/172602927-600b566e-fe6f-4981-94eb-7270657c3174.png" width="50%" height="50%">

* 개발   
초기 계획을 참고하여, 사진에는 6가지 필터를 적용하였고,   
"m"키를 누를 시 카메라가 켜지게 되는데,    
이때 실시간으로 얼굴을 인식하여 모자이크 처리를 할 수 있도록 만들었다.   

---
## <사용자 인터페이스 및 프로그램에 사용한 필터>
* 숫자키
  * 1 : gray 필터
  * 2 : RGB 필터
  * 3 : HSV 필터
  * 4 : Canny 엣지 필터 -> ('-'키 : 어둡게, '+'키 : 밝게)
  * 5 : GaussianBlur 필터
  * 6 : bit 연산 not을 이용한 나만의 필터
* 영문키
  * 'i'키 : 원본 필터 (중첩으로 필터가 적용되는 것을 방지)
  * 'm'키 : 실시간 얼굴 영역 모자이크

---
## <핵심 코드 설명>

먼저 Key를 이용하여 필터를 바꾸는 이벤트 처리 코드이다.
이미지에 대하여 6가지의 필터가 적용되도록 구현하였다.
```py
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
```
이미지의 밝기를 조절해 주는 코드이다. Canny 엣지 필터에만 적용이 된다.
```py
    elif key == ord("+"): #+버튼
        image += cv2.add(image, 100)  # 영상 밝게

    elif key == ord("-"): #-버튼
        image += cv2.subtract(image, 100) #영상 어둡게
```
'm'키를 누르면 노트북 웹캠을 카메라로 사용하여 실시간 얼굴영역 모자이크처리를 하는 코드이다.   
먼저 얼굴을 인식할 수 있는 haarcascade_frontalface_default.xml를 다운받아 불러온 뒤,   
웹캠이 켜지면 카메라를 통해 프레임을 읽어온다.   
그 후, 탐지된 얼굴 이미지의 크기를 가져와서 모자이크 영역을 계산하면 얼굴에 모자이크가 나타나게 된다.   
```py
    elif key == ord("m"): #m
        cap = cv2.VideoCapture(0)  #노트북 웹캠을 카메라로 사용
        cap.set(3, 640)  # 너비
        cap.set(4, 480)  # 높이

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

            cv2.imshow('mosaic_cam', frame) #cam 불러오기

            k = cv2.waitKey(30) & 0xff
            if k == 27:  # Esc 키를 누르면 종료
                cv2.destroyWindow('mosaic_cam') #cam 이름의 윈도우 창 닫기
                break
```
---
## <스크린 샷>

* 사용한 원본 이미지 및 'i'키
<img src="https://user-images.githubusercontent.com/92451281/172604447-fe0e99df-2cb9-4486-9806-357ad6520a4f.png" width="50%" height="50%">

* 1번 : gray 필터
<img src="https://user-images.githubusercontent.com/92451281/172605545-4a0c8e91-8af9-41c8-88cd-42f975a5e540.png" width="50%" height="50%">

* 2번 : RGB 필터
<img src="https://user-images.githubusercontent.com/92451281/172605652-52771963-70f3-47f2-9938-c1d81e2525e8.png" width="50%" height="50%">

* 3번 : HSV 필터
<img src="https://user-images.githubusercontent.com/92451281/172606378-479962b0-b7fa-46f3-a028-4942c3555f29.png" width="50%" height="50%">

* 4번 : canny 엣지 필터
<img src="https://user-images.githubusercontent.com/92451281/172606445-62587ada-23a5-4203-a9ec-091076aa9188.png" width="50%" height="50%">

* 5번 : GaussianBlur 필터
<img src="https://user-images.githubusercontent.com/92451281/172606516-8648b3bf-ba42-4636-bb1c-ca9fbb4bdbe3.png" width="50%" height="50%">

* 6번 : bit_not을 이용한 나만의 필터
<img src="https://user-images.githubusercontent.com/92451281/172606579-8f19de7c-2d62-4b5a-81a0-4f5dc0aa7961.png" width="50%" height="50%">

* 'm'키 : 실시간 얼굴영역 모자이크
<img src="https://user-images.githubusercontent.com/92451281/172606628-d4e30277-46c8-4b36-adc8-a648979ff780.png" width="50%" height="50%">

* '-'키 : 밝기 낮춤
<img src="https://user-images.githubusercontent.com/92451281/172606700-a06b2580-a779-4b81-84d1-fb0ecb5cd508.png" width="50%" height="50%">

* '+'키 : 밝기 높임
<img src="https://user-images.githubusercontent.com/92451281/172606770-9fc4709a-57a9-4ff6-b0ca-48e937df5991.png" width="50%" height="50%">
