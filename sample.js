const endpoint = "https://users.thesiloapp.com/api/v1/version"
const params = {
    method: "GET",
    mode: "cors", 
    headers: {
        "Content-Type": "application/json"
    }
}

fetch(endpoint, params)
    .then(success)
    .then(onSuccess, onFailure)
    .catch(error)


function success(response) {
    if (!response.ok) {
        throw response; 
    }
    return response;
}

function onSuccess(response) {
    return response.json().then(displaySuccessResponse);
}

function onFailure(response) {

}

function error(response) {

}

function displaySuccessResponse(response) {
    console.log(response);
}

function mockButtonPressed() {
    // cod care nu functioneaza

    // implementeaza functionalitatea dorita atunci cand primesc raspunsul cu succes de la API
    response = {
        first_name: 'Sample first name',
        last_name: 'Sample last name',
        year: 2022
    }

    const p = document.getElementsByName("userName")[0];
    p.innerText = `Welcome to your Study Buddy Profile, ${response.first_name} ${response.last_name}!`;

    const gradYearPar = document.createElement("p");
    gradYearPar.innerText = `Graduation year: ${response.year}`;

    const body = document.getElementsByTagName("body")[0];
    body.appendChild(gradYearPar);
}