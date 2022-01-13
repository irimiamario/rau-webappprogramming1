const homePageUrl = "../home/home-610.html";

function signin() {
    const payload = {
        "email": document.getElementById("email").value,
        "password": document.getElementById("password").value
    };

    // inseram email in localstorage
    window.localStorage.setItem("user-email", payload.email);

    // // extragem email din localstorage 
    // const email = window.localStorage.getItem("user-email");

    // // stergem email din localstorage
    // window.localStorage.removeItem("user-email");

    // // stergem tot din localstorage
    // window.localStorage.clear();

    const endpoint = "http://localhost:3010/api/v1/sign-in"
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
    return response.json().then(error)
}

function error(response) {
    let errorPar = document.getElementById("errorParagraph");
    if (errorPar) {
        errorPar.innerText = response.error;
    } else {
        errorPar = document.createElement("p");
        errorPar.innerText = response.error;
        errorPar.setAttribute("id", "errorParagraph");

        const errorDiv = document.createElement("div");
        errorDiv.appendChild(errorPar);

        const body = document.getElementsByTagName("body")[0];
        body.appendChild(errorDiv);
    }
}