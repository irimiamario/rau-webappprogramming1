function cancel() {
    const container = document.getElementById("container")
    const div = document.createElement("div");
    const p = document.createElement("p");
    p.innerText = "Warning! You are about to reset your inputs.Are you sureyou want to continue?";
    p.style.fontSize = "20px";
    p.style.color = 'red';
    div.appendChild(p);
    container.appendChild(div);
}

function success(r) {
    console.log("API call worked!");
}



function signup() {
    const data = {
        name: document.getElementsByName("name")[0].value,
        email: document.getElementsByName("email")[0].value,
        password: document.getElementsByName("password")[0].value,
        retryPassword: document.getElementsByName("retry-password")[0].value
    }

    function fail(err) {
        console.log("Success!");
        console.log(data);
    }
    
    const params = {
        method: 'POST',
        body: JSON.stringify(data)
    }
    fetch("https://example.com", params)
        .then(success)
        .catch(fail);
}