'use strict';

const form = document.querySelector('#chuck_joke');
const resultContainer = document.querySelector('#results');

form.addEventListener('submit', async function (evt) {
    evt.preventDefault();

    const query = document.querySelector('input[name=q]').value;
    try {
        const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${query}`);
        const jokeData = await response.json();

        resultContainer.innerHTML='';

        jokeData.result.forEach(joke => {
            const article = document.createElement('article');
            const paragraph = document.createElement('p');
            paragraph.innerText = joke.value;

            article.appendChild(paragraph);
            resultContainer.appendChild(article);
        })
    } catch (error) {
        console.log(error.message);
    }

})