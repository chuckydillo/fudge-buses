console.log("nav bar connected")

//navbar

document.addEventListener('DOMContentLoaded', function() {
    const navContainer = document.getElementById('navbar-container');
    const indexNavContainer = document.getElementById('index-navbar-container');


    if (userNavContainer) {
        fetch('navbar-user.html')
        .then(response => response.text())
        .then(data => {
            indexNavContainer.innerHTML = data;
        })
        .catch(error => console.error('Error loading the navbar:', error));
    }

    if (guestNavContainer) {
        fetch('navbar-guest.html')
        .then(response => response.text())
        .then(data => {
            navContainer.innerHTML = data;
        })
        .catch(error => console.error('Error loading the navbar:', error));
    }

});