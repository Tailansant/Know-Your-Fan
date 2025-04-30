let allFans = []; // Variável global para armazenar todos os fãs
let fanChartInstance = null;

function updateFanChart(fans) {
    let cs2Count = 0;
    let lolCount = 0;
    let valorantCount = 0;

    fans.forEach(fan => {
        if (fan.preferences) {
            if (fan.preferences.CS2) cs2Count++;
            if (fan.preferences.LoL) lolCount++;
            if (fan.preferences.Valorant) valorantCount++;
        }
    });

    const ctx = document.getElementById('fanChart').getContext('2d');

    if (fanChartInstance) {
        fanChartInstance.destroy(); // Destroi gráfico anterior
    }

    fanChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['CS2', 'LoL', 'Valorant'],
            datasets: [{
                label: 'Fãs por Jogo',
                data: [cs2Count, lolCount, valorantCount],
                backgroundColor: ['#09f', '#f39c12', '#e74c3c'],
                borderColor: ['#09f', '#f39c12', '#e74c3c'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: function (tooltipItem) {
                            return 'Fãs: ' + tooltipItem.raw;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Jogos' }
                },
                y: {
                    title: { display: true, text: 'Quantidade de Fãs' },
                    beginAtZero: true,
                    precision: 0
                }
            }
        }
    });
}

function renderFanCards(fans) {
    const fansList = document.getElementById('fans-list');
    fansList.innerHTML = '';

    if (fans.length === 0) {
        fansList.innerHTML = '<p>Nenhum fã encontrado.</p>';
    } else {
        fans.forEach(fan => {
            const card = document.createElement('div');
            card.className = 'fan-card';

            let preferencesHtml = '';
            if (fan.preferences) {
                preferencesHtml = '<ul>';
                for (const key in fan.preferences) {
                    preferencesHtml += `<li><strong>${key}:</strong> ${fan.preferences[key]}</li>`;
                }
                preferencesHtml += '</ul>';
            }

            card.innerHTML = `
                <h4>${fan.name}</h4>
                <p><strong>Username:</strong> ${fan.username}</p>
                <p><strong>Localização:</strong> ${fan.location}</p>
                <h5>Preferências:</h5>
                ${preferencesHtml}
            `;
            fansList.appendChild(card);
        });
    }
}

function filterFans(jogo) {
    let filtrados = [];

    if (jogo === 'Todos') {
        filtrados = allFans;
    } else {
        filtrados = allFans.filter(fan => fan.preferences && fan.preferences[jogo]);
    }

    renderFanCards(filtrados);
    updateFanChart(filtrados);
}

async function fetchFans() {
    try {
        const response = await fetch('http://127.0.0.1:8000/fans');
        if (!response.ok) {
            throw new Error('Erro ao buscar fãs');
        }
        const fans = await response.json();
        allFans = fans; // Salva os fãs para uso global

        renderFanCards(fans);
        updateFanChart(fans);
    } catch (error) {
        console.error('Erro:', error);
    }
}

document.addEventListener('DOMContentLoaded', fetchFans);

// Função para registrar a resposta do quiz
let quizAnswer = null;

function recordAnswer(answer) {
    quizAnswer = answer;
    document.getElementById('quiz-result').textContent = `Você escolheu: ${answer}`;
}

