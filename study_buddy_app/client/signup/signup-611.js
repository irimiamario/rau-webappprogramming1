const endpoint = "http://localhost:3011/api/v1/sign-up";
const signInPageUrl = "../signin/signin-611.html";

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
    // get error paragraph 
    const errorParagraph = document.getElementsByName("errorParagraph")[0];

    if (!errorParagraph) {
        // extrage elementul unde vrem sa inseram un tag nou (body)
        const body = document.getElementsByTagName("body")[0];

        // instantiem un nou element (div)
        const errorDiv = document.createElement("div");

        // instantiem un paragraf (p)
        const errorPar = document.createElement("p");

        // adaugam textul erorii la textul paragrafului 
        errorPar.innerText = response.error;
        errorPar.setAttribute("name", "errorParagraph");

        // adaugam paragraful in div
        errorDiv.appendChild(errorPar);

        // adaugam div + paragraf in body
        body.appendChild(errorDiv); 
    } else {
        errorParagraph.innerText = response.error;
    }
    // alert(response.error);
}

function signup() {
    // extrag valorile din input fields
    const payload = {
        "first_name": document.getElementsByName("firstName")[0].value,
        "last_name": document.getElementsByName("lastName")[0].value,
        "email": document.getElementsByName("email")[0].value,
        "password": document.getElementsByName("password")[0].value
    };

    // initializez parametri unui request POST catre API-ul de sign up
    const params = {
        body: JSON.stringify(payload),
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json"
        }
    };

    // fac request catre API de sign up 
    // daca request-ul nu are erori => redirect catre signin
    // daca request are erori => afisez eroarea pe ecran, sub buton
    fetch(endpoint, params)
        .then(success)
        .then(onSuccess, onFailure)
        .catch(error);
}