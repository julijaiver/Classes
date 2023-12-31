'use strict';

// global variables
const overlay = document.querySelector('.overlay');
const popup = document.querySelector('.popup');
function initializeMap() {
    const map = L.map('map').setView([51.505, -0.09], 7);

    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 20,
    }).addTo(map);

    const redMarker = L.icon({
        iconUrl: 'photos/roundMarker.png',
        iconSize: [50, 50],
        iconAnchor: [25, 20]
    });

    const greenMarker = L.icon({
        iconUrl: 'photos/marker2.png',
        iconSize: [50, 50],
        iconAnchor: [25, 20]
    });

    let active = false;
    let marker;

    if (active) {
        marker = L.marker([51.505, -0.09], {icon: greenMarker}).addTo(map);
        marker.bindPopup(`You are here: <br>//airport name</br>`);
        marker.openPopup();
    } else {
        marker = L.marker([51.505, -0.09], {icon: redMarker}).addTo(map);
        const popupContent = document.createElement('div');
        const h4 = document.createElement('h4');
        h4.innerHTML = `//airport name`;
        popupContent.append(h4);
        const p = document.createElement('p');
        p.innerHTML = `Distance: //range`;
        popupContent.append(p);
        const flyButton = document.createElement('button');
        flyButton.classList.add('popup-button');
        flyButton.innerHTML = 'FLY';
        popupContent.append(flyButton);
        marker.bindPopup(popupContent);
    }

        // Function to close the popup
    function closeMarkerPopup() {
        if (!map.getBounds().contains(marker.getLatLng())) {
            marker.closePopup();
        }
    }

    // Event listeners for the marker and popup
    marker.on('mouseover', function () {
        marker.openPopup();
    });

    marker.on('mouseout', function () {
        closeMarkerPopup();
    });

    marker.getPopup().on('mouseout', function () {
        closeMarkerPopup();
    });
}

//Popup doesn't stay open when mouse is over it


// Need to set initial coordinates with database random loc.
//const map = L.map('map').setView([51.505, -0.09], 13);

function showPopup(id) {
    const popup = document.querySelector(`#${id}`);
    overlay.style.display = 'block';
    popup.style.display = 'block';
}

async function nameFormSubmit(evt) {
    evt.preventDefault();
    const name = document.querySelector('#playersName').value;
    const nameDisplay = document.querySelector('#displayName');
    nameDisplay.append(name);
    popup.style.display = 'none';
     //Flask part?
//     try {
//         await fetch('/name', {
//             method: 'POST',
//             headers: {
//             'Content-Type': 'application/json'
//         },
//             body: JSON.stringify({name: name})
//         })
//             .then(response => {
//                 if (response.ok) {
//                     overlay.style.display = 'none';
//                     const popup = document.querySelector('#startPopContainer');
//                     popup.style.display = 'none';
//                 } else {
//                     throw new Error('Submission failed.');
//                 }
//             })
//     } catch (error) {
//         alert('Error: ' + error.message);
//     }
 }

document.addEventListener('DOMContentLoaded', function () {
       initializeMap();
       //showPopup('startPopContainer');
});

const nameForm = document.querySelector('#playerForm');
nameForm.addEventListener('submit', nameFormSubmit);


    // in the html file display name
const submitDifficultyButton = document.querySelector('#submitContinent');
//submitDifficultyButton.addEventListener('click', async function() {
//     const selectedContinent = document.querySelector('input[name="Difficulty"]:checked').id;
//     const data = {
//         continent: selectedContinent
//     };
//
//     fetch('/submit_continent', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//     })
//     .then(response => {
//         if (response.ok) {
//             return response.json();
//         } else {
//             throw new Error('Response failed');
//         }
//     })
//         .then(aiportData => {
//             //handle airport data
//             airportData.forEach(airport => {
//                 //do something
//             })
//         })
//         .catch(error => {
//             console.error('Error: ', error)
//         });
// });
// })




//showPopup('missionSuccess');
//success button.eventlistener. when clicked game starts again (if points == leaderboard then show)

//showPopup('gotCaught');

const quizButton = document.querySelector('#quizButton');
const quizPopupContainer = document.querySelector('#quizPopup');
const quizContent = document.querySelector('#quizContent');
const submitButton = document.querySelector('#submitQuiz');
let quizData = []; // Holds the quiz data array
let currentQuestionData; // Holds the current question data
//later to be changed to different event

async function fetchQuizData() {
    const url = 'https://quiz26.p.rapidapi.com/questions';
    const options = {
        method: 'GET',
        headers: {
            'X-RapidAPI-Key': '009ecb696dmshe46f2fac8aecfccp1f6ec3jsnae92dcd0a865',
            'X-RapidAPI-Host': 'quiz26.p.rapidapi.com'
        }
    };

    try {
        const response = await fetch(url, options);
        const result = await response.json();
        return result;
    } catch (error) {
        throw new Error(error);
    }
}

function displayRandQuestion() {
    if (quizData.length === 0) {
        console.log('No more questions.');
        return;
    }

    const randomIndex = Math.floor(Math.random() * quizData.length);
    currentQuestionData = quizData[randomIndex];
    quizData.splice(randomIndex, 1); // Remove the selected question from the array

    const questionDiv = document.createElement('div');
    questionDiv.classList.add('popup-content');
    questionDiv.innerHTML = `<h3>${currentQuestionData.question}</h3>`;

    const options = Object.keys(currentQuestionData).filter(key => key !== 'question' && key !== 'answer');
    options.forEach(optionKey => {
        const optionLabel = document.createElement('label');
        const optionInput = document.createElement('input');
        optionInput.type = 'radio';
        optionInput.name = 'answer';
        optionInput.value = optionKey;

        optionLabel.appendChild(optionInput);
        optionLabel.appendChild(document.createTextNode(currentQuestionData[optionKey]));
        questionDiv.appendChild(optionLabel);
        questionDiv.appendChild(document.createElement('br'));
    });

    quizContent.innerHTML = ''; // Clears previous question
    quizContent.appendChild(questionDiv);
}

async function startQuiz() {
    try {
        quizData = await fetchQuizData();
        displayRandQuestion();
        quizPopupContainer.classList.add('visible'); // Adds 'visible' class to trigger animation
    } catch (error) {
        console.error(error);
    }
}
quizButton.addEventListener('click', function() {
    startQuiz();
    overlay.style.display = 'block'; // Show the dark overlay
    quizPopupContainer.style.display = 'block'; // Show the popup window
});

function checkAnswers() {
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (selectedAnswer) {
        const selectedValue = selectedAnswer.value;
        const correctAnswer = currentQuestionData.answer;

        if (selectedValue === correctAnswer) {
            alert('Congratulations! You get 15 points and battery power');
            //Adding points to the number on screen
            overlay.style.display = 'none';
            quizPopupContainer.style.display = 'none';
        } else {
            overlay.style.display = 'none';
            quizPopupContainer.style.display = 'none';
            showPopup('gotCaught');
        }
    } else {
        alert('Please select an answer.');
    }
}

submitButton.addEventListener('click', function() {
    checkAnswers();
});


const submitNameButton = document.querySelector('#submitName');
submitNameButton.addEventListener('click', function () {
    showPopup('difficultyPopContainer');
})