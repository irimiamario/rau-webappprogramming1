function buttonClicked() {
    console.log("Clicked!");
    const h1 = document.querySelector("h1");
    h1.style.color = "blue";
    h1.style.fontFamily = 'Courier';

    const p = document.createElement("p")
    p.innerText = "This was created on button click.";

    const div = document.getElementById("container");
    div.appendChild(p);

    const ps = document.querySelectorAll("p");
    for (const pi of ps) {
        pi.classList.add("auto-para")
    }
}

function buttonClickedResponse(resp) {
    return resp.json();
}

function displayData(resp) {
    console.log(resp);
    const nElements = resp.data.length;

    const p = document.createElement("p");
    p.innerText = `Number of servers available: ${nElements}`;
    p.style.fontSize = '20px';
    p.style.fontWeight = 500;
    p.style.color = 'blue';
    const body = document.querySelector("body");
    body.insertBefore(p, body.children[1]);

    const div = document.getElementById("container");
    for (const entry of resp.data) {
        const serverIdParagraph = document.createElement("p");
        serverIdParagraph.innerText = `Server id ${entry.id}`;
        body.insertBefore(serverIdParagraph, div);
    }
}

function buttonClickedError(err) {
    const body = document.querySelector("body");
    const p = document.createElement("p");
    p.innerText = "Mare eroare! Nu a mers nimic!";
    p.style.fontFamily = 'Courier';
    p.style.fontSize = '60px';
    p.style.color = 'red';
    body.appendChild(p);
}

function getData() {
    url = 'https://api.battlemetrics.com/servers?page[size]=100&sort=rank&filter[game]=rust&filter[status]=online&filter[search]=rustafied'
    // url = 'example.com';
    fetch(url)
        .then(buttonClickedResponse)
        .then(displayData)
        .catch(buttonClickedError)
    console.log("I'm still waiting.")
}