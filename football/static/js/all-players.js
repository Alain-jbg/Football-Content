document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('playerSearch');
    const playersTable = document.getElementById('playersTable').getElementsByTagName('tr');
    const resetButton = document.getElementById('resetFilters');
    const seasonFilter = document.getElementById('season');
    const clubFilter = document.getElementById('club');

    function filterPlayers() {
        const filter = searchInput.value.toLowerCase();
        for (let i = 0; i < playersTable.length; i++) {
            const playerName = playersTable[i].getElementsByTagName('td')[0].textContent.toLowerCase();
            if (playerName.includes(filter)) {
                playersTable[i].style.display = '';
            } else {
                playersTable[i].style.display = 'none';
            }
        }
    }

    function resetFilters() {
        searchInput.value = '';
        seasonFilter.value = '2024/25';
        filterPlayers();
    }

    searchInput.addEventListener('input', filterPlayers);
    resetButton.addEventListener('click', resetFilters);

    // Initialize filters on load
    resetFilters();
});
