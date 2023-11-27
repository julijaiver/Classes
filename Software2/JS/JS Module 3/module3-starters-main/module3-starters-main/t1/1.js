const list = document.getElementById('target');
    const items =
        `<li>First Item</li>
         <li>Second Item</li>
         <li>Third Item</li>`;
    list.innerHTML = items;

    list.classList.add('my-list');
