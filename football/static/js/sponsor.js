document.getElementById('sponsorshipForm').addEventListener('submit', function(e) {
    e.preventDefault();
    let emailAddress = document.getElementById("contactEmail");
    let name = document.getElementById("contactName");
    let companyName = document.getElementById("companyName");
    let message = document.getElementById("message");

    let emailValid = /^[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/.test(emailAddress.value);
    let nameValid = name.value.trim() !== "";
    let compNameValid = companyName.value.trim() !== "";
    let messageValid = message.value.trim() !== "";

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

    if (!compNameValid) {
        companyName.style.border = "1px solid hsl(4, 100%, 67%)";
        companyName.style.color = "hsl(4, 100%, 67%)";
        document.getElementById("issue-invalid").style.display = "block";
        setTimeout(() => {
            document.getElementById("issue-invalid").style.display = "none";
            companyName.style.color = "black";
            companyName.style.border = "1px solid hsl(231, 7%, 60%)";
        }, 2000);
    } else {
        companyName.style.border = "1px solid hsl(231, 7%, 60%)";
        companyName.style.color = "black";
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
    if (!messageValid) {
        message.style.border = "1px solid hsl(4, 100%, 67%)";
        message.style.color = "hsl(4, 100%, 67%)";
        document.getElementById("issue-invalid").style.display = "block";
        setTimeout(() => {
            document.getElementById("issue-invalid").style.display = "none";
            message.style.color = "black";
            message.style.border = "1px solid hsl(231, 7%, 60%)";
        }, 2000);
    } else {
        message.style.border = "1px solid hsl(231, 7%, 60%)";
        message.style.color = "black";
    }


    if (emailValid && nameValid && messageValid && compNameValid) {
        window.location.href = "../pages/finance/sponsor-success.html";
    }
});