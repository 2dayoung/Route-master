# Route Master
#### 고객의 주소 데이터를 받아와 ‘소요시간 or 거리’를 가중치로 두어 최단경로 찾아주어 효율적인 택배배송을 위한 프로그램   
  
</br>

### 사용언어 
- #### C++ or Python
- #### Node.js
- #### html
- #### JavaScript

</br>

## 계획
### 1. 고객의 주소 데이터 확보 
### 2. DB 저장
### 3. 네이버 API 이용
 - #### 주소 위도 경도로 변환
 - #### 위도 경도 바뀐값으로 소요시간 구함
 - #### 주소위치 마커로 표시
### 4. Dijkstra 알고리즘 이용 하여 최단거리 구함 - 가중치 : 소요시간
### 5. 구한 경로 사용자에게 웹 사이트구성하여 제공

</br>

## To Do
1. 고객의 주소 데이터 어떻게 할것인지 
2. 네이버API공부 
(10/11)
- 네이버 클라우드 플랫폼 가입
- application등록 이름 (Route-master)
- 성공 :    
    * get_taketime.py -> 소요시간 구하기  
        출발지에서 목적지까지 378990m 거리이며, 약 16161101분 소요됩니다. 
    * get_latlon.py -> 주소가지고 경도 위도 구하기   
        주소: 충청북도 청주시 서원구 모충로 32
        경도: 127.4677057, 위도: 36.6242653

3. 웹페이지 구성하는법 공부 (Node.js)
4. 

## How to 
1단계로 실제 존재하는 인프라(도로)를 바탕으로 길찾기 문제를 풀어보고, 2단계로 택배 물품을 2개 이상 받았을 때 어떤 순서대로 물품을 배송하면 좋을지


https://yermi.tistory.com/category/%E2%96%A3%20Tools/API%F0%9F%8E%AF?page=1


네이버 맵 가이드
https://navermaps.github.io/maps.js.ncp/docs/naver.maps.html  
https://navermaps.github.io/maps.js.ncp/docs/naver.maps.Map.html#toc4__anchor  

마커찍기
https://lpla.tistory.com/132
# 2023.10.12   
nodejs파일 추가 

모듈 설치   
$ npm install morgan  

$ npm install cookie-parser  

$ npm install express-session  

$ npm install express  
-node_modules/ 폴더 생성 

$ npm install -D nodemon 
-이제 $npm nodemon 하면 중간에 파일 수정해도 변경 사항이 반영됨 

**실행방법**

$ npx nodemon 파일이름.js

- index.html 에 지도 띄우기 만들고 map_site.js로 실행


**계획**  
1. 마커찍기  
    var marker   
    - 맵 가운데도 지정하고 위도 경도 바꿔야함 
    충북대학교 
    (36.629449717767436,127.45769316147752)

2. 왼쪽에 지도 띄우기

    \<div id="map" style="left:100px;width:50\%;height:600px;">  
\</div>
left,right,width,height 가 있고 px,\%가 있다.

3. 오른쪽에 리스트 띄우기 

4. 주소를 받아와서 웹사이트에 넣으면 리스트나 DB에 저장 
- 주소를 일단 임의로 저장하고 딕셔너리를 활용해서 주소랑 좌표를 알기 쉽게 정리해서 보여줄 수 있도록  -> 일단 딕셔너리이용해서 각 주소pair 간에 소요시간이랑 거리 구해서 나타냄 
- 혹은 json이용?

5. 주소 위도경도로 바꿈
- 성공 
6. 바뀐 위도경도로 driving이용해서 소요시간 계산
- 성공 

    문제점 - 모듈 이용해서 각각 함수 가져와서 test파일에서 get_latlon의 address_to_coordinates로 좌표 변환한거 리스트에 넣고 get_taketime의 get_travel_time 써서 거리랑 소요시간 구함. 거리는 m 소요시간은 ms(millisecond(1/1000초)) 

        # 밀리초를 초로 변환
        seconds = milliseconds / 1000

        # 초를 분과 초로 변환
        minutes = seconds // 60  # 분
        remaining_seconds = seconds \% 60  # 초

        이용해서 분 초 로 바꿈 
        
        start_location=coordinate_list[0]
        destination_location=coordinate_list[1] 
        이 자기 맘대로 들어가는듯. -> coordinate_list부터 맘대로 들어가는거임.

        -> 이유 : address_list가 []이 아니라 {}이었음..


7. 소요시간 Dijkstra 알고리즘

Q. python에서 데이터를 어떻게 js에 넣는가?  
A. 1. json형식 사용
2. RESTful API 
3. 데이터베이스 사용


+ 소방서 위치  

청주서부소방서,충청북도 청주시 흥덕구 가경동 1508-2
청주동부소방서,충청북도 청주시 상당구 영운로 61


+ 주소 예시 

충청북도 청주시 서원구 사창동 367-7
충청북도 청주시 서원구 1순환로680번길 13-11
충청북도 청주시 서원구 모충로3번길 26
충청북도 청주시 서원구 내수동로 140
충청북도 청주시 서원구 창직로31번길 12-1  
address_list={충청북도 청주시 서원구 사창동 367-7,
충청북도 청주시 서원구 1순환로680번길 13-11,
충청북도 청주시 서원구 모충로3번길 26,
충청북도 청주시 서원구 내수동로 140,
충청북도 청주시 서원구 창직로31번길 12-1}


Q.파이썬 파일 간에 데이터 교류법  
A.모듈이용 
    

    import data_module

    data = data_module.get_shared_data()
    print(data)




