let navbar = document.querySelector('.navbar');
var links = document.querySelectorAll('.navbar a');
var sections = document.querySelectorAll('section');
let menu = document.querySelector('#menu-bars');

const fixturesLink = document.getElementById("fixtures-link");
const resultsLink = document.getElementById("results-link");

const fixturesSection = document.getElementById("fixtures-section");
const resultsSection = document.getElementById("results-section");

menu.onclick = () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

links.forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault(true);
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

        // Scroll to the top of the target section
        window.scrollTo({ top: 0, behavior: 'smooth' });

        // Close the navbar after a link is clicked
        menu.classList.remove('fa-times');
        navbar.classList.remove('active');
    });
});

// Function to toggle visibility of matches sections
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

//Filter fixtures by competition
const competitionSelect = document.getElementById("competition-select");
const fixturesContainer = document.getElementById("fixtures-container");

// Function to filter fixtures by competition
function filterFixturesByCompetition(competition) {
    const fixtures = fixturesContainer.querySelectorAll(".fixture");
    fixtures.forEach(fixture => {
        const fixtureCompetition = fixture.getAttribute("data-competition");
        if (competition === "all" || competition === fixtureCompetition) {
                fixture.style.display = "block";
        } else {
            fixture.style.display = "none";
        }
    });
}

// Event listener for dropdown change
competitionSelect.addEventListener("change", function() {
    const selectedCompetition = competitionSelect.value;
    filterFixturesByCompetition(selectedCompetition);
});

// Job listings
/* const jobSearchInput = document.querySelector(".job-search");
const jobsContainer = document.querySelector(".jobs");
const noMatch = document.getElementById("no-match");

jobSearchInput.addEventListener("input", (e) => {
    const searchTerm = e.target.value.toLowerCase().trim();

    const jobs = Array.from(jobsContainer.querySelectorAll(".job"));
    let matchFound = false; 

    jobs.forEach((job) => {
        const title = job.querySelector(".job-title").textContent.toLowerCase();

        if (title.includes(searchTerm)) {
            job.style.display = "flex";
            matchFound = true; 
        } else {
            job.style.display = "none";
        }
    });

    // Display "no match" message if no jobs match the search term
    if (!matchFound) {
        noMatch.style.display = "block";
    } else {
        noMatch.style.display = "none";
    }
}); */


/* function redirectToStaffPage(jobTitle) {
    // Redirect to job details page with job title as a parameter
    window.location.href = `job-listing/club1-job.html?job=${encodeURIComponent(jobTitle)}`;
} */