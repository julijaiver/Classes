document.querySelector('#source').addEventListener('submit', function (evt) {
    evt.preventDefault();

    const first_name = document.querySelector('input[name=firstname]').value;
    const last_name = document.querySelector('input[name=lastname]').value;
    const p = document.querySelector('#target');

    p.textContent = `Your name is ${first_name} ${last_name}`;
});



