const list = document.getElementById('target');

    const items = ["First Item", "Second item", "Third item"];

    items.forEach(itemText => {
        const li = document.createElement('li');
        li.textContent = itemText;
        list.appendChild(li);
    })

    const second = document.getElementsByTagName('li')[1];
    second.classList.add('my-list');