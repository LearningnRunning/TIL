# Imaged, Containers & Volumes

Area: For DevOps
Done: Yes
Goal: https://www.notion.so/dd234f9fe40549af84196fef20247b37
Projects: https://www.notion.so/478b74083bc54a9bb91e1b9a1e511c84

# Volumes

```docker
#볼륨 확인
docker volume ls
```

## Volumes(Managed by Docker)

- 컨테이너 내부와 로컬 컴퓨터를 잇는 저장소
- 컨테이너가 중지, 삭제되어도 Volume은 남아있다.
- 호스트머신에서의 저장 위치 파악이 힘든다

### anonymous Volume

- 익명이기에 컨테이너가 존재하는 동안만 실존한다.
- 사용하지 않는 익명 볼륨 삭제 방법

```docker

# 저정 삭제
docker volume rm VOL_NAME
# 전체 삭제
docker volume prune
```

### named Volume

- 컨테이너가 종료되어도 계속 살아있다.
- named Volume 만드는 법
    - Dockerfile 내부에서 named Volume를 만들 수 없기 때문에 도커 파일내 Volume 명령어는 제거한다
    - Volume 명명어가 없는 도커파일을 build 한다
    
    ```docker
    docker build -t feedback-node:volumes .
    # feedback-node이름:volumes태그
    ```
    
    - 컨테이너를 실행할 때 Volume의 경로와 이름을 명명한다
    
    ```docker
    docker run -p 3000:80 -d --name feedback-app --rm -v feedback:/app/feedback feedback-node:volumes
    # 로컬 3000번 포트로 도커포트 80과 연결
    # 컨테이너 이름은 feedback-app
    # 종료되는 동시 삭제 --rm
    # 볼륨의 이름:볼륨 폴더 경로
    # 기반 이미지 이름 feedback-node:volumes
    ```
    
    - 컨테이너가 삭제되어도 볼륨은 살아있는 것을 확인할 수 있다(docker volume ls)
    - 삭제 했다가 다시 살려도 여전히 남아있다.

## Bind Mounts(Managed by you)

- 호스트머신에서의 위치를 알 수 있다

### 설치 방법

- 컨테이너에만 영향을 주기에 Dockerfile에서 만들 수 없다

```docker
$ docker run -p 3000:80 -d --name feedback-app --rm -v feedback:/app/feedback -v "D:\GitHub\TIL\Docker/Docker_day5:/app" feedback-node:volumes
# 마운트볼륨을 위해 -v "D:\GitHub\TIL\Docker/Docker_day5:/app" 명령어로 볼륨을 추가했다. 
# 로컬에 없는 경로라면 볼륨의 이름으로 취급되어 명명된 볼륨이 된다
# 절대경로를 써줘야한다.
# 다만 절대 경로가 아닌 바로가게끔 설정도 가능하다
```

### ****바로 가기(Shortcuts)****

- 항상 전체 경로를 복사하여 사용하고 싶지 않은 경우, 다음 바로 가기를 사용할 수 있다

```docker
#macOS / Linux
-v $(pwd):/app

#Windows: 
-v "%cd%":/app
```

## 볼륨끼리의 결합과 병합

- 예시 코드 중에 npm install 로 생겨나는 node_module 폴더를 컨테이너 내부 볼륨으로 생성해서 충독을 막는다

```docker
docker run -d -p 3000:80 --name feedback-app -v feedback:/app/feedback -v "D:/GitHub/TIL/Docker/Docker_day5:/app" -v /app/node_modules feedback-node:volumes
# 마지막에 추가한 node_modules 볼륨
-v /app/node_modules feedback-node:volumes
```

<aside>
🚫 Error: Cannot find module 'express’
→ npm install express 로 해결

</aside>

# 컨테이너 가동 중에서도 코드 수정하기

## NodeJS 특화 조정_#54

- server.js 가 변경 될 때마다 컨테이너를 종료 시켰다가 다시 시행할 순 없다!
- nodemon 패키지로 server.js 시행시킬 수 있게 종속성 추가

```docker
# package.json 파일에서 
"scripts": {
    "start": "nodemon server.js"
},
"dependencies" : {
	~
},
"devDependencies" : {
	"nodemon"
}
```

```docker
# 방금 추가한 스크립트를 통해 서버를 제어하기 위해 Dockerfile를 수정해준다.
CMD ["npm", "start"]
```

| 종류 | Anonymous Volume | Named Volume | Bind Mount |
| --- | --- | --- | --- |
| 생성 명령어 예시 -v  | /app/data
VOLUME [”/app/data”] | data:/app/data | /로컬경로:/app/code |
| 특징 | - 컨테이너가 제거되면 자동 삭제
- 컨테이너 간의 교류 안 됨
- 다른 모듈에 의해 덮어쓰여지는 것을 방지하는데 유용함
- 호스트머신에 폴더를 생성하므로  | - 컨테이너를 제거해도 살아남아 있음
- 컨테이너 간의 데이터 공유 가능
 | - 데이터가 저장되는 위치를 알 수 있음
- 네임드 볼륨이 가진 모든 장점을 가지고 있음 |

# 퀴즈

### "볼륨"이란 무엇인가요? (Docker로 작업할 때)

컨테이너 외부의 특정 폴더를 연결된 내부의 폴더 및 파일

### '바인드 마운트'란 무엇인가요?

특정한 호스트 머신 상의 경로이며, 우리가 알 수 있음. 일부 컨테이너 내부 경로에 매핑됨

### **'바인드 마운트'의 일반적인 사용 사례는 무엇인가요?**

**컨테이너에 '라이브 데이터'를 제공하려고 합니다 (리빌드할 필요 없음).**

### **익명 볼륨은 쓸모 없는 걸까요?**

 **아니요, 외부 경로보다 컨테이너 내부 경로의 우선 순위를 높이는 데 사용할 수 있습니다.**