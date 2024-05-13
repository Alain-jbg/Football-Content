let navbar = document.querySelector('.navbar');
var links = document.querySelectorAll('.navbar a');
var sections = document.querySelectorAll('section');

const fixturesLink = document.getElementById("fixtures-link");
const resultsLink = document.getElementById("results-link");

const fixturesSection = document.getElementById("fixtures-section");
const resultsSection = document.getElementById("results-section");

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