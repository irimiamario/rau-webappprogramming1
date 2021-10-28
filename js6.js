document.writeln("This is inside a script.");

let variable1 = 1 + 2 + 3;
const variable2 = 3.4323;
console.log(variable1);
variable1 = 8;
console.log(variable1);

const variable3 = "this is a string. u49u24fm.";
const variable4 = 'this is a string. 34;l-431-';
const variable5 = `this is a string with a variable ${variable1} continue`;
const variable6 = 'this is a string with a variable ' + variable1.toString() + " continue";

console.log(variable3);
console.log(variable4);
console.log(variable5.toUpperCase());
console.log(variable6);

const l = [1, 'sda', 3, '32r', 5, 6, 'anr', 'daret', 'sdad']
l[3] = 'rjkj';
l.push(1034);
console.log(l);

const o = {
    name: 'andrei',
    country: 'ro',
    'month of birth': 'j'
};
console.log(o);
o.name = "liviu";
o.newProperty = 'new value';
console.log(o);

/*
&& ||
>
<
== --> compara valoarea --> 10 = '10'
=== --> compara tip si valoare --> 10 != '10'
!= 
!==
*/

function product(a, b) {
    return a * b;
}

function sum(a, b) {
    return a + b;
}

console.log(product(10, 20));

const productName = product;
console.log(productName(2, 2));

const funcs = [sum, product];
let variable10 = 0;
for (const func of funcs) {
    variable10 = variable10 + func(10, 20);
}
console.log(variable10);

function productIfCondition(a, b, condition) {
    if (condition(a, b)) {
        return a * b;
    }
    else {
        return 1;
    }
}

function areEven(a, b) {
    let aIsEven = undefined;
    if (a % 2 === 0) {
        aIsEven = true;
    } else {
        aIsEven = false;
    }
    let bIsEven = undefined;
    if (b % 2 === 0) {
        bIsEven = true;
    } else {
        bIsEven = false;
    }
    let bothEven = undefined;
    if (aIsEven === true && bIsEven === true) {
        bothEven = true;
    } else {
        bothEven = false;
    }
    return bothEven;
}

console.log(areEven(10, 21));


