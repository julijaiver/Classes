'use strict';

const quizButton = document.querySelector('#quizButton');
const overlay = document.querySelector('#overlay');
const popupContainer = document.querySelector('#popupContainer');
const quizContent = document.querySelector('#quizContent');
const submitButton = document.querySelector('#submitQuiz');
let quizData = []; // Holds the quiz data array
let currentQuestionData; // Holds the current question data

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
        return result;// Return the entire quiz data array
    } catch (error) {
        throw new Error(error);
    }
}

function displayNextQuestion() {
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

    quizContent.innerHTML = ''; // Clear previous question
    quizContent.appendChild(questionDiv);
}

async function startQuiz() {
    try {
        quizData = await fetchQuizData();
        displayNextQuestion();
        popupContainer.classList.add('visible'); // Add 'visible' class to trigger animation
    } catch (error) {
        console.error(error);
    }
}

quizButton.addEventListener('click', function() {
    startQuiz();
    overlay.style.display = 'flex'; // Show the dark overlay
    popupContainer.style.display = 'block'; // Show the popup window
});

submitButton.addEventListener('click', function() {
    checkAnswers();
    displayNextQuestion();
});

function checkAnswers() {
    const selectedAnswer = document.querySelector('input[name="answer"]:checked');
    if (selectedAnswer) {
        const selectedValue = selectedAnswer.value;
        const correctAnswer = currentQuestionData.answer;

        if (selectedValue === correctAnswer) {
            alert('Correct answer!');
        } else {
            alert('Incorrect answer. Try again!');
        }
    } else {
        alert('Please select an answer.');
    }
}
