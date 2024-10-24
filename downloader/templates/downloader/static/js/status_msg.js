document.getElementById('download-form').onsubmit = async function(event) {
    event.preventDefault(); 

    const formData = new FormData(event.target);
    const response = await fetch('', {
        method: 'POST',
        body: formData,
    });
    const result = await response.json();
    document.getElementById('result').innerText = result.message;
}