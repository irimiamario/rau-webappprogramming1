let variable1 = 10;
const variable2 = 20.23;
const variable3 = "acesta este un string";
const variable4 = 'acesta este un string';
const variable5 = `string cu valori ${variable1}`;
const variable6 = [1, 2, 3, 4, 5, 6, 7, 8];
variable6.push(9);
variable6.push(10);
const variable7 = {
    name: 'andrei',
    country: 'romania',
    'month of birth': 'june'
};
variable7.country = 'ro';

console.log(variable7);
if (variable7.name === 'andrei') {
    variable7.surname = 'luchici';
} else {
    variable7.surname = 'unknown';
}
console.log(variable7);

function sumNumbersUpToN(n) {
    let s = 0;
    for (let i = 0; i <= n; i++) {
        s = s + i;
    }
    return s;
}

const sum = sumNumbersUpToN(10);
console.log(sum);

let n = 14;
while (n > 10) {
    console.log(n);
    n = n - 1;
}

const f = sumNumbersUpToN;
console.log(f(20));

const fs = [f, f, f];
for (let i = 0; i < fs.length; i++) {
    console.log('sum',i, fs[i](120));
}

function sumNumbers(n, f) {
    return f(n);
}

function returnFunction(n) {
    const f = function fi() {
        console.log('Apelat din interiorul functiei', n);
    }
    return f;
}
console.log('sum', sumNumbers(10, sumNumbersUpToN));

const a = returnFunction(10);
a();