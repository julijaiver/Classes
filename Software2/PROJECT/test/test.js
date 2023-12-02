'use strict';

// global variables
const overlay = document.querySelector('.overlay');

function initializeMap() {
const map = L.map('map').setView([60, 24], 7);

L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 20,
}).addTo(map);

const customIcon = L.icon({
    iconUrl: 'mapMarker.png',
    iconSize: [50, 50],
    iconAnchor: [16, 32]
});

for (let airport of gameData.location) {
    L.marker([airport.latitude, airport.longitude], { icon: customIcon }).addTo(map);
}

// Need to set initial coordinates with database random loc.
//const map = L.map('map').setView([51.505, -0.09], 13);

}

function showPopup(id) {
    const popup = document.querySelector(`#${id}`);
    overlay.style.display = 'block';
    popup.style.display = 'block';
}

async function nameFormSubmit(evt) {
    evt.preventDefault();
    const name = document.querySelector('#playersName').value;

     //Flask part?
    try {
        await fetch('/name', {
            method: 'POST',
            body: JSON.stringify({name: name})
        })
            .then(response => {
                if (response.ok) {
                    overlay.style.display = 'none';
                    const popup = document.querySelector('#startPopContainer');
                    popup.style.display = 'none';
                } else {
                    throw new Error('Submission failed.');
                }
            })
    } catch (error) {
        alert('Error: ' + error.message);
    }
}

document.addEventListener('DOMContentLoaded', function () {
       //showPopup('startPopContainer');
       initializeMap();
});

const nameForm = document.querySelector('#playerForm');
nameForm.addEventListener('submit', nameFormSubmit);

    // in the html file display name

showPopup('missionSuccess');
//success button.eventlistener. when clicked game starts again (if points == leaderboard then show)

//showPopup('gotCaught');
