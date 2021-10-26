console.log("Test");

let variable1 = 10;
const variable2 = 20;

let camelCaseStyle = "test";

// a == b; a === b 
console.log(1 == "1");
console.log(1 === "1");

// a != b; a !== b
console.log(1 !== "1");
console.log(1 != "1");

// >, < >=, <= 

// !a (not a)

// +, -, *, / 
console.log("Addition:", variable1 + variable2);
console.log("Exp 1:", variable2 * 10 / variable1);

let variable3 = variable1 === variable2;
console.log("Comparsion result: ", variable3);

console.log('' == false);
console.log('a' == false);

function add(p1, p2) {
    const sum = p1 + p2;
    return sum;
}

let addition1 = add(20, 20);
console.log(addition1);

const f = (p1, p2) => {
    const product = p1 * p2;
    return product;
}
let prod = f(2, 2);
console.log(prod);

if (variable2 === 10) {
    console.log("Variable2 is 10");
} else if (variable2 === 20) {
    console.log("Variable2 is 20");
} else {
    console.log("Unknown variable2 value");
}

// switch 
// for 
let s = 0;
for (let i = 0; i < 10; i++) {
    s = s + i;
}
console.log(s);

// while
while (s > 0) {
    console.log("Current value for s is: ", s);
    s = s - 1;
}

