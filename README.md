# Assignment7-JW

원티드x위코드 백엔드 프리온보딩 과제7
- 과제 출제 기업 정보
  - 기업명 : 카닥
    - [카닥 사이트](https://www.cardoc.co.kr/)

## Members
| 이름 | github                                    | 담당 기능      |
|-----|--------------------------------------------|------------ |
|박지원 |[jiwon5304](https://github.com/jiwon5304)   | 회원 생성, 타이어 정보 저장(db_upload), 회원이 소유한 타이어 저장 및 조회, 배포 |

## 과제 내용
<details>
<summary><b>과제내용 자세히 보기</b></summary>
<div markdown="1">

### **[필수 포함 사항]**
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - **서버 구조 및 디자인 패턴에 대한 개략적인 설명**
    - 완료된 시스템이 배포된 서버의 주소
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현
  
### 1. 배경 및 공통 요구사항

<aside>
😁 **카닥에서 실제로 사용하는 프레임워크를 토대로 타이어 API를 설계 및 구현합니다.**

</aside>

- 데이터베이스 환경은 별도로 제공하지 않습니다.
 **RDB중 원하는 방식을 선택**하면 되며, sqlite3 같은 별도의 설치없이 이용 가능한 in-memory DB도 좋으며, 가능하다면 Docker로 준비하셔도 됩니다.
- 단, 결과 제출 시 README.md 파일에 실행 방법을 완벽히 서술하여 DB를 포함하여 전체적인 서버를 구동하는데 문제없도록 해야합니다.
- 데이터베이스 관련처리는 raw query가 아닌 **ORM을 이용하여 구현**합니다.
- Response Codes API를 성공적으로 호출할 경우 200번 코드를 반환하고, 그 외의 경우에는 아래의 코드로 반환합니다.

| Response Code  | Description                     |
|-------|------------------------------------------|
|200 OK	|성공
|400 Bad Request	|Parameter가 잘못된 (범위, 값 등)|
|401 Unauthorized	|인증을 위한 Header가 잘못됨|
|500 Internal Server Error	|기타 서버 에러|

---

### 2. 사용자 생성 API

🎁 **요구사항**

- ID/Password로 사용자를 생성하는 API.
- 인증 토큰을 발급하고 이후의 API는 인증된 사용자만 호출할 수 있다.

```jsx
/* Request Body 예제 */

 { "id": "candycandy", "password": "ASdfdsf3232@" }
```

---

### 3. 사용자가 소유한 타이어 정보를 저장하는 API

🎁 **요구사항**

- 자동차 차종 ID(trimID)를 이용하여 사용자가 소유한 자동차 정보를 저장한다.
- 한 번에 최대 5명까지의 사용자에 대한 요청을 받을 수 있도록 해야한다. 즉 사용자 정보와 trimId 5쌍을 요청데이터로 하여금 API를 호출할 수 있다는 의미이다.

```jsx
/* Request Body 예제 */
[
  {
    "id": "candycandy",
    "trimId": 5000
  },
  {
    "id": "mylovewolkswagen",
    "trimId": 9000
  },
  {
    "id": "bmwwow",
    "trimId": 11000
  },
  {
    "id": "dreamcar",
    "trimId": 15000
  }
]
```

🔍 **상세구현 가이드**

- 자동차 정보 조회 API의 사용은 아래와 같이 5000, 9000부분에 trimId를 넘겨서 조회할 수 있다.
 **자동차 정보 조회 API 사용 예제**
  
📄 [https://dev.mycar.cardoc.co.kr/v1/trim/5000](https://dev.mycar.cardoc.co.kr/v1/trim/5000)
  
📄 [https://dev.mycar.cardoc.co.kr/v1/trim/9000](https://dev.mycar.cardoc.co.kr/v1/trim/9000)

📄 [https://dev.mycar.cardoc.co.kr/v1/trim/11000](https://dev.mycar.cardoc.co.kr/v1/trim/11000)

📄 [https://dev.mycar.cardoc.co.kr/v1/trim/15000](https://dev.mycar.cardoc.co.kr/v1/trim/15000)
  
  
- 조회된 정보에서 타이어 정보는 spec → driving → frontTire/rearTire 에서 찾을 수 있다.
- 타이어 정보는 205/75R18의 포맷이 정상이다. 205는 타이어 폭을 의미하고 75R은 편평비, 그리고 마지막 18은 휠사이즈로써 {폭}/{편평비}R{18}과 같은 구조이다.
 위와 같은 형식의 데이터일 경우만 DB에 항목별로 나누어 서로다른 Column에 저장하도록 한다.

  
### 4. 사용자가 소유한 타이어 정보 조회 API

🎁 **요구사항**

- 사용자 ID를 통해서 2번 API에서 저장한 타이어 정보를 조회할 수 있어야 한다.

</div>
</details>

## 사용 기술 및 tools
> - Back-End :  <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;
> - ETC :  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>&nbsp;


## 모델링
<p align="center"><img src="https://user-images.githubusercontent.com/80395324/143776378-79d8d576-aa18-40b1-b171-fa3694198c9b.png" width="900" height="400"/></p>



## API
- [Postman Doc](https://documenter.getpostman.com/view/17234812/UVJcjvpx)


## 내부 구조
<p align="center"><img src="https://user-images.githubusercontent.com/80395324/143780485-6a24884e-b9de-4f71-8397-7c90cf2dab8a.png" width="600" height="400"/></p>


## 구현 기능

### 사용자 생성 API
- userid 와 password 입력을 기본으로 회원가입을 진행합니다.
- userid 는 unique 설정을 하여 회원을 구별하도록 구현하였고, 암호화하여 비밀번호를 데이터베이스에 저장합니다.
- is_admin는 False를 기본으로 하며, True로 입력 시 관리자로 간주합니다.
- simple-jwt를 사용하여 토큰을 발급합니다.

### 타이어 스펙 저장 기능
- db_upload.py라는 파일을 실행시킴으로써, 조회 시 필요한 front_tire 와 rear_tire 의 폭 & 편평비 & 휠사이즈 정보만 저장하도록 구현하였습니다

### 사용자가 소유한 타이어 정보를 저장하는 API
- 회원가입 시 저장된 is_admin이라는 정보를 기준으로 관리자를 구분하여, 관리자만 정보를 저장하는 요청을 보내도록 하였습니다.
- 5개가 넘는 요청에 대해서는 에러를 반환하도록 기능을 구현하였습니다.
- 유저와 유저가 소유한 타이어의 정보가 중복으로 데이터베이스에 입력되지 않도록 기능을 구현하였습니다.
- 요청된 데이터 중 가입된 유저나 등록되어 있는 타이어가 아니면 에러를 반환하도록 기능을 구현하였습니다.
- 5개의 이하의 요청 중에서 1개라도 잘못된 요청이 들어올 시 데이터베이스에 입력되지 않도록 트랜잭션 기능을 사용하여 구현하였습니다.

### 사용자가 소유한 타이어 정보 조회 API
- 관리자가 아닌 일반 회원도 타이어 정보 조회가 가능합니다.
- 등록되지 않은 유저에 대한 정보 조회를 요청 시 에러를 반환하도록 기능을 구현하였습니다.


## 배포정보
|구분   |  정보          |비고|
|-------|----------------|----|
|배포플랫폼 | AWS EC2    |    |
|API 주소 | http://3.37.217.41:8000/ |    |



## API TEST 방법
1. 옆에 링크로 접속합니다. [Postman Doc](https://documenter.getpostman.com/view/17234812/UVJcjvpx)

2. 아래의 사진과 같이 클릭하여 이동합니다.
![image](https://user-images.githubusercontent.com/80395324/143778139-2f2a0d15-daf3-41a6-b200-c0a3c7f85fb3.png)

3. 아래의 사진과 같이 서버의 주소가 올바른지 확인 후 테스트를 진행합니다.
![image](https://user-images.githubusercontent.com/80395324/143778281-8f1f4fee-2b98-4954-b65c-6a4bc2ad60ea.png)



## 설치 및 실행 방법
### Local 개발 및 테스트용

1. 해당프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.
    ```bash
    git clone https://github.com/Wanted-Preonboarding-Backend-1st-G5/Assignment7-JW.git
    cd Assignment7-JW
    ```
    
2. 가상 환경을 생성하고 프로젝트에 사용한 python package를 받는다.
    ```bash
    conda create -n cardoc python=3.8 
    conda actvate cardoc
    pip install -r requirements.txt
    ```

3. 데이터베이스에 테이블을 생성한다.
    ```bash
    python manage.py migrate
    ```

4. 서버를 실행한다.
    ```bash
    python manage.py runserver 0:8000
    ```

## 폴더 구조
```bash
├── README.md
├── cardoc
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── db_upload.py
├── manage.py
├── my_settings.py
├── requirements.txt
├── tires
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
└── users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```


## TIL정리 (Blog)
- 


# Reference
- 이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 에서 출제한 과제를 기반으로 만들었습니다.
- 본 과제는 저작권의 보호를 받으며, 문제에 대한 정보를 배포하는 등의 행위를 금지 합니다.
