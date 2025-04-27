let fanChartInstance = null; // Guardar a instância do gráfico

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
    const fanChart = new Chart(ctx, {
        type: 'bar', // Tipo de gráfico (bar = gráfico de barras)
        data: {
            labels: ['Fã 1', 'Fã 2', 'Fã 3', 'Fã 4', 'Fã 5'],
            datasets: [{
                label: 'Interações',
                data: [12, 19, 3, 5, 2],
                backgroundColor: ['#09f', '#f39c12', '#1abc9c', '#e74c3c', '#3498db'],
                borderColor: ['#09f', '#f39c12', '#1abc9c', '#e74c3c', '#3498db'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return 'Interações: ' + tooltipItem.raw;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Fãs'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Quantidade'
                    }
                }
            }
        }
    });
}

async function fetchFans() {
    try {
        const response = await fetch('http://127.0.0.1:8000/fans');
        if (!response.ok) {
            throw new Error('Erro ao buscar fãs');
        }
        const fans = await response.json();
        console.log(fans); // Verifique se os fãs estão sendo carregados corretamente

        const fansList = document.getElementById('fans-list');
        fansList.innerHTML = ''; // Limpar qualquer conteúdo anterior

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

        // Atualiza o gráfico depois de listar os fãs
        updateFanChart(fans);

    } catch (error) {
        console.error('Erro:', error);
    }
}

// Chama a função quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', fetchFans);
