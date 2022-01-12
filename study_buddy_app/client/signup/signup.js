const endpoints = {
    signup: "http://localhost:3008/api/v1/signup",
}

const pagesUrls = {
    sigin: "../signin/signin.html"
}

function ifSuccess(response) {
    if (response) {
        window.location.href = pagesUrls.sigin;
    }
}

function ifError(error) {
    const body = document.getElementsByTagName("body");

    const errorDiv = document.createElement("div");
    const errorP = document.createElement("p");
    errorP.innerText = error.error;
    errorDiv.appendChild(errorP);
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
    fetch(endpoints.signup, params)
    .then(ifSuccess)
    .catch(ifError);
}