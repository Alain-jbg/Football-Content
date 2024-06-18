let menu = document.querySelector('#menu-bars');
let navbar = document.querySelector('.navbar');
var links = document.querySelectorAll('.navbar a');
var sections = document.querySelectorAll('section');

menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

links.forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault(); 

        links.forEach(function(link) {
            link.classList.remove('active');
        });
        sections.forEach(function(section) {
            section.classList.remove('live');
        });

        this.classList.add('active');
        var targetSectionClass = this.getAttribute('href').substring(1);
        var targetSection = document.querySelector('.' + targetSectionClass);
        targetSection.classList.add('live');

        // Scroll to the top of the page
        window.scrollTo({ top: 0, behavior: 'smooth' });

    });
});

// Bottom footer navbar toggling
let footerLinks = document.querySelectorAll('.bottom-nav a');

footerLinks.forEach(function(footerLink) {
    footerLink.addEventListener('click', function(event) {
        event.preventDefault(); 

        var targetSectionId = this.getAttribute('href');
        var targetSection = document.querySelector(targetSectionId);

        sections.forEach(function(section) {
            section.classList.remove('live');
        });

        if (targetSection) {
            targetSection.classList.add('live');
        }

        links.forEach(function(navbarLink) {
            navbarLink.classList.remove('active');
        });

        links.forEach(function(navbarLink) {
            if (navbarLink.getAttribute('href') === targetSectionId) {
                navbarLink.classList.add('active');
            }
        });

        // Scroll to the top of the page
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});

 
// Event listeners for toggling content sections
fixturesLink.addEventListener("click", function(event) {
    event.preventDefault();
    resultsLink.classList.remove('active');
    fixturesLink.classList.add('active')
    toggleSection(fixturesSection);
});

resultsLink.addEventListener("click", function(event) {
    event.preventDefault();
    fixturesLink.classList.remove('active');
    resultsLink.classList.add('active')
    toggleSection(resultsSection);
});

// By default, show fixtures section
toggleSection(fixturesSection);
