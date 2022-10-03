# JS 기초 공부

Priority: High 🔥
Status: Completed
달성률: 🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴 100%
목표: 17
완료: 17

### 참조한 강의: 코딩악마의 **[자바스크립트 기초 강좌 : 100분 완성](https://www.youtube.com/watch?v=KF6t61yuPCY)**

```jsx
alert()

**console.log()
```

## 변수 선언

### let, const, var

```jsx
let grade = "F" // 변경 여지가 있는 것
const pie = 3.14  // 변하지 않는 값, 가급적 대문자

 
// let과 비교하여 변화가 마구 가능하다
var name
console.log(name)
name = 'Rok'
// TDZ(temporal Dead Zone) 
```

### 스코프 구별

- 함수 스코프: var(function 외에 if, while 등등 에서 전역변수처럼)
- 블록 스코프: let, const

### 변수의 생성과정

1. 선언 단계
2. 초기화 단계
3. 할당 단계
- var 는 1,2 를 한번에 한다.(다만, 할당이 안되어 undefined)
- const 1,2,3을 한번에 한다.

## 자료형

### 문자형 표시“ ”, ‘ ’, ` `

```jsx
const message1  = 'I\'m JS'
const message2  = "I'm JS"
const message3 = `My name is ${name}` // 문자형 안에 변수 선언시 베티

Error
const message3 = "My name is ${name}" // 베티를 사용하지 않으면 그냥 문자형으로 반환하니 주의
```

## null vs undefined

- null : 빈 값
- undefined : 값이 할당되어 있지 않다

## 대화상자

- alert 알려준다
- prompt 입력 받는다 (Python에서 input)
- confirm 확인 받는다

```jsx
const name = promt("이름을 입력하세요", '디폴트값')
alert("환영합니다, "+ name + "님") 
alert(`환영합니다, ${name}님`)
```

```jsx
const isAdult = confirm("당신은 성인입니까?")
console.log(isAdult) // 확인 취소 버튼을 누르는 팝업 등장

```

## 타입 확인 typeof

- 단 null을 객체 타입으로 인식한다.

```jsx
console.log(typeof "what is my type?")
```

### 형변환

```jsx
String()
Number() // 공백도 해준다
Boolean()
```

## 연산자

### 덧셈

```jsx
let num = 10;
let result = ++num;
```

## 조건문

### IF

```jsx
const age = 10
if (age > 19){
    console.log('환영 합니다')
}else if(age == 19 ){
    console.log('1년 뒤!')
}else{
    console.log('미성년자입니다.')
}
```

### 논리 연산자

```jsx
const age = prompt('나이가?')
const gender = prompt('성별은?')
const isAge = age > 19;
const isGender = gender == '남성';

if(isAge && isGender){
  console.log('성인 남성입니다.')
}else{
    console.log('미성년자입니다.')
}
```

## 반복문

### for

```jsx
for(let i = 0; i < 10; i++){
    console.log(i)
}
```

### while

```jsx
let i = 0;
while (i < 10){
    console.log(i)
		i++;
}
```

### do while(조건을 뒤로 두는 while문)

```jsx
let i = 0;
do{
    console.log(i)
		i++;
}while (i < 10)
```

### break, continue

- break: 만나는 즉시 반복문 탈출
- continue: 해당 반복만 점프하고 계속 진행

### switch 문

```jsx
let fruit = prompt('무슨 과일을 사고 싶나요?')

switch (fruit){
    case '사과' :
        console.log('100원 입니다.');
        break;
    case '바나나' :
        console.log('200원 입니다.');
        break;
    case '키위' :
        console.log('300원 입니다.');
        break;
    case '씨없는 수박': //조건
    case '수박' :
        console.log('500원 입니다.');
        break;
    default : //else랑 같다
        console.log('그런 과일은 없습니다.');
}
```

## function

```jsx
function sayHello(name){
	console.log(`Hello, ${name}`);
}
```

```jsx
function sayHello(name){

  const msg = `Hello, ${name}`
  alert('환영합니다.')
	console.log(msg);
}

sayHello('성록')
```

```jsx
function sayHello(name){
  let msg = `Hello`
  if (name){
    msg += `, ${name}`
  }

	console.log(msg);
}
```

```jsx
function sayLikeAnton(name){
  let newName = name || 'friendo';
  let msg = `What do you care where I come from, ${newName}?`
	console.log(msg);
}

sayLikeAnton('sir')
-> "What do you care where I come from, sir?"
sayLikeAnton()
-> "What do you care where I come from, friendo?"
```

### 호이스팅

