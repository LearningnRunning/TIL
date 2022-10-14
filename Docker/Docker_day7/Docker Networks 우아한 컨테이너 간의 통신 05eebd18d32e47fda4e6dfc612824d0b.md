# Docker Networks: 우아한 컨테이너 간의 통신

Area: For DevOps
Done: No
Goal: https://www.notion.so/dd234f9fe40549af84196fef20247b37
Projects: https://www.notion.so/b05e29d012f5435397c75b85ea6d2773

# 컨테이너 네트워크 만들기

- docker network —help

```docker
docker network create NETWORK_NAME
```

## 명명한 네트워크 속에서 컨테이너 통신 하기

- 'mongodb://172.17.0.2:27017/swfavorites’
→ 'mongodb://CONTAINER_NAME:27017/swfavorites’

```docker
docker run --network NETWORK_NAME
# 예제
docker run -d --name mongodb --network favorites-net mongo
# 예제_ node
docker run --name favorites --network favorites-net -d --rm -p 3000:3000 favorites-node
```

- 컨테이너 이름을 넣어주면 컨테이너의 id를 자동으로 바꿔준다.