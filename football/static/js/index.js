// Match poster sliding effect
var dots = document.querySelectorAll('.dot');
var matches = document.querySelectorAll('.slider .match');
var currentMatch = 0; // index of the first match 
const interval = 3000; // duration (speed) of the slide

// Change slide based on the dot clicked
dots.forEach(dot => {
    dot.addEventListener('click', function () {
        clearInterval(timer); // Stop automatic sliding
        currentMatch = Array.from(dots).indexOf(dot); // Find the index of the clicked dot
        changeSlide(currentMatch); // Show corresponding slide
        timer = setInterval(() => changeSlide(), interval); // Restart the timer
    });
});

function changeSlide(n) {
    if (n !== undefined) {
        currentMatch = n; // Use the provided index
    } else {
        currentMatch = (currentMatch + 1) % matches.length; // Move to the next slide in the loop
    }

    var slides = document.querySelector('.slides');
    slides.style.transform = `translateX(-${currentMatch * 100}%)`; // Shift slides horizontally

    // Update active dot
    dots.forEach(dot => dot.classList.remove('active'));
    dots[currentMatch].classList.add('active'); // Highlight the active dot
}

// Start automatic sliding
var timer = setInterval(() => changeSlide(), interval);

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

// Function to toggle game highlights and blogs sections
const gamesLink = document.getElementById("games-link");
const blogsLink = document.getElementById("blogs-link");
const highlightsSection = document.getElementById("highlights-section");
const blogsSection = document.getElementById("blogs-section");

function toggleSectionBlog(sectionToShow) {
    const sections = [highlightsSection, blogsSection];
    sections.forEach(section => {
        section.style.display = "none";
    });
    sectionToShow.style.display = "grid";
}

// Event listeners for toggling content sections
gamesLink.addEventListener("click", function(event) {
    event.preventDefault();
    blogsLink.classList.remove('active');
    gamesLink.classList.add('active')
    toggleSectionBlog(highlightsSection);
});

blogsLink.addEventListener("click", function(event) {
    event.preventDefault();
    gamesLink.classList.remove('active');
    blogsLink.classList.add('active')
    toggleSectionBlog(blogsSection);
});

// By default, show fixtures highlights
toggleSectionBlog(highlightsSection);