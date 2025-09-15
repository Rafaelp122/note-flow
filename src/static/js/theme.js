// Recupera tema do localStorage ou usa 'light'
const storedTheme = localStorage.getItem("theme") || "light";
document.documentElement.setAttribute("data-bs-theme", storedTheme);

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

    // Define ícone inicial
    icon.className = storedTheme === "light" ? "bi bi-moon-fill" : "bi bi-sun-fill";

    btn.addEventListener("click", () => toggleTheme(icon));
});