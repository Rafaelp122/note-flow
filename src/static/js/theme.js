// Função para alternar tema e atualizar ícone
function toggleTheme(iconElement) {
    const current = document.documentElement.getAttribute("data-bs-theme");
    const next = current === "light" ? "dark" : "light";
    document.documentElement.setAttribute("data-bs-theme", next);
    localStorage.setItem("theme", next);
    iconElement.className = next === "light" ? "bi bi-moon-fill" : "bi bi-sun-fill";
}

// Executa quando o DOM estiver pronto
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("theme-toggle");
    const icon = document.getElementById("theme-icon");

    if (btn && icon) {
        // Define o ícone inicial com base no tema que já foi carregado
        const initialTheme = document.documentElement.getAttribute("data-bs-theme");
        icon.className = initialTheme === "light" ? "bi bi-moon-fill" : "bi bi-sun-fill";

        // Adiciona o evento de clique
        btn.addEventListener("click", () => toggleTheme(icon));
    }
});
