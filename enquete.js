document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("enquete-modal");
    if (!modal) return;

    const closeBtn = document.querySelector(".enquete-close-btn");
    const enqueteCardBtn = document.querySelector(".enquete-card-btn");
    const optionBtns = document.querySelectorAll(".enquete-option-btn");
    const optionsContainer = document.querySelector(".enquete-options");
    const resultsContainer = document.querySelector(".enquete-results");

    let hasVoted = localStorage.getItem("enquete_votada") === "true";
    let hasDismissed = sessionStorage.getItem("enquete_dismissed") === "true";

    function showModal() {
        modal.classList.add("show");
        if (hasVoted) {
            showResultsState();
            fetchResults();
        } else {
            optionsContainer.style.display = "flex";
            resultsContainer.style.display = "none";
        }
    }

    function closeModal() {
        modal.classList.remove("show");
        if (!hasVoted) {
            sessionStorage.setItem("enquete_dismissed", "true");
        }
    }

    // Gatilhos de Fechamento
    if (closeBtn) closeBtn.addEventListener("click", closeModal);
    
    // Fechar ao clicar fora (Backdrop)
    modal.addEventListener("click", (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    // Fechar com a tecla ESC
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && modal.classList.contains("show")) {
            closeModal();
        }
    });

    // Gatilho Manual
    if (enqueteCardBtn) {
        enqueteCardBtn.addEventListener("click", () => {
            showModal();
        });
    }

    // Gatilho Automático (se não fechou nem votou)
    if (!hasVoted && !hasDismissed) {
        // Apenas disparar automaticamente na página inicial
        if (window.location.pathname === "/" || window.location.pathname === "/index.html") {
            setTimeout(showModal, 4000);
        }
    }

    // Ações de Voto
    optionBtns.forEach(btn => {
        btn.addEventListener("click", async (e) => {
            const optionId = e.currentTarget.getAttribute("data-option");
            
            // UI Feedback Imediato
            localStorage.setItem("enquete_votada", "true");
            hasVoted = true;
            showResultsState();
            
            // Simular load progress ou algo assim
            updateProgressBars({ total: 1, opcao_a: 0, opcao_b: 0, opcao_c: 0 }); 

            try {
                const response = await fetch('/api/enquete/votar', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ option: optionId })
                });

                if (response.ok) {
                    const data = await response.json();
                    updateProgressBars(data);
                } else {
                    console.error("Erro ao registrar voto");
                    fetchResults(); // fallback to get results
                }
            } catch (err) {
                console.error("Erro na requisição de voto", err);
            }
        });
    });

    function showResultsState() {
        optionsContainer.style.display = "none";
        resultsContainer.style.display = "flex";
    }

    async function fetchResults() {
        try {
            const response = await fetch('/api/enquete/resultados');
            if (response.ok) {
                const data = await response.json();
                updateProgressBars(data);
            }
        } catch (err) {
            console.error("Erro ao buscar resultados", err);
        }
    }

    function updateProgressBars(data) {
        const total = data.total || 1; // evitar divisão por zero
        const options = ['opcao_a', 'opcao_b', 'opcao_c'];
        
        options.forEach(opt => {
            const count = data[opt] || 0;
            const percentage = Math.round((count / total) * 100);
            
            const bar = document.getElementById(`progress-${opt}`);
            const pctText = document.getElementById(`pct-${opt}`);
            
            if (bar && pctText) {
                // Request animation frame for smoother transition if just rendered
                requestAnimationFrame(() => {
                    bar.style.width = `${percentage}%`;
                    pctText.textContent = `${percentage}%`;
                });
            }
        });
    }
});
