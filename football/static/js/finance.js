document.addEventListener('DOMContentLoaded', function() {
    const revenue = 50;
    const expenses = 0;
    const balance = revenue - expenses;

    document.getElementById('revenue').textContent = `$${revenue.toLocaleString()}`;
    document.getElementById('expenses').textContent = `$${expenses.toLocaleString()}`;
    document.getElementById('profit').textContent = `$${balance.toLocaleString()}`;

    const ctx = document.getElementById('financialChart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Revenue', 'Expenses', 'Balance'],
            datasets: [{
                label: 'Amount in $',
                data: [revenue, expenses, balance],
                backgroundColor: ['#36a2eb', '#ff6384', '#4caf50']
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});
