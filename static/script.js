document.addEventListener('DOMContentLoaded', () => {
    const mineBtn = document.getElementById('mineBtn');
    
    mineBtn.addEventListener('click', async () => {
        try {
            const response = await fetch('/api/mine', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const result = await response.json();
            alert(`Block #${result.index} mined!\nHash: ${result.hash.slice(0, 16)}...`);
        } catch (error) {
            console.error('Mining error:', error);
        }
    });
});
