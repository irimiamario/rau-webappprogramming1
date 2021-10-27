function cancel() {
    const formDiv = document.getElementById("container");
    const messageDiv = document.createElement("div");
    const messagePar = document.createElement("p");
    messagePar.innerText = "Warning! You are about to reset your inputs. Are you sureyou want to continue?";
    // messagePar.style.color = 'red';
    // messagePar.style.fontSize = '20px';
    messagePar.classList.add('new-paragraph');
    messageDiv.appendChild(messagePar);
    formDiv.appendChild(messageDiv);
}