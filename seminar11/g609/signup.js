function signup() {
    // extract input data from all 5 inputs 
    const firstName = document.getElementsByName("firstName")[0].value;
    const lastName = document.getElementsByName("lastName")[0].value;
    const email = document.getElementsByName("email")[0].value;
    const password = document.getElementsByName("password")[0].value;
    const secondPassword = document.getElementsByName("secondPassword")[0].value;

    // create a request body with the following fields firstName, lastName, email, password, secondPassword
    const body = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email, 
        "password": password,
        "secondPassword": secondPassword
    };

    // make a POST request to http://localhost:3004/api/v1/users using Fetch API
    const options = {
        "body": JSON.stringify(body),
        "method": "POST",
        "mode": "cors",
        "headers": {
            "Content-Type": "application/json",
        }
    }
    fetch("http://localhost:3004/api/v1/users", options)
        .then(ifSuccess)
        .catch(ifError)
}

function ifSuccess(r) {
    // TODO: implement what happens when I get a successful response from server
}

function ifError(e) {
    // TODO: implement what happens when I get an error
}