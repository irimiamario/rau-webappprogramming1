function buttonClickedResponse(resp) {
    console.log("..IT WORKS!!")
    return resp.json();
}

function buttonClickedError(err) {
    console.log("--There was an error");
    console.log(err)
}

function displayData(r) {
    console.log(r);
    console.log("Number of results: ", r.data.length)
}

function buttonClicked() {
    console.log("Someone clicked me.");
    // console.log(e);
    console.log("I'm going to get data.");
    requestOptions = {
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    // url = 'https://api.battlemetrics.com/servers?page[size]=100&sort=rank&filter[game]=rust&filter[status]=online&filter[search]=rustafied'
    url = 'http://localhost:5000/data';
    fetch(url,
        requestOptions)
        .then(buttonClickedResponse)
        .then(displayData)
        .catch(buttonClickedError)
    console.log("I'm still waiting.")
}

