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
