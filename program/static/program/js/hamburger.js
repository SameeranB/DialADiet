hamburger = document.getElementById('hamburger')
sidebar_div = document.getElementById('sidebar')


hamburger.addEventListener("click", () => {
    if ((sidebar_div.style.display !== 'none') && (document.documentElement.clientWidth > 437)) {
        sidebar_div.style.display = 'none';
    } else {
        sidebar_div.style.display = 'grid';
    }
})