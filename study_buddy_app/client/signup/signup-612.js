const endpoint = "http://localhost:3012/api/v1/sign-up"
const signInPageUrl = "../signin/signin-608.html"

function onSuccess(response) {
    window.location.href = signInPageUrl;
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

function signup() {
    const payload = {
        "first_name": document.getElementsByName("firstName")[0].value,
        "last_name": document.getElementsByName("lastName")[0].value,
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
    }

    fetch(endpoint, params)
        .then(success)
        .then(onSuccess, onFailure)
        .catch(error);
}