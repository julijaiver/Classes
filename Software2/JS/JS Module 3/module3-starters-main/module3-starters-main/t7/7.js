const p = document.getElementById('trigger');
const image = document.getElementById('target');
function mouseOver(){
    image.src = 'img/picB.jpg';
}
function mouseOut() {
    image.src = 'img/picA.jpg';
}

p.addEventListener('mouseover', mouseOver);
p.addEventListener('mouseout', mouseOut);