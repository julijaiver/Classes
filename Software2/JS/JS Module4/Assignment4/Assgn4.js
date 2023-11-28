'use strict';

const searchForm = document.querySelector('#movie_form');
const resultsContainer = document.querySelector('#results');

searchForm.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const query = document.querySelector('input[name=q]').value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const jsonData = await response.json();

        resultsContainer.innerHTML = '';

        jsonData.forEach (result => {
            const article = document.createElement('article');

            const name = document.createElement('h2');
            name.textContent = result.show.name;

            const url = document.createElement('a');
            url.href = result.show.url;
            url.textContent = 'Link';
            url.target = '_blank';

            const image = document.createElement('img');
            image.src = result.show.image ? result.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
            image.alt = 'image';

            const summary = document.createElement('div');
            summary.innerHTML = result.show.summary;

            article.appendChild(name);
            article.appendChild(image);
            article.appendChild(summary);
            article.appendChild(url);

            resultsContainer.appendChild(article);
        })
    } catch (error) {
        console.log(error.message);
    }
});