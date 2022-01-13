const signInPageUrl = '../signin/signin-609.html';

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
        // extrag body din html
        const body = document.getElementsByTagName("body")[0];

        // instantiez un div 
        const errorDiv = document.createElement("div");

        // instatiez un paragraf
        errorPar = document.createElement("p");
        
        // adaug textul cu eroarea paragrfului
        errorPar.innerText = response.error;
        errorPar.setAttribute("name", "errorParagraph");
        
        // connectez paragraful de div
        errorDiv.appendChild(errorPar);

        // connectez div-ul de body
        body.appendChild(errorDiv);
    } else {
        errorPar.innerText = response.error;
    }
}

function signup() {
    // extrag informatiile introduse in campurile de input
    // liniile 4 - 6 sunt echivalente cu linia 7
    // const inputs = document.getElementsByName("firstName");
    // const input1 = inputs[0];
    // const input1Value = input1.value;
    // document.getElementsByName("firstName")[0].value,

    const payload = {
        "first_name": document.getElementsByName("firstName")[0].value,
        "last_name": document.getElementsByName("lastName")[0].value,
        "email": document.getElementsByName("email")[0].value,
        "password": document.getElementsByName("password")[0].value
    }
    
    // instantiez parametrii request-ului 
    const endpoint = "http://localhost:3009/api/v1/sign-up";
    const params = {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    };

    // execut request catre API de sign-up
    fetch(endpoint, params)
        .then(success)
        .then(onSuccess, onFailure)
        .catch(error)
}