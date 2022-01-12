const endpoint = "http://localhost:3007/api/v1/sign-in";
const homePageUrl = "../home/home-607.html";

function onSuccess(response) {
    window.location.href = homePageUrl;
}

function onFailure(response) {
    return response.json().then(error);
}

function success(response) {
    if (!response.ok) {
        throw response;
    } 
    return response
}

function error(response) {
    const body = document.getElementsByTagName("body")[0];
    
    const errorDiv = document.createElement("div");
    
    const errorPar = document.createElement("p");
    errorPar.innerText = response.error;

    errorDiv.appendChild(errorPar);
    body.appendChild(errorDiv);
}

function signin() {
    const payload = {
        "email": document.getElementsByName("email")[0].value,
        "password": document.getElementsByName("password")[0].value
    };

    const params = {
        body: JSON.stringify(payload),
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json"
        }
    };

    fetch(endpoint, params)
        .then(success)
        .then(onSuccess, onFailure)
        .catch(error);
}