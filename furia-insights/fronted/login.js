// Exemplo de como enviar dados para criar um fã
document.getElementById("create-fan-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const fanData = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    age: document.getElementById("age").value,
    };

    try {
    const response = await fetch("http://127.0.0.1:8000/fans", {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(fanData),
    });

    if (response.ok) {
        const newFan = await response.json();
        console.log("Fã criado:", newFan);
        // Talvez redirecionar para outra página ou atualizar a UI com o novo fã
    } else {
        alert("Erro ao criar fã");
    }
    } catch (error) {
    console.error("Erro ao fazer requisição:", error);
    }
});
