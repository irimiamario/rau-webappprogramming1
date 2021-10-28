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