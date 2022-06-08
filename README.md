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
