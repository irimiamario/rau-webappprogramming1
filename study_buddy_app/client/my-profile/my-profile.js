// load user data 
const user_id = 1;
const endpoint = `http://localhost:3018/api/v1/my-profile/${user_id}`;
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
    return response.json().then(displayProfile);
}

function onFailure(response) {
    return response.json().then(error);
}

function error(response) {
    alert(response);
}

function displayProfile(response) {
    const p = document.getElementsByName("userName")[0];
    p.innerText = `Welcome to your Study Buddy Profile, ${response.first_name} ${response.last_name}!`;

    const gradYearPar = document.createElement("p");
    gradYearPar.innerText = `Graduation year: ${response.year}`;

    const body = document.getElementsByTagName("body")[0];
    body.appendChild(gradYearPar);
}
