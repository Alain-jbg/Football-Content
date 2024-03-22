document.addEventListener("DOMContentLoaded", function() {
    let links = document.querySelectorAll('.navbar .nav-links a');
    let sections = document.querySelectorAll('main section');

    // Initially, show only the "Home" section
    let homeSection = document.getElementById('home');
    if (homeSection) {
        homeSection.style.display = "block";
        homeSection.classList.add('live');
    }

    // Function to handle navigation to another page
    function navigateToPage(url) {
        let nextPageUrl = "pages/" + url;
        // Change the URL to the desired page
        window.location.href = nextPageUrl;
    }


    links.forEach(function(link) {
        link.addEventListener('click', function(event) {  
            let targetSectionId = this.getAttribute('href').substring(1);
            let targetSection = document.getElementById(targetSectionId);
            
            if (targetSection) {
                event.preventDefault(); // Prevent default behavior for all links

                sections.forEach(function(section) {
                    section.classList.remove('live');
                    section.style.display = "none"; // Hide all sections
                });

                if (targetSectionId === 'home') {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                } else {
                    window.scrollTo({ top: targetSection.offsetTop, behavior: 'smooth' });
                    targetSection.style.display = "block"; // Show the target section
                    targetSection.classList.add('live');
                }

                links.forEach(function(link) {
                    link.classList.remove('active');
                });
                this.classList.add('active');
            }
        });
    });

    // Select your button and attach an event listener
    let buttonSignIn = document.querySelector('#sign-in');
    if (buttonSignIn) {
        buttonSignIn.addEventListener('click', function() {
            // Call the navigateToPage function with the URL of the desired page
            navigateToPage("login.html");
        });
    }
});
