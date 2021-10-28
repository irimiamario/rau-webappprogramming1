function showError(e) {
    alert("Something went wrong");
    const p = document.createElement('p');
    p.innerText = "There was an error with the server.";
    p.style.fontSize = '20px';
    p.style.color = 'red';
    p.style.fontFamily = 'Courier';

    const body = document.querySelector('body');
    body.appendChild(p);
}

function dataReceived(r) {
    return r.json();
}

function displayData(r) {
    console.log(r);
    // const existingDataParagraph = document.querySelector('#entries');
    const existingDataParagraph = document.getElementById('entries');
    if (existingDataParagraph) {
        existingDataParagraph.innerText = `I received ${r.data.length} entries. Modified.`;
    } else {
        const p = document.createElement('p');
        p.innerText = `I received ${r.data.length} entries`;
        p.style.fontFamily = 'Arial';
        p.style.fontSize = '15px';
        p.style.color = 'green';
        p.id = 'entries';
        const body = document.querySelector('body');
        body.appendChild(p);
    }
    return 'Data displayed successfully.'
}

function showMessage(r) {
    alert(r);
}

function getData() {
    url = 'https://api.battlemetrics.com/servers?page[size]=100&sort=rank&filter[game]=rust&filter[status]=online&filter[search]=rustafied'
    fetch(url)
        .then(dataReceived)
        .then(displayData)
        .then(showMessage)
        .catch(showError);
    console.log("Hello");
}

function showSuccess(r) {
    alert('It works!');
}

function sendData() {
    const data = {
        'name': 'andrei',
        'country': 'ro'
    }
    console.log(JSON.stringify(data));
    const sample = JSON.parse('{"location": "ro"}');
    console.log(sample.location);
    
    url = 'https://example.com'
    const params = {
        method: 'POST',
        body: JSON.stringify(data)
    }
    fetch(url, params)
        .then(showSuccess)
        .catch(showError);
}