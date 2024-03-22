document.addEventListener("DOMContentLoaded", function() {
    // Function to handle navigation to another page
    function navigateToPage(url) {
        // Construct the URL relative to the pages directory
        let nextPageUrl = url;
        
        // Change the URL to the desired page
        window.location.href = nextPageUrl;
    }

    // Select the button in the other document and attach an event listener
    let buttonSignIn = document.querySelector('.signupbtn');
    if (buttonSignIn) {
        buttonSignIn.addEventListener('click', function() {
            // Call the navigateToPage function with the URL of the desired page
            navigateToPage("sign-up.html");
        });
    }
});