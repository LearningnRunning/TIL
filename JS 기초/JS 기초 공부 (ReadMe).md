# JS κΈ°μ΄ κ³΅λΆ

Priority: High π₯
Status: Completed
λ¬μ±λ₯ : π¦΄π¦΄π¦΄π¦΄π¦΄π¦΄π¦΄π¦΄π¦΄π¦΄ 100%
λͺ©ν: 17
μλ£: 17

### μ°Έμ‘°ν κ°μ: μ½λ©μλ§μ **[μλ°μ€ν¬λ¦½νΈ κΈ°μ΄ κ°μ’ : 100λΆ μμ±](https://www.youtube.com/watch?v=KF6t61yuPCY)**

```jsx
alert()

**console.log()
```

## λ³μ μ μΈ

### let, const, var

```jsx
let grade = "F" // λ³κ²½ μ¬μ§κ° μλ κ²
const pie = 3.14  // λ³νμ§ μλ κ°, κ°κΈμ  λλ¬Έμ

 
// letκ³Ό λΉκ΅νμ¬ λ³νκ° λ§κ΅¬ κ°λ₯νλ€
var name
console.log(name)
name = 'Rok'
// TDZ(temporal Dead Zone) 
```

### μ€μ½ν κ΅¬λ³

- ν¨μ μ€μ½ν: var(function μΈμ if, while λ±λ± μμ μ μ­λ³μμ²λΌ)
- λΈλ‘ μ€μ½ν: let, const

### λ³μμ μμ±κ³Όμ 

1. μ μΈ λ¨κ³
2. μ΄κΈ°ν λ¨κ³
3. ν λΉ λ¨κ³
- var λ 1,2 λ₯Ό νλ²μ νλ€.(λ€λ§, ν λΉμ΄ μλμ΄ undefined)
- const 1,2,3μ νλ²μ νλ€.

## μλ£ν

### λ¬Έμν νμβ β, β β, ` `

```jsx
const message1  = 'I\'m JS'
const message2  = "I'm JS"
const message3 = `My name is ${name}` // λ¬Έμν μμ λ³μ μ μΈμ λ² ν°

Error
const message3 = "My name is ${name}" // λ² ν°λ₯Ό μ¬μ©νμ§ μμΌλ©΄ κ·Έλ₯ λ¬ΈμνμΌλ‘ λ°ννλ μ£Όμ
```

## null vs undefined

- null : λΉ κ°
- undefined : κ°μ΄ ν λΉλμ΄ μμ§ μλ€

## λνμμ

- alert μλ €μ€λ€
- prompt μλ ₯ λ°λλ€ (Pythonμμ input)
- confirm νμΈ λ°λλ€

```jsx
const name = promt("μ΄λ¦μ μλ ₯νμΈμ", 'λν΄νΈκ°')
alert("νμν©λλ€, "+ name + "λ") 
alert(`νμν©λλ€, ${name}λ`)
```

```jsx
const isAdult = confirm("λΉμ μ μ±μΈμλκΉ?")
console.log(isAdult) // νμΈ μ·¨μ λ²νΌμ λλ₯΄λ νμ λ±μ₯

```

## νμ νμΈ typeof

- λ¨ nullμ κ°μ²΄ νμμΌλ‘ μΈμνλ€.

```jsx
console.log(typeof "what is my type?")
```

### νλ³ν

```jsx
String()
Number() // κ³΅λ°±λ ν΄μ€λ€
Boolean()
```

## μ°μ°μ

### λ§μ

```jsx
let num = 10;
let result = ++num;
```

## μ‘°κ±΄λ¬Έ

### IF

```jsx
const age = 10
if (age > 19){
    console.log('νμ ν©λλ€')
}else if(age == 19 ){
    console.log('1λ λ€!')
}else{
    console.log('λ―Έμ±λμμλλ€.')
}
```

### λΌλ¦¬ μ°μ°μ

