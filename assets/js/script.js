document.addEventListener('DOMContentLoaded', () => { // Correctly closed parentheses here
    const cells = document.querySelectorAll('.cell');
    const message = document.getElementById('message');
    let isPlayerVsBot = false;
    let currentPlayer = 'X';
    let board = Array(9).fill(null);
    let gameActive = true;

    const winningCombinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    document.getElementById('player-vs-player').addEventListener('click', () => {
        resetGame();
        isPlayerVsBot = false;
    });

    document.getElementById('player-vs-bot').addEventListener('click', () => {
        resetGame();
        isPlayerVsBot = true;
    });

    cells.forEach(cell => {
        cell.addEventListener('click', handleCellClick);
    });

    function handleCellClick(event) {
        const index = event.target.getAttribute('data-index');

        if (!board[index] && gameActive) {
            board[index] = currentPlayer;
            event.target.textContent = currentPlayer;

            if (checkWinner()) {
                message.textContent = `${currentPlayer} wins!`; 
                gameActive = false;
                return;
            }

            if (board.every(cell => cell !== null)) {
                message.textContent = 'Draw!';
                gameActive = false;
                return;
            }

            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';

            if (isPlayerVsBot && currentPlayer === 'O' && gameActive) {
                botMove();
            }
        }
    }

    function botMove() {
        let availableCells = board
        .map((cell, index) => (cell === null ? index : null))
        .filter(index => index !== null);

        let randomIndex = availableCells[Math.floor(Math.random() * availableCells.length)];

        board[randomIndex] = 'O';
        cells[randomIndex].textContent = 'O';

        if (checkWinner()) {
            message.textContent = 'O wins!';
            gameActive = false;
            return;
        }

        if (board.every(cell => cell !== null)) {
            message.textContent = 'Draw!';
            gameActive = false;
            return;
        }

        currentPlayer = 'X';
    }

    function checkWinner() {
        return winningCombinations.some(combination => {
            return combination.every(index => board[index] === currentPlayer);
        });
    }

    function resetGame() {
        board.fill(null);
        cells.forEach(cell => (cell.textContent = ''));
        currentPlayer = 'X';
        message.textContent = '';
        gameActive = true;
    }
});
