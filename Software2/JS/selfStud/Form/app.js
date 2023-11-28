const form = document.querySelector('#cats');
const input = document.querySelector('#catName');
const list = document.querySelector('#available');
form.addEventListener('submit', function (e) {
    e.preventDefault();
    const cat_name = input.value;
    const new_li = document.createElement('li');
    new_li.innerHTML = cat_name;
    list.append(new_li);
})

function new_color() {
    const r = Math.floor(Math.random()*255);
    const g = Math.floor(Math.random()*255);
    const b = Math.floor(Math.random()*255);
    return {r, g, b};
}

function is_dark_color (color) {
    const sum = color.r + color.g + color.b;
    return sum<130;
}

document.querySelector('#change_color').addEventListener('click', function () {
    const color = new_color();
    const text_color = is_dark_color(color) ? 'white' : 'black';
    document.body.style.backgroundColor = `rgb(${color.r}, ${color.g}, ${color.b})`;
    document.querySelector('#color').innerText = `rgb(${color.r}, ${color.g}, ${color.b})`;
    const body = document.querySelectorAll('body *');
    body.forEach(element => {
        element.style.color = text_color;
    })
})