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

//Contact us form
let submitForm = document.getElementById("submit-form");
submitForm.addEventListener("submit", (e) => {
    e.preventDefault();
    let emailAddress = document.getElementById("email-textbox");
    var regExpression = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+/;
    if(emailAddress.value.match(regExpression)){
        alert("Successful")
    } else {
        document.querySelector("#email-textbox").style.border = "1px solid hsl(4, 100%, 67%)";
        document.querySelector("#email-textbox").style.color = "hsl(4, 100%, 67%)";
        //document.querySelector("span").classList.add("fail-email");
        //document.querySelector("span").classList.add("active");
        setTimeout(function() {
            document.querySelector("span").classList.remove("active");
            document.querySelector("#email-textbox").style.color = "black";
            document.querySelector("#email-textbox").style.border = "1px solid hsl(231, 7%, 60%)";

        }, 2000);
    }
    
});

// Function to toggle visibility of fixtures and results sections
const fixturesLink = document.getElementById("fixtures-link");
const resultsLink = document.getElementById("results-link");
const fixturesSection = document.getElementById("fixtures-section");
const resultsSection = document.getElementById("results-section");

function toggleSection(sectionToShow) {
    const sections = [fixturesSection, resultsSection];
    sections.forEach(section => {
        section.style.display = "none";
    });
    sectionToShow.style.display = "block";
}

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
