function signup() {
    // extract values from all inputs 
    const firstName = document.getElementsByName("firstName")[0].value;
    const lastName = document.getElementsByName("lastName")[0].value;
    const email = document.getElementsByName("email")[0].value; 
    const password = document.getElementsByName("password")[0].value; 
    const secondPassword = document.getElementsByName("secondPassword")[0].value;

    // define API endpoint 
    const url = "http://localhost:3010/api/v1/users";

    // create a request body 
    const userDetails = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": password,
        "secondPassword": secondPassword
    };

    // create additional parameters required to make a POST request 
    const options = {
        "body": JSON.stringify(userDetails), 
        "method": "POST", 
        "mode": "cors", 
        "headers": {
            "Content-Type": "application/json"
        }
    };

    // make post request 
    fetch(url, options)
        .then(ifSuccess)
        .catch(ifError)
}

function ifSuccess(r) {
    // TODO: Implement behaviour when request is successful 
}

function ifError(e) {
    // TODO: Implement behaviour when you get an error
}