```jsx
const age = prompt('λμ΄κ°?')
const gender = prompt('μ±λ³μ?')
const isAge = age > 19;
const isGender = gender == 'λ¨μ±';

if(isAge && isGender){
  console.log('μ±μΈ λ¨μ±μλλ€.')
}else{
    console.log('λ―Έμ±λμμλλ€.')
}
```

## λ°λ³΅λ¬Έ

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

### do while(μ‘°κ±΄μ λ€λ‘ λλ whileλ¬Έ)

```jsx
let i = 0;
do{
    console.log(i)
		i++;
}while (i < 10)
```

### break, continue

- break: λ§λλ μ¦μ λ°λ³΅λ¬Έ νμΆ
- continue: ν΄λΉ λ°λ³΅λ§ μ ννκ³  κ³μ μ§ν

### switch λ¬Έ

```jsx
let fruit = prompt('λ¬΄μ¨ κ³ΌμΌμ μ¬κ³  μΆλμ?')

switch (fruit){
    case 'μ¬κ³Ό' :
        console.log('100μ μλλ€.');
        break;
    case 'λ°λλ' :
        console.log('200μ μλλ€.');
        break;
    case 'ν€μ' :
        console.log('300μ μλλ€.');
        break;
    case 'μ¨μλ μλ°': //μ‘°κ±΄
    case 'μλ°' :
        console.log('500μ μλλ€.');
        break;
    default : //elseλ κ°λ€
        console.log('κ·Έλ° κ³ΌμΌμ μμ΅λλ€.');
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
  alert('νμν©λλ€.')
	console.log(msg);
}

sayHello('μ±λ‘')
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

### νΈμ΄μ€ν

- JSλ μΈν°νλ¦¬ν° μΈμ΄μ΄μ§λ§ ν¨μ μ μΈ μμͺ½μ ν¨μ νΈμΆμ΄ μμ΄λ μ€λ₯ μμ΄ μ μ²λ¦¬νλ€.
- κ·Έ μ΄μ λ μ μ²΄ μ½λμμ ν¨μμ½λλ§ λ―Έλ¦¬ μμ±ν΄λκΈ° λλ¬Έμ κ°λ₯ν©λλ€, μ¦ νΈμ΄μ€ν λλΆμ΄λ€.

```jsx
sayLikeAnton() // ν¨μ μ μΈ μ  νΈμΆ

function sayLikeAnton(name){
  let newName = name || 'friendo';
  let msg = `What do you care where I come from, ${newName}?`
	console.log(msg);
}

sayLikeAnton('sir')

-> "What do you care where I come from, friendo?"
	 "What do you care where I come from, sir?"
```

## ν¨μ ννμ

- ν¨μλ₯Ό λ³μ μ μΈνλ― μ¬μ©νλ€.
- κ·Έλ₯ ν¨μμ λ€λ₯Ό λ°κ° μμ§λ§ ν¨μ ννμμ νΈμ΄μ€νμ΄ λμ§ μκΈ°μ ν΄λΉ λΌμΈμ λλ¬νλ©΄ ν¨μ μμ±μ΄ λλ€.

```jsx
sayLikeAnton('sir') // ν¨μννμμ νΈμ΄μ€ν μ§λ¨μ λ€μ΄κ°μ§ μμ μ€λ₯

let sayLikeAnton = function(name){
  let newName = name || 'friendo';
  let msg = `What do you care where I come from, ${newName}?`
	console.log(msg);
}

sayLikeAnton('sir')
```

### νμ΄ν ν¨μ

```jsx
// ν¨μννμ
let add = function(num1, num2){
  return num1 + num2;
}

// νμ΄ν ν¨μ
let add = (num1, num2) => {
  return num1 + num2;
}

