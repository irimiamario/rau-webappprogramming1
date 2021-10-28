function buttonClickedResponse(resp) {
    console.log("..IT WORKS!!")
    return resp.json();
}

function buttonClickedError(err) {
    console.log("--There was an error");
    console.log(err)
}

function displayData(r) {
    console.log("..Processing data.");
    const button = document.querySelector("button")
    button.innerText = "Waiting to print results";
    const body = document.querySelector("body");
    const paragraph = document.createElement("p");
    paragraph.innerText = `Number of data points: ${r.data.length}`;
    body.appendChild(paragraph);
    for (const value of r.data) {
        const paragraph1 = document.createElement("p");
        paragraph1.innerText = value.attributes.name;
        paragraph1.classList.add('new-paragraph');
        // paragraph1.style.fontSize = '20px';
        // paragraph1.style.color = 'blue';
        // paragraph1.style.fontFamily = 'Courier';
        body.appendChild(paragraph1);
    }
    button.innerText = "Waiting done. Click again.";
}

function buttonClicked() {
    const button = document.querySelector("button");
    button.innerText = "Just clicked";
    setTimeout(() => { }, 100);
    console.log("Someone clicked me.");
    // console.log(e);
    console.log("I'm going to get data.");
    requestOptions = {
        headers: {
            'Content-Type': 'application/json'
        }
    }
    url = 'https://api.battlemetrics.com/servers?page[size]=100&sort=rank&filter[game]=rust&filter[status]=online&filter[search]=rustafied'
    fetch(url,
        requestOptions)
        .then(buttonClickedResponse)
        .then(displayData)
        .catch(buttonClickedError)
    console.log("I'm still waiting.")
}

