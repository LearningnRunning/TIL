# Using Arguments & Environment Variables

Area: For DevOps
Done: Yes
Goal: https://www.notion.so/dd234f9fe40549af84196fef20247b37
Projects: https://www.notion.so/478b74083bc54a9bb91e1b9a1e511c84

# 인수와 환경변수

![Untitled](Using%20Arguments%20&%20Environment%20Variables/Untitled.png)

```jsx
# server.js 파일 수정
app.listen(80);
->  app.listen(process.env.PORT);
```

```docker
# COPY 밑에 기본값을 설정
ENV PORT(환경변수이름=key) 80(value) 

EXPOSE $PORT
```

```docker
docker run -d -p 3000:80 --env PORT=8000  --name feedback-app -v feedback:/app/feedback -v "D:/GitHub/TIL/Docker/Docker_day5:/app:ro" -v /app/temp -v /app/node_modules feedback-node:env
# 이미지를 리빌드하지 않고도 포트를 재설정할 수 있다. 
# --env PORT=8000 추가했다
```

### .env 파일로 포트번호 관리

- .env 파일에 PORT=8000 키 밸류 쌍을 입력해 놓고

```docker
docker run -d -p 3000:80 --env-file ./.env --name feedback-app -v feedback:/app/feedback -v "D:/GitHub/TIL/Docker/Docker_day5:/app:ro" -v /app/temp -v /app/node_modules feedback-node:env
# 포트 번호를 따로 수정할 것 없이
# --env-file ./.env 넣어주면 .env 파일 내에서 수정 가능하다
```

### **환경 변수 & 보안**

**환경 변수 및 보안**에 대한 한 가지 중요한 참고사항: 환경 변수에 저장하는 데이터의 종류에 따라, 보안 데이터를 `Dockerfile`에 직접 포함하고 싶지 않을 수도 있습니다.
그 대신 런타임에만 사용되는 별도의 환경 변수 파일로 이동시키죠. (즉, `Docker run`으로 컨테이너를 실행할 때).
그렇지 않으면, 값이 '이미지에 포함'되며, 모든 이가 'docker history <이미지>'를 통해, 이 값을 읽을 수 있습니다.
일부 값의 경우, 이것이 중요하지 않을 수도 있지만, 자격 증명, 개인 키 등의 경우에는 확실히 피해야만 합니다!
별도의 파일을 사용하는 경우, '`docker run`'을 실행할 때 그 파일을 가리키므로, 그 값은 이미지의 일부분이 아닙니다. 하지만 소스 컨트롤을 사용하는 경우, 별도의 파일을 소스 컨트롤 저장소의 일부분으로 커밋하지 않도록 조심하세요.

## 빌드 인수(ARG) 사용하기

```docker
# Dockerfile

ARG DEFAULT_PORT=80

ENV PORT $DEFAULT_PORT

```

- 빌드할 때 인수로 포트 변경하기
- --build-arg DEFAULT_PORT=8000

```docker
docker build -t feedback-node:dev --build-arg DEFAULT_PORT=8000 .
```