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

