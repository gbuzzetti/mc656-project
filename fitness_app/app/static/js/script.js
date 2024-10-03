document.getElementById('calcular-btn').addEventListener('click', function () {
    var kg = document.getElementById('kg-input').value;

    if (kg) {
        fetch('/calcular_recomendacao_agua', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ kg: kg })
        })
        .then(response => response.json())
        .then(data => {
            if (data.result) {
                document.getElementById('resultado').innerText = 'Resultado em litros: ' + data.result;
            } else {
                document.getElementById('resultado').innerText = 'Erro: ' + data.error;
            }
        })
        .catch(error => {
            document.getElementById('resultado').innerText = 'Erro de conexão com o servidor';
        });
    } else {
        alert("Por favor, insira um valor em Kg");
    }
});