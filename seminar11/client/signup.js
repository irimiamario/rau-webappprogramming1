function ifSuccess(response) {
    console.log("USER SIGNED UP.");
}

function ifError(error) {
    console.log(error);
}

function createAccount() {
    const data = {
        firstName: document.getElementsByName("firstName")[0].value,
        lastName: document.getElementsByName("lastName")[0].value,
        email: document.getElementsByName("email")[0].value,
        password: document.getElementsByName("password")[0].value,
        secondPassword: document.getElementsByName("secondPassword")[0].value
    };
    url = "http://localhost:3002/api/v1/users";
    options = {
        body: JSON.stringify(data),
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        }
    };

    fetch(url, options)
    .then(ifSuccess)
    .catch(ifError)
}