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

        // Close the navbar after a link is clicked
        menu.classList.remove('fa-times');
        navbar.classList.remove('active');
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

/*let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}*/

//Contact us
let submitForm = document.getElementById("submit-form");
submitForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let emailAddress = document.getElementById("email-textbox");
    let name = document.getElementById("name-textbox");
    let issue = document.getElementById("issue-textarea");

    let emailValid = /^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/.test(emailAddress.value);
    let nameValid = name.value.trim() !== "";
    let issueValid = issue.value.trim() !== "";

    // Email validation
    if (!emailValid) {
        emailAddress.style.border = "1px solid hsl(4, 100%, 67%)";
        emailAddress.style.color = "hsl(4, 100%, 67%)";
        document.getElementById("email-invalid").style.display = "block";
        setTimeout(() => {
            document.getElementById("email-invalid").style.display = "none";
            emailAddress.style.color = "black";
            emailAddress.style.border = "1px solid hsl(231, 7%, 60%)";
        }, 2000);
    } else {
        emailAddress.style.border = "1px solid hsl(231, 7%, 60%)";
        emailAddress.style.color = "black";
    }

    // Name validation
    if (!nameValid) {
        name.style.border = "1px solid hsl(4, 100%, 67%)";
        name.style.color = "hsl(4, 100%, 67%)";
        document.getElementById("name-invalid").style.display = "block";
        setTimeout(() => {
            document.getElementById("name-invalid").style.display = "none";
            name.style.color = "black";
            name.style.border = "1px solid hsl(231, 7%, 60%)";
        }, 2000);
    } else {
        name.style.border = "1px solid hsl(231, 7%, 60%)";
        name.style.color = "black";
    }

    // Issue validation
    if (!issueValid) {
        issue.style.border = "1px solid hsl(4, 100%, 67%)";
        issue.style.color = "hsl(4, 100%, 67%)";
        document.getElementById("issue-invalid").style.display = "block";
        setTimeout(() => {
            document.getElementById("issue-invalid").style.display = "none";
            issue.style.color = "black";
            issue.style.border = "1px solid hsl(231, 7%, 60%)";
        }, 2000);
    } else {
        issue.style.border = "1px solid hsl(231, 7%, 60%)";
        issue.style.color = "black";
    }

    if (emailValid && nameValid && issueValid) {
        var textPass = encodeURIComponent(emailAddress.value);
        window.location.href = "pages/success.html?value=" + textPass;
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
