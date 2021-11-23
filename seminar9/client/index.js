function ifSuccess(response) {
    return response.json()
}

function newUserCreated(response) {
    const body = document.querySelector('body');
    const p = document.createElement("p");
    p.innerText = `New user created!! User name: ${response.name}. User email ${response.email}`;
    body.appendChild(p);
}

function displayUserInfo(response) {
    const body = document.querySelector('body');
    for (const user of response) {
        const p = document.createElement("p");
        p.innerText = `User name: ${user[0]}. User email ${user[1]}`;
        body.appendChild(p);
    }
}

function ifError(err) {
    console.log(err)
}

function signup() {
    const data = {
        name: document.getElementsByName("name")[0].value,
        email: document.getElementsByName("email")[0].value,
        password: document.getElementsByName("password")[0].value,
        company_id: parseInt(document.getElementsByName("company_id")[0].value)
    }
    url = "http://localhost:5000/users"
    params = {
        method: 'POST',
        body: JSON.stringify(data),
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        }
    }
    fetch(url, params)
        .then(ifSuccess)
        .then(newUserCreated)
        .catch(ifError)
}

function showUsers() {
    url = "http://localhost:5000/users"
    params = {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        }
    }
    fetch(url, params)
        .then(ifSuccess)
        .then(displayUserInfo)
        .catch(ifError);
}