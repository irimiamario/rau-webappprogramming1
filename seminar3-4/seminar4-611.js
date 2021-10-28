function changeStyle() {
    const h1 = document.querySelector('.heading');
    console.log(h1);
    const div = document.querySelector('#container');
    console.log(div);

    const p = document.createElement('p');
    p.innerText = 'This is a paragraph generated on click.'
    div.appendChild(p);

    for (const child of div.children) {
        // console.log(child.tagName);
        if (child.tagName.toLowerCase() === 'p') {
            child.classList.add('para');
        }
    }

    const body = document.querySelector('body');

    const newDiv = document.createElement('div');
    const newPar = document.createElement('p');
    newPar.innerText = 'Inserted paragraph before div with id = container';
    newDiv.appendChild(newPar);
    body.insertBefore(newDiv, div);
}

function appendElements() {
    const body = document.querySelector('body')
    const button = document.getElementsByName('button-left')[0];
    for (let i = 0; i < 10; i++) {
        // const p = document.createElement('p');
        // p.innerText = `Paragraph # ${i + 1}`;
        const p = createParagraph(`${i + 1}`);
        body.insertBefore(p, button);
    }
}

function createParagraph(text) {
    const p = document.createElement('p');
    p.innerText = `Paragraph # ${text}`;
    p.classList.add('para');
    p.style.fontSize = '15px';
    return p;
}