// document.write("Hello everyone! Welcome to my page.");
// document.write("This is my second line");
// // alert("Hellooooo!");
// document.write(variable1);

const l = [1, 2, 23, 3, 5, 6, 7, "string"];

const a = 1120;
if (a === 10) {
    // document.write("a = 10");
} else if (a === 1120) {
    // document.write("a = 1120");
} else {
    // document.write("a != 10");
}

// for 
for (let i = 0; i < 10; i++) {
    // document.write(i);
}

// while 
let b = 10;
while (b > 0) {
    document.write("\n");
    // document.write(b);
    b = b - 1;
}

function sumNNumbers(ni) {
    let s = 0;
    for (let i = 0; i <= ni; i++) {
        s = s + i;
    }
    return s;
}

const c = sumNNumbers(20);
// document.write(c);

const obj = {
    b: 10
};
const d = sumNNumbers(obj);
document.write(d);