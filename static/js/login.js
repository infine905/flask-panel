const passwordInput = document.getElementById("password");
const confirmPasswordInput = document.getElementById("confirm_password");
const passwordMessageItems = document.getElementsById("password-message-item"); 
const passwordMessage = document.getElementById("password-message"); 
const submitRegisterButton = document.getElementById("submit_register");

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

passwordInput.oninput = function () { 
    // Cheching passwords do match
    if (passwordInput.value === confirmPasswordInput.value && passwordInput.value != "") {  
        passwordMessageItems[1].classList.remove("invalid"); 
        passwordMessageItems[1].classList.add("valid");
        submitRegisterButton.disabled = false; 
    } else { 
        passwordMessageItems[1].classList.remove("valid"); 
        passwordMessageItems[1].classList.add("invalid");
        submitRegisterButton.disabled = true
    }
}

confirmPasswordInput.oninput = function () {
    // Cheching passwords do match
    if (passwordInput.value === confirmPasswordInput.value && confirmPasswordInput.value != "") {
        passwordMessageItems[1].classList.remove("invalid"); 
        passwordMessageItems[1].classList.add("valid");
        submitRegisterButton.disabled = false
    } else { 
        passwordMessageItems[1].classList.remove("valid"); 
        passwordMessageItems[1].classList.add("invalid");
        submitRegisterButton.disabled = true
    }
}