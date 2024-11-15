class Weight {
    constructor(kg) {
        this.setKg(kg);
    }

    setKg(kg) {
        const parsedKg = parseFloat(kg);
        if (isNaN(parsedKg) || parsedKg <= 0) {
            throw new Error("Invalid weight value. Please enter a positive number.");
        }
        this.kg = parsedKg;
    }

    getKg() {
        return this.kg;
    }
}

document.getElementById('calcular-btn').addEventListener('click', function () {
    try {
        const weight = new Weight(document.getElementById('kg-input').value);

        fetch('/calcular_recomendacao_agua', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ kg: weight.getKg() })
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
    } catch (error) {
        alert(error.message);
    }
});
