let variable1 = 1021.213445;
const variable2 = 20.345;
const variable3 = 1 + 2;


console.log(variable3);
variable1 = variable1 + variable2;

const variable4 = "this is a string quotes";
const variable5 = 'this is a string quotes';
const variable6 = `this is a string with quoutes a value ${variable1}`;

const l = [1, 2, 3, 4, "hello", "how are you"];
l.push(10);
l.pop();

l[0] = 10;
console.log(l[3]);
console.log(l);

const o = {
    name: 'andrei',
    country: 'ro',
    'month of birth': 'june'
}

o.name = 'liviu'
o['month of birth'] = 'j'
console.log(o);

o.newProperty = 'new value';
console.log(o);

function sum(n) {
    let s = 0;
    for (let i = 0; i <= n; i++) {
        s = s + i;
    }
    return s;
}

const s = sum(10);
console.log(s);

const sumVariable = sum;
console.log(sumVariable(10));

function sumIfCondition(n, condition) {
    let s = 0;
    for (let i = 0; i <= n; i++) {
        if (condition(i) === true) {
            s = s + i;
        }
    }
    return s;
}

function isEven(n) {
    return n % 2 === 0;
}

const s2 = sumIfCondition(10, isEven);
console.log(s2);

// () => {}
const s3 = sumIfCondition(10, (x) => { return x % 2 === 1 });
console.log(s3);

function outsideFunc() {
    function insideFunc() {
        console.log('Inside is on.');
    }
    console.log('Outside is on.');
    return insideFunc;
}

const func = outsideFunc();
func();
o.sum = sumIfCondition;
o.condition = isEven;

console.log(o.sum(20, o.condition));

console.log(10 != '10');
console.log(10 !== '10');