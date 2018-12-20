function preloader() {
    document.getElementById("loading").style.display = "none";
    document.getElementById("content").style.display = "block";
}
window.onload = preloader;
