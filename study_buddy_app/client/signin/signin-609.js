const homePageUrl = "../home/home-609.html";

function signin() {
    const payload = {
        "email": document.getElementsByName("email")[0].value,
        "password": document.getElementsByName("password")[0].value
    };

    const endpoint = "http://localhost:3009/api/v1/sign-in";
    const params = {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    };

    fetch(endpoint, params)
        .then(success)
        .then(onSuccess, onFailure)
        .catch(error);
}

function success(response) {
    if (!response.ok) {
        throw response;
    }
    return response;
}

function onSuccess(response) {
    window.location.href = homePageUrl;
}

function onFailure(response) {
    return response.json().then(error);
}

function error(response) {
    let errorPar = document.getElementsByName("errorParagraph")[0];

    if (!errorPar) {
        const body = document.getElementsByTagName("body")[0];
        const errorDiv = document.createElement("div");
        errorPar = document.createElement("p");
        errorPar.innerText = response.error;
        errorPar.setAttribute("name", "errorParagraph");
        errorDiv.appendChild(errorPar);
        body.appendChild(errorDiv);
    } else {
        errorPar.innerText = response.error;
    }
}