'use strict';

const movieForm = document.querySelector('#movie_form');
movieForm.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const searchValue = document.querySelector('#query').value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${searchValue}`);
        const jsonData = await response.json();
        console.log(jsonData);
    } catch (error) {
        console.log(error.message);
    }
});