content_div = document.getElementById('content')
sidebar_div = document.getElementById('sidebar')

hamburger = document.getElementById('hamburger')

content_div.addEventListener("click", () => {
    if ((sidebar_div.style.display !== 'none') && (document.documentElement.clientWidth < 437)) {

        sidebar_div.style.display = 'none';
    }
})
hamburger.addEventListener("click", () => {
    if ((sidebar_div.style.display !== 'none') && (document.documentElement.clientWidth > 437)) {
        sidebar_div.style.display = 'none';
    } else {
        sidebar_div.style.display = 'unset';
    }
})




