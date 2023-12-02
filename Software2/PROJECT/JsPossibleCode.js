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