- JS는 인터프리터 언어이지만 함수 선언 위쪽에 함수 호출이 있어도 오류 없이 잘 처리한다.
- 그 이유는 전체 코드에서 함수코드만 미리 생성해놓기 때문에 가능합니다, 즉 호이스팅 덕분이다.

```jsx
sayLikeAnton() // 함수 선언 전 호출

function sayLikeAnton(name){
  let newName = name || 'friendo';
  let msg = `What do you care where I come from, ${newName}?`
	console.log(msg);
}

sayLikeAnton('sir')

-> "What do you care where I come from, friendo?"
	 "What do you care where I come from, sir?"
```

## 함수 표현식

- 함수를 변수 선언하듯 사용한다.
- 그냥 함수와 다를 바가 없지만 함수 표현식은 호이스팅이 되지 않기에 해당 라인에 도달하면 함수 생성이 된다.

```jsx
sayLikeAnton('sir') // 함수표현식은 호이스팅 집단에 들어가지 않아 오류

let sayLikeAnton = function(name){
  let newName = name || 'friendo';
  let msg = `What do you care where I come from, ${newName}?`
	console.log(msg);
}

sayLikeAnton('sir')
```

### 화살표 함수

```jsx
// 함수표현식
let add = function(num1, num2){
  return num1 + num2;
}

// 화살표 함수
let add = (num1, num2) => {
  return num1 + num2;
}

// 화살표 함수_ 리턴문이일 때
// 괄호로 리턴과 중괄호 대체 가능
const add = (num1, num2) => (
	num1 + num2
	);

// 화살표 함수_ 리턴문이일 때
// 구현코드, 리턴 모두 한 줄 일때 괄호도 생략 가능
const add = (num1, num2) => num1 + num2;

// 화살표 함수_ 파라메터가 하나일 때
// 괄호 생략 가능
const twice= num1 => num1*2;

// 인수가 없는 경우 생략 불가능
const showError = () => {
	alert('error!')
};
```

# Object

```jsx
const myObject ={
    name : 'Rok',
    age : 31
}

//접근
myObject.name
// 또는
myObject['name']

// 추가
myObject.name = 'choi';
myObject['hairColor'] = 'black'; // 괄호도 마찬가지로 가능

//삭제
delete myObject.hairColor;
```

### 단축 프로퍼티

```jsx
function makeObject(name, age){
    return{
        name,
        age,
        hobby : 'football'
    };
}

const Rok = makeObject('Rok',31);
console.log(Rok)

// 인자 확인
'age' in myObject;
-> true
'birthDay' in myObject;
-> false
myObject.age;
-> true

// 응용 
function isAdult(user) {
    if(!('age' in user) || // user에 age가 없거나
        user.age < 20){ // 20살 미만 이면
        return false;
    }  
    return true;
}

const Choi = {
    name : 'Choi'
};

console.log(isAdult(Choi))
-> false
// 만약 !('age' in user) 이걸 같이 연산 안 해주면 true 값이 나온다.
// if문으로 들어가지 않기 때문이다.
```

### 반복문 사용

```jsx
const Choi = {
    name : 'Choi',
    age : 31
};

for(x in Choi){
    console.log(Choi[x]) // Choi['name']
}
```

## method: 객체 프로퍼티로 할당된 함수

```jsx
const myObject = {
    name : 'Rok',
    age : 31,
    fly(){ // fly : function(){  생략 가능 
        console.log(`Hello, ${this.name}`) // this
    }
}
```

```jsx
let myObject = {
    name : 'Rok',
    age : 31,
    fly(){ // fly : function(){  생략 가능 
        console.log(`Hello, ${this.name}`)
    }
};

let myObjec2 = myObject;
myObjec2.name = 'Choi';

console.log(myObjec2.name)
```

## 배열

```jsx
let days = ['월','화','수']

// 뒤에서 추가
days.push('목')
//뒤에서 제거
days.pop()

// 앞에서 추가
days.unshift('일')
days.unshift('일','월','수') // 여러 개 가능
// 뒤에서 제거
days.shift();

//변경
days[1] = '화요일'

// 길이
console.log(days.length) 
```

### 반복문 활용

```jsx
// 인덱스 활용
for (let idx = 0; idx < days.length; idx++){
    console.log(days[idx])
}

// 바로 꺼내기
for (let day of days){
    console.log(day)
}
```

### 다음 목표 강의: 코딩악마의 **[자바스크립트 중급 강좌 : 140분 완성](https://www.youtube.com/watch?v=4_WLS9Lj6n4)**