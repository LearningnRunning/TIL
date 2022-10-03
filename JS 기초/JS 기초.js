let grade = "F" // 변경 여지가 있는 것
const pie = 3.14  // 변하지 않는 값, 가급적 대문자


// let과 비교하여 변화가 마구 가능하다
var name
console.log(name)
name = 'Rok'
// TDZ(temporal Dead Zone)

//문자형 표시“ ”, ‘ ’, ` `
const message1  = 'I\'m JS'
const message2  = "I'm JS"
const message3 = `My name is ${name}` // 문자형 안에 변수 선언시 베티

const message3 = "My name is ${name}" // 베티를 사용하지 않으면 그냥 문자형으로 반환하니 주의

//대화상자
const name = promt("이름을 입력하세요", '디폴트값')
alert("환영합니다, "+ name + "님")
alert(`환영합니다, ${name}님`)

const isAdult = confirm("당신은 성인입니까?")
console.log(isAdult) // 확인 취소 버튼을 누르는 팝업 등장

//타입 확인 typeof
console.log(typeof "what is my type?")
//형 변환
String()
Number() // 공백도 해준다
Boolean()

//연산자
// 덧셈
let num = 10;
let result = ++num;
//논리연산자
const age = prompt('나이가?')
const gender = prompt('성별은?')
const isAge = age > 19;
const isGender = gender == '남성';

if(isAge && isGender){
  console.log('성인 남성입니다.')
}else{
    console.log('미성년자입니다.')
}


//조건문
//if
const age = 10
if (age > 19){
    console.log('환영 합니다')
}else if(age == 19 ){
    console.log('1년 뒤!')
}else{
    console.log('미성년자입니다.')
}


//반복문
//for
for(let i = 0; i < 10; i++){
    console.log(i)
}

//while
let i = 0;
while (i < 10){
    console.log(i)
		i++;
}

//do while
let i = 0;
do{
    console.log(i)
		i++;
}while (i < 10)

//switch 문
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

//function
function sayHello(name){
	console.log(`Hello, ${name}`);
}

function sayHello(name){

  const msg = `Hello, ${name}`
  alert('환영합니다.')
	console.log(msg);
}

sayHello('성록')

function sayHello(name){
  let msg = `Hello`
  if (name){
    msg += `, ${name}`
  }

	console.log(msg);
}

function sayLikeAnton(name){
  let newName = name || 'friendo';
  let msg = `What do you care where I come from, ${newName}?`
	console.log(msg);
}

sayLikeAnton('sir')
//-> "What do you care where I come from, sir?"
sayLikeAnton()
//-> "What do you care where I come from, friendo?"

// 호스팅스
sayLikeAnton() // 함수 선언 전 호출

function sayLikeAnton(name){
  let newName = name || 'friendo';
  let msg = `What do you care where I come from, ${newName}?`
	console.log(msg);
}

sayLikeAnton('sir')

/* -> "What do you care where I come from, friendo?"
	 "What do you care where I come from, sir?" */


// 함수 표현식
sayLikeAnton('sir') // 함수표현식은 호이스팅 집단에 들어가지 않아 오류

let sayLikeAnton = function(name){
  let newName = name || 'friendo';
  let msg = `What do you care where I come from, ${newName}?`
	console.log(msg);
}

sayLikeAnton('sir')


// 화살표 함수
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

// Object
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


//단축 프로퍼티
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
//-> true
'birthDay' in myObject;
//-> false
myObject.age;
//-> true

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
//-> false
// 만약 !('age' in user) 이걸 같이 연산 안 해주면 true 값이 나온다.
// if문으로 들어가지 않기 때문이다.

// 반복문 사용해서
const Choi = {
    name : 'Choi',
    age : 31
};

for(x in Choi){
    console.log(Choi[x]) // Choi['name']
}


// method: 객체 프로퍼티로 할당된 함수
const myObject = {
    name : 'Rok',
    age : 31,
    fly(){ // fly : function(){  생략 가능
        console.log(`Hello, ${this.name}`) // this
    }
}

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


// 배열
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

//반복문 활용
// 인덱스 활용
for (let idx = 0; idx < days.length; idx++){
    console.log(days[idx])
}

// 바로 꺼내기
for (let day of days){
    console.log(day)
}