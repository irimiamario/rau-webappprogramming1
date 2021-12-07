function responseReceived(response) {
    return response.json()
}

function processResponse(response) {
    console.log(response);
}

function errorReceived(error) {
    console.log(error);
}

function getUsersData() {
    url = 'http://localhost:3005/users'
    response = fetch(url)
        .then(responseReceived)
        .then(processResponse)
        .catch(errorReceived);
}