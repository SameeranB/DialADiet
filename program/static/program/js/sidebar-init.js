function setSidebarWidth() {
    let width;
    if (document.documentElement.clientWidth > 437) {
        width = document.getElementById('logo-wrapper').offsetWidth;
        document.getElementById('inner-body').style.gridTemplateColumns = `${width}px auto`;
    }
}

setSidebarWidth()

function setPulloutPosition() {
    let width = document.getElementById('sidebar').offsetWidth
    if (width === 0) {
        document.getElementById('sidebar-pullout').style.left = `0px`
        document.getElementById('sidebar-pullout').innerText = "Menu"

    } else {
        document.getElementById('sidebar-pullout').style.left = `${width}px`
        document.getElementById('sidebar-pullout').innerText = "Close"

    }
}

function toggleSidebar() {
    let sidebar_div = document.getElementById('sidebar')
    if (sidebar_div.style.display !== 'grid') {
        sidebar_div.style.display = 'grid';
    } else {
        sidebar_div.style.display = 'none';
    }
    setPulloutPosition()

}
