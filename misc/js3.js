const variable1 = 10;
const variable2 = 12345.6533;
const variable3 = "this is a string";
const variable4 = 'this is a string';
const variable5 = `this is a string with a value ${variable3}`;

const variable6 = 1 + 2;

let variable7 = 20;
variable7 = 1000;

const l = [1, "string", 2, "123", 1.233, {}];
l[0] = 10;
console.log(l[0]);
l.push(1000);
l.pop();

const o = {
    name: 'andrei',
    country: 'romania'
};
console.log(o);
o.name = 'liviu';
o.surname = 'luchici';
console.log(o);

const a = 10;
const b = "10";
if (a === b) {
    console.log("Same data!");
} else if (a > 9) {
    console.log("a > 9");
} else {
    console.log("Different data");
}

function product(a, b) {
    const p = a * b;
    return p;
}

function factorial(n) {
    let p = 1;
    for (let i = 1; i <= n; i++) {
        p = p * i;
    }
    return p;
}

let prod = product(10, 20);
console.log("Product of 10 & 20 = ", prod);
const fact = factorial(10);
console.log("10! = ", fact);

while (prod > 190) {
    console.log(prod);
    prod = prod - 1;
}

const f = function newFunction (x) {
    return x * x;
}
const g = (x) => {
    return x * x;
}

console.log(f(10));

function sumIfCondition(n, func) {
    let s = 0;
    for (let i = 1; i <= n; i++) {
        if (func(i) === true) {
            s = s + i;
        }
    }
    return s;
}

function isEven(x) {
    return x % 2 === 0;
}

const s1 = sumIfCondition(21, (x) => { return x > 20 });
console.log(s1);

const s2 = sumIfCondition(100, isEven);
console.log(s2);

function log() {
    function innerLog() {
        console.log("inner function called.");
    }
    console.log('outer function called');
    return innerLog;
}

const lg = log();
lg();