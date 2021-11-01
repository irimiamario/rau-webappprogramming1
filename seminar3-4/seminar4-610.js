alert("This is an alert!");

const variabilaConstanta = 10;
let variabila = 10;


if (variabila > 20) {
    alert(">20");
} else {
    variabila = 50;
    console.log("test");
}

for (let i = 0; i < 10; i++) {
    console.log(i);
}

const l = [1, 2, 3, 4, 5, 6];
for (const e of l) {
    console.log(e);
}

console.log("while")
let a = 20;
while (a > 15) {
    console.log(a);
    a = a - 1;
}

function functiaMea(n) {
    let s = 0;
    for (let i = 0; i <= n; i++) {
        s = s + i;
    }
    return s;
}

const s = functiaMea(variabila);
console.log(`Suma numerelor pana la ${variabila} inclusiv este ${s}`);

const body = document.querySelector("body");

const p = document.createElement("p");
p.innerText = "Acest paragraf e inserat din JS.";
p.style.color = "green";
p.style.fontFamily = "Courier";

body.appendChild(p);


function dataReady(r) {
    return r.json();
}

function displayData(r) {
    console.log(r);
    return 'I am done with displaying data.'
}

function showMessage(r) {
    alert(r);
}

function showError(e) {
    alert('There was an error');
}

url = 'https://users.thesiloapp.com/api/v1/version'
fetch(url)
    .then(dataReady)
    .then(displayData)
    .then(showMessage)
    .catch(showError);