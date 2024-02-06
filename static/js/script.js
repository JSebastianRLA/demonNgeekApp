const toggleSwitch = document.querySelector('input[type="checkbox"]');
const theme = document.getElementById('theme');

toggleSwitch.addEventListener('change', switchTheme);

function switchTheme(event) {
    if (event.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        theme.href = 'dark-theme.css'; // Cambiar a dark-theme.css si prefieres un archivo CSS separado para el modo oscuro
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        theme.href = 'styles.css'; // Cambiar a styles.css si prefieres volver al tema claro
    }
}
