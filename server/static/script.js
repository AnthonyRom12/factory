function updateTimers() {
    $.get('/check_timer', function(data) {
        if (data.button_active) {
            $('#collect_button').prop('disabled', false);
            $('#collect_timer').text('');
        } else {
            $('#collect_button').prop('disabled', true);
            $('#collect_timer').text('Время до активации: ' + formatTime(data.time_until_collect));
        }

        $('#points').text(data.points);
        $('#total_points').text(data.total_points);

        if (data.time_until_upgrade > 0) {
            $('#upgrade_timer').text('Время до улучшения: ' + formatTime(data.time_until_upgrade));
        } else {
            $('#upgrade_timer').text('');
        }
    });
    setTimeout(updateTimers, 1000);
}

function formatTime(seconds) {
    let hours = Math.floor(seconds / 3600);
    let minutes = Math.floor((seconds % 3600) / 60);
    let secs = Math.floor(seconds % 60);
    return hours + 'ч ' + minutes + 'м ' + secs + 'с';
}

function collectPoints() {
    $.post('/collect', function(data) {
        if (data.success) {
            $('#total_points').text(data.total_points);
            $('#collect_button').prop('disabled', true);
        }
    });
}

function upgradeLevel() {
    $.post('/upgrade_level', function(data) {
        if (data.success) {
            $('#level').text(data.level);
            $('#total_points').text(data.total_points);
            alert('Уровень повышен!');
        } else {
            alert('Недостаточно баллов или улучшение доступно через 24 часа.');
        }
    });
}

function openModal() {
    document.getElementById("myModal").style.display = "block";
}

function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

$(document).ready(function() {
    updateTimers();
    // Закрытие модального окна при клике вне его
    window.onclick = function(event) {
        let modal = document.getElementById("myModal");
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});