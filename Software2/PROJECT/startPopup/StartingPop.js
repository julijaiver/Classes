'use strict';

const overlay = document.querySelector('#startOverlay');
const popup = document.querySelector('#startPopContainer');
const nameForm = document.querySelector('#playerForm');

document.addEventListener('DOMContentLoaded', function () {
    overlay.style.display = 'block';
    popup.style.display = 'block';
});

nameForm.addEventListener('submit', async function(evt) {
    evt.preventDefault();
    const name = document.querySelector('#playersName').value;

    // in the html file display name

    //Flask part?
    try {
        await fetch('/name', {
            method: 'POST',
            body: JSON.stringify({name: name})
        })
            .then(response => {
                if (response.ok) {
                    overlay.style.display = 'none';
                    popup.style.display = 'none';
                } else {
                    throw new Error('Submission failed.');
                }
            })
    } catch (error) {
        alert('Error: ' + error.message);
    }
});



// event listener after loading page:
// overlay and start popup display: block
//
// submit button event listener:
// click, POST data to flask
