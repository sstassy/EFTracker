function performLogin() {
    var username = document.getElementById("email").value;
    var password = document.getElementById("psw").value;

    if (username === "pippin@gmail.com" && password === "pippin") {
        alert("Login successful!");
        updateNavigationAfterLogin();
        window.location.href = "emergency.html"; // Redirect to the Emergency page
    } else {
        alert("Invalid username or password.");
    }
}

function updateNavigationAfterLogin() {
    var loginNavItem = document.getElementById("loginNavItem");
    if (loginNavItem) {
        loginNavItem.innerHTML = "<a href='account.html'>Account</a>";
    }
}
