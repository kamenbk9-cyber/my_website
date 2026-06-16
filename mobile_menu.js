var btn = document.getElementById("mobile_menu");
btn.addEventListener("click", openMobileMenu);
var menu = document.getElementById("navig");
var flag;
if (getComputedStyle(menu).display == "none"){
    flag = true;
}
else {flag = false;}
function openMobileMenu() {
    if (flag) {
        menu.style.display = "flex";
        flag = false;
    }
    else {
        menu.style.display = "none";
        flag = true;
    }
    }
