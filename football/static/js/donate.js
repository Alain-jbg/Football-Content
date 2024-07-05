document.addEventListener('DOMContentLoaded', function () {
    var links = document.querySelectorAll('.navbar2 a');
    var sections = document.querySelectorAll('section');

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
            var targetSectionId = this.getAttribute('href').substring(1);
            var targetSection = document.getElementById(targetSectionId);
            targetSection.classList.add('live');
        });
    });
});
