async function fetchData (url) {
    const response = await fetch(url);
    if (!response.ok) throw new Error('Invalid server input');
    const result = await response.json();
    return result
}


async function gameSetup() {
    try {
        const gameData = fetchData('')
        console.log(gameData);


    } catch (error) {
        console.log(error);
    }
}

const difficultyButton = document.querySelector('#submitContinent');
difficultyButton.addEventListener('click', async function() {
    const selectedContinent = document.querySelector('input[name="Difficulty"]:checked').id;
    const data = {
        continent: selectedContinent
    };

    fetch('/submit_continent', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Response failed');
        }
    })
        .then(aiportData => {
            //handle airport data
            airportData.forEach(airport => {
                //do something
            })
        })
        .catch(error => {
            console.error('Error: ', error)
        });
});



//currentPoints global var?
//currentBattery global var?
//in line 44
flyButton.setAttribute('id', 'flyToAirport');

const playerPoints = document.querySelector('#playerPoints');
const batteryPower = document.querySelector('#batteryPower')
async function flyToAirport() {
    try {
        const response = await fetch('/checkgoal');
        if (!response.ok) throw new Error('Response failed');
        const goal = await response.json();

        if (goal === '1') {
            alert('Weather seems to be clear and sunny in ..... You get ... points!');
            playerPoints.innerHTML = `${currentPoints +15}`;
            batteryPower.innerHTML = `${currentBattery - (distance)}`;
            //current.airport = chosen.airport
        } else if (goal === '2') {
            alert('Weather seems to be cloudy in .... You get 20 points but use 15% more battery');
            playerPoints.innerHTML = `${currentPoints +15}`;
            batteryPower.innerHTML = `${currentBattery - (distance*1.15)}`;
            //current.airport = chosen.airport
        } else if (goal === '3') {
            if (confirm('This location seems suspicious. Do you want to play a minigame with a possibility' +
                'to gain points and extra battery power and risk getting caught?')) {
                startQuiz();
                overlay.style.display = 'block';
                quizPopupContainer.style.display = 'block';
            } else {
                alert("You didn't risk getting caught but.... Choose an airport");
                //current airport stays the same.
            }
        } else if (goal === '4') {
            showPopup('gotCaught');
        }

        const dataForBackend = {
            airport.icao:
            //points and battery sent at the end?
        }

        const airportsResponse = await fetch('/flyto', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dataForBackend),
        });

        if (!airportsResponse.ok) throw new Error('Fetching airports failed');
        const newAirportsinRange = await airportsResponse.json();

        airportsInRangeOnMap(newAirportsinRange);

    } catch (error) {
        console.log(error.message)
    }
}

async function sendGameData() {
    try {
        const endGameData = {
            //gameid?
            //playerName
            //points
        }
        const response = await fetch ('/endgame', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(endGameData),
        });

        if (!response.ok) throw new Error('Sending data failed');

        const leaderboard = await fetch('/leaderboard');
        if (!response.ok) throw new Error('Receiving leaderboard failed');

        const leaderboardData = await leaderboard.json();

        //in leaderboard table data = put response
    } catch (error) {
        console.error(error.message)
    }
}



//async function getLeaderboard() {
// const playerName = document.querySelector('#nameField');
// const playerScore = document.querySelector('#scoreField');
//  try {
//  const response = await fetch('/leaderboard');
//  if (!response.ok) throw new Error('Response failed');
//  const leaderboard = await response.json();

    // leaderboard.forEach(row => {
    //     playerName.innerHTML = `${row.name}`
    //     playerScore.innerHTML = `${row.score}`
    // });
// }
// } catch (error) {
// console.log.(error.message)
// }








