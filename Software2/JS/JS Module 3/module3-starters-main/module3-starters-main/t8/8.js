function calculate() {
    let result;
    const num1 = parseInt(document.getElementById('num1').value);
    const num2 = parseInt(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;
    if (operation === 'add') {
        result = num1 + num2;
    } else if (operation === 'sub') {
        result = num1 - num2;
    } else if (operation === 'multi') {
        result = num1 * num2;
    } else if (operation === 'div') {
        result = num1 / num2;
    }
    document.getElementById('result').textContent = `Result: ${result}`;
}

document.getElementById('start').addEventListener('click', calculate)