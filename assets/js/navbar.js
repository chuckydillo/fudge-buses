console.log("nav bar connected")

//navbar

document.addEventListener('DOMContentLoaded', function() {
    const navContainer = document.getElementById('navbar-container');
    const indexNavContainer = document.getElementById('index-navbar-container');


    if (userNavContainer) {
        fetch('/pages/navbar-user.html')
        .then(response => response.text())
        .then(data => {
            userNavContainer.innerHTML = data;
        })
        .catch(error => console.error('Error loading the navbar:', error));
    }

    if (guestNavContainer) {
        fetch('/pages/navbar-guest.html')
        .then(response => response.text())
        .then(data => {
            guestNavContainer.innerHTML = data;
        })
        .catch(error => console.error('Error loading the navbar:', error));
    }

});