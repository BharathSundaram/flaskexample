function sendOption() {
    const selectedOption = document.getElementById('Toolsoption').value;
    fetch('/submit-option', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ option: selectedOption })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}