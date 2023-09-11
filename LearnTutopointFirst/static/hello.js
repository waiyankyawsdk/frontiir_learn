var switch_count = 0;
function greeting() {
    var today = new Date();
    var hour = today.getHours();
    var minute = today.getMinutes();
    var second = today.getSeconds();
    var msg = "";
    switch_count++;
    if (switch_count == 1) {
        switch (true) {
            case hour < 12:
                msg = "Good Morning, ";
                break;
            case hour >= 12 && h < 18:
                msg = "Good Afternoon, ";
                break;
            default:
                msg = "Good Evening, ";
                break;
        }
        var text = document.getElementById('ttl').innerHTML;
        document.getElementById('ttl').innerHTML = msg + text;
    }
    document.getElementById('time').innerHTML = `${(formatTime(hour))}:${formatTime(minute)}:${formatTime(second)}`;

}
const formatTime = time => time.toString().padStart(length = 2, '0');
setInterval(greeting, 1000)