const signInPageUrl = "../signin/signin-610.html"

function signup() {
    // extragem datele din formular 
    // document.getElementsByName("firstName")[0].value este echivalet cu urmatorii pasi
    // 1. const inputs = document.getElementsByName("firstName") => returneaza o lista de elem 
    // 2. const input = inputs[0] ==> selectez primul element
    // 3. const value = input.value ==> extrag valoarea primului element
    const payload = {
        "first_name": document.getElementsByName("firstName")[0].value,
        "last_name": document.getElementsByName("lastName")[0].value,
        "email": document.getElementsByName("email")[0].value,
        "password": document.getElementsByName("password")[0].value
    };

    // initializam parametrii unui request POST
    const endpoint = "http://localhost:3010/api/v1/sign-up";
    const params = {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    };

    // facem un request catre API de signup
    fetch(endpoint, params)
        .then(success)
        .then(onSuccess, onFailure)
        .catch(error)
}

function success(response) {
    if (!response.ok) {
        throw response;
    }
    return response;
}

function onSuccess(response) {
    window.location.href = signInPageUrl;
}

function onFailure(response) {
    return response.json().then(error);
}

function error(response) {
    let errorPar = document.getElementsByName("errorParagraph")[0];

    if (!errorPar) {
        const errorPar = document.createElement("p");
        errorPar.innerText = response.error;
        errorPar.setAttribute("name", "errorParagraph");

        const errorDiv = document.createElement("div");
        errorDiv.appendChild(errorPar);

        const body = document.getElementsByTagName("body")[0];
        body.appendChild(errorDiv);
    } else {
        errorPar.innerText = response.error;
    }
}