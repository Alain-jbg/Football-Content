const TICKET_PRICE = 100;
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

document.getElementById("cont").addEventListener("click", function (event) {
    event.preventDefault(true);
    inputValidation();
});

function inputValidation() {
    const firstName = document.getElementById('first-name');
    const lastName = document.getElementById('last-name');
    const email = document.getElementById('email');

    if(!firstName.value) {
        //alert('Please enter your first name.');
        firstName.style.border = "1px solid hsl(4, 100%, 67%)";
        document.getElementById("first-name-error").classList.add("active");
        setTimeout(function() {
            document.getElementById("first-name-error").classList.remove("active");
            firstName.style.color = "black";
            firstName.style.border = "1px solid #ccc";

        }, 2000);

    } else if (!lastName.value) {
        lastName.style.border = "1px solid hsl(4, 100%, 67%)";
        document.getElementById("last-name-error").classList.add("active");
        setTimeout(function() {
            document.getElementById("last-name-error").classList.remove("active");
            lastName.style.color = "black";
            lastName.style.border = "1px solid #ccc";

        }, 2000);

    } else if (!email.value.match(emailRegex)) {
        email.style.border = "1px solid hsl(4, 100%, 67%)";
        document.getElementById("email-error").classList.add("active");
        setTimeout(function() {
            document.getElementById("email-error").classList.remove("active");
            email.style.color = "black";
            email.style.border = "1px solid #ccc";

        }, 2000);

    }  else { 
        window.location.href = payUrl;
    }
}

        // function updateSummary() {
        //     const quantity = document.getElementById('quantity').value || 0;
        //     const ticketPrice = quantity * TICKET_PRICE;

        //     document.getElementById('ticketCount').textContent = quantity;
        //     document.getElementById('ticketPrice').textContent = ticketPrice.toFixed(2);
        //     document.getElementById('totalPrice').textContent = ticketPrice.toFixed(2);

        //     updateTicketInfoFields(quantity);
        // }
//const quantity_val = quantity.value;

// function updateTicketInfoFields() {
//     const container = document.getElementById('ticket-info-container');
//     const quantity = document.getElementById('quantity');
//     const quantity_val = quantity.value;
//     container.innerHTML = '';

//     for (let i = 1; i <= quantity_val; i++) {
//         container.innerHTML += `
//             <div class="ticket-info">
//                 <h2>Ticket Holder ${i} Details</h2>
//                 <div class="form-group">
//                     <div>
//                         <label for="ticket-first-name-${i}">First Name</label>
//                         <input type="text" id="ticket-first-name-${i}" name="ticket-first-name-${i}" placeholder="First Name">
//                     </div>
//                     <div>
//                         <label for="ticket-last-name-${i}">Last Name</label>
//                         <input type="text" id="ticket-last-name-${i}" name="ticket-last-name-${i}" placeholder="Last Name">
//                     </div>
//                 </div>
//                 <div class="form-group">
//                     <div style="width: 100%;">
//                         <label for="ticket-email-${i}">Email Address</label>
//                         <input type="email" id="ticket-email-${i}" name="ticket-email-${i}" placeholder="Email Address">
//                     </div>
//                 </div>
//             </div>
//         `;
//     }
// }

// quantity.addEventListener('change', () => {
//     const quantityVal = parseInt(quantity.value);
//     updateTicketInfoFields(quantityVal);
// });

        // function copyBuyerDetails() {
        //     const firstName = document.getElementById('first-name').value;
        //     const lastName = document.getElementById('last-name').value;
        //     const email = document.getElementById('email').value;
        //     const quantity = document.getElementById('quantity').value || 0;

        //     for (let i = 1; i <= quantity; i++) {
        //         document.getElementById(`ticket-first-name-${i}`).value = firstName;
        //         document.getElementById(`ticket-last-name-${i}`).value = lastName;
        //         document.getElementById(`ticket-email-${i}`).value = email;
        //     }
        // }

        // function proceedToPayment() {
        //     // Add validation and redirection logic for payment here
        //     alert('Proceeding to payment');
        // }