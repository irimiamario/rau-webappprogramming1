function signup() {
    console.log("Congratulations! You have successfully created an account");
    let s = 0;
    for (let i = 0; i <= 50; i++) {
        s += i;
    }
    console.log(`Sum of all numbers up to 50: ${s}`);
}

function cancel() {
    console.log("Warning! You are about to reset your inputs. Are you sure you want to continue?");
}

function signupCall() {
    const data = {
        name: document.getElementsByName("name")[0].value,
        email: document.getElementsByName("email")[0].value,
        password: document.getElementsByName("password")[0].value,
        retryPassword: document.getElementsByName("retry-password")[0].value
    }
    console.log(data);
    const newUserResponse = fetch("", {
        method: 'POST',
        body: JSON.stringify(data)
    })
        .then(() => {
            console.log("API call worked!");
        })
        .catch(() => {
            console.log("Success!");
            console.log(data);
        })
}

function cancelCall() {
    const div = document.createElement('div');
    const par = document.createElement('p');
    par.innerText = "Warning! You are about to reset your inputs. Are you sure you want to continue?";
    par.style.fontSize = '20px';
    par.style.color = 'red';
    div.appendChild(par);
    // document.body.appendChild(div);
    const inputDiv = document.getElementsByClassName("container")[0];
    inputDiv.appendChild(div);
}