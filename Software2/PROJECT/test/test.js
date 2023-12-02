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

// for (let airport of gameData.location) {
//     L.marker([airport.latitude, airport.longitude], { icon: customIcon }).addTo(map);
// }

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

