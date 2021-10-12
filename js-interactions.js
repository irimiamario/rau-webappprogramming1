function changeWelcomeText() {
    const elements = document.querySelectorAll('h2');
    elements[0].innerText = "Modified Welcome Page Message";
    // elements[0].style.fontFamily = 'Roboto';
    // elements[0].style.color = 'green';
    // elements[0].style.fontSize = '60px';
    // console.log(elements[0].attributes);
    // elements[0].attributes[0].value = 'header-modified-style';
    console.log(elements[0].classList);
    elements[0].classList.add('header-color');
    console.log(elements[0].classList);

    const addressElement = document.getElementById("sample-address");
    // console.log(addressElement);
    // addressElement.innerText = "Tg Jiu, Romania";
    for (const element of addressElement.children) {
        console.log(element.classList);
        if (element.classList.contains('header-style')) {
            element.classList.add('header-modified-style');
        }
    }
    // const addressParagraph = addressElement.querySelector("p");
    // addressParagraph.innerText = "Tg Jiu";
    // addressParagraph.classList = [];
    // addressParagraph.style.fontSize = "14px";
    // const addressHeader = addressElement.querySelector("h6");
    // addressHeader.classList = [];
    // addressHeader.style.fontSize = "20px";
    // addressHeader.style.fontFamily = "Arial";

    const div = document.createElement('div');
    const p = document.createElement('p');
    p.innerText = "Automated div + paragraph";
    // div.innerHTML = '<p>Automated div</p>';
    div.appendChild(p);
    document.body.appendChild(div);
}

function getData() {
    const data = fetch("https://reqres.in/")
        .then(response => {
            console.log('Response', response);
        })
        .catch(error => {
            console.log('Error', error);
        });
    const response = fetch("", {
        method: 'POST',
        headers: {},
        body: JSON.stringify(
            {
                name: 'andrei',
                email: 'l@l.l',
                password: '3424rwefe3421'
            }
        )
        })
        .then(r => {
        })
        .catch(e => {
            console.log(e);
            changeWelcomeText();
        });
}


