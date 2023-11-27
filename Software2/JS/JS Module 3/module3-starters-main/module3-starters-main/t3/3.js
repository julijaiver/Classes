'use strict';
const names = ['John', 'Paul', 'Jones'];
const list = document.getElementById('target');
for (let i=0; i<names.length; i++) {
    list.innerHTML += `<li>${names[i]}</li>`;
}
