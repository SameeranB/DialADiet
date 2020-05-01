function setSidebarWidth() {
    let width;
    if (document.documentElement.clientWidth > 437) {
        width = document.getElementById('logo-wrapper').offsetWidth;
        document.getElementById('inner-body').style.gridTemplateColumns = `${width}px auto`;
    }
}
setSidebarWidth()

window.onresize = setSidebarWidth;