content_div = document.getElementById('content')
sidebar_div = document.getElementById('sidebar')

hamburger = document.getElementById('hamburger')

content_div.addEventListener("touchstart", () => {
    if (sidebar_div.style.display !== 'none') {
        sidebar_div.style.display = 'none';
        setPulloutPosition()
    }
})





