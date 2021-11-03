let variable1 = 20.3431;
const variable2 = 30.343;
const variable3 = 1 + 3;

const variable4 = "this is a string with numbers 12345";
const variable5 = 'this is a string with numbers 65672';
const variable6 = `this is a string with variable ${variable1}`;

console.log(variable6.toUpperCase());

console.log(variable2.toString());

const l = [10, 20, 30, 'un string', 'alt string', 243.1232];
l[0] = 20;
l.push('new value');
console.log(l);

const o = {
    name: 'andrei',
    country: 'ro',
    'month of birth': 'j'
};
console.log(o);
o.name = 'liviu';
o.newProperty = 'new value';
console.log(o);

function sum(n) {
    let s = 0;
    for (let i = 0; i <= n; i++) {
        s = s + i;
    }
    return s;
}

console.log(sum(10));

const func = sum;
console.log(func(10));

function sumIfCondition(n, condition) {
    let s = 0;
    for (let i = 0; i <= n; i++) {
        if (condition(i)) {
            s += i; // s = s + i;
        }
    }
    return s;
}

function isEven(n) {
    return n % 2 === 0;
}

const s1 = sumIfCondition(10, isEven);
console.log(s1);

const s2 = sumIfCondition(10, (x) => { return x % 2 === 1; });
console.log(s2);

function outerFunction(func) {
    function innerFunction() {
        console.log("Inner is on.");
        console.log(func(20));
    }
    console.log("Outer is on.");
    return innerFunction;
}

const ou = outerFunction(isEven);
ou();

o.sum = sum;
console.log(o.sum(20));