// νμ΄ν ν¨μ_ λ¦¬ν΄λ¬Έμ΄μΌ λ
// κ΄νΈλ‘ λ¦¬ν΄κ³Ό μ€κ΄νΈ λμ²΄ κ°λ₯
const add = (num1, num2) => (
	num1 + num2
	);

// νμ΄ν ν¨μ_ λ¦¬ν΄λ¬Έμ΄μΌ λ
// κ΅¬νμ½λ, λ¦¬ν΄ λͺ¨λ ν μ€ μΌλ κ΄νΈλ μλ΅ κ°λ₯
const add = (num1, num2) => num1 + num2;

// νμ΄ν ν¨μ_ νλΌλ©ν°κ° νλμΌ λ
// κ΄νΈ μλ΅ κ°λ₯
const twice= num1 => num1*2;

// μΈμκ° μλ κ²½μ° μλ΅ λΆκ°λ₯
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

//μ κ·Ό
myObject.name
// λλ
myObject['name']

// μΆκ°
myObject.name = 'choi';
myObject['hairColor'] = 'black'; // κ΄νΈλ λ§μ°¬κ°μ§λ‘ κ°λ₯

//μ­μ 
delete myObject.hairColor;
```

### λ¨μΆ νλ‘νΌν°

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

// μΈμ νμΈ
'age' in myObject;
-> true
'birthDay' in myObject;
-> false
myObject.age;
-> true

// μμ© 
function isAdult(user) {
    if(!('age' in user) || // userμ ageκ° μκ±°λ
        user.age < 20){ // 20μ΄ λ―Έλ§ μ΄λ©΄
        return false;
    }  
    return true;
}

const Choi = {
    name : 'Choi'
};

console.log(isAdult(Choi))
-> false
// λ§μ½ !('age' in user) μ΄κ±Έ κ°μ΄ μ°μ° μ ν΄μ£Όλ©΄ true κ°μ΄ λμ¨λ€.
// ifλ¬ΈμΌλ‘ λ€μ΄κ°μ§ μκΈ° λλ¬Έμ΄λ€.
```

### λ°λ³΅λ¬Έ μ¬μ©

```jsx
const Choi = {
    name : 'Choi',
    age : 31
};

for(x in Choi){
    console.log(Choi[x]) // Choi['name']
}
```

## method: κ°μ²΄ νλ‘νΌν°λ‘ ν λΉλ ν¨μ

```jsx
const myObject = {
    name : 'Rok',
    age : 31,
    fly(){ // fly : function(){  μλ΅ κ°λ₯ 
        console.log(`Hello, ${this.name}`) // this
    }
}
```

```jsx
let myObject = {
    name : 'Rok',
    age : 31,
    fly(){ // fly : function(){  μλ΅ κ°λ₯ 
        console.log(`Hello, ${this.name}`)
    }
};

let myObjec2 = myObject;
myObjec2.name = 'Choi';

console.log(myObjec2.name)
```

## λ°°μ΄

```jsx
let days = ['μ','ν','μ']

// λ€μμ μΆκ°
days.push('λͺ©')
//λ€μμ μ κ±°
days.pop()

// μμμ μΆκ°
days.unshift('μΌ')
days.unshift('μΌ','μ','μ') // μ¬λ¬ κ° κ°λ₯
// λ€μμ μ κ±°
days.shift();

//λ³κ²½
days[1] = 'νμμΌ'

// κΈΈμ΄
console.log(days.length) 
```

### λ°λ³΅λ¬Έ νμ©

```jsx
// μΈλ±μ€ νμ©
for (let idx = 0; idx < days.length; idx++){
    console.log(days[idx])
}

// λ°λ‘ κΊΌλ΄κΈ°
for (let day of days){
    console.log(day)
}
```

### λ€μ λͺ©ν κ°μ: μ½λ©μλ§μ **[μλ°μ€ν¬λ¦½νΈ μ€κΈ κ°μ’ : 140λΆ μμ±](https://www.youtube.com/watch?v=4_WLS9Lj6n4)**