// for your JavaScript

// mostly stackOverflow snippets/references
function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("typePasswordX").value;
    var errorMessage = "";

    if (username.trim() === "" && password.trim() === "") {
      errorMessage = "Please enter both username and password!";
    } else if (username.trim() === "") {
      errorMessage = "Please enter a username!";
    } else if (password.trim() === "") {
      errorMessage = "Please enter a password!";
    }

    if (errorMessage !== "") {
      alert(errorMessage);
      return false;
    }

    return true;
  }

  document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("loginForm");
    form.addEventListener("submit", function(event) {
      if (!validateForm()) {
        event.preventDefault();
      }
    });
  });

function validateRegistrationForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm_password").value;

    // Validate password and confirm password equality
    if (password !== confirmPassword) {
    alert("Passwords do not match!");
      return false;
    }

    // Validate password length and complexity
    if (password.length < 8) {
      alert("Password should be at least 8 characters long!");
      return false;
    }

    // Regular expressions to check for capital letter and symbol
    //Found with help of StackOverflow (Not directly copied)
    var capitalLetterRegex = /[A-Z]/;
    var symbolRegex = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;

    // Check if password contains at least one capital letter and one symbol
    if (!capitalLetterRegex.test(password) || !symbolRegex.test(password)) {
      alert("Password should contain at least one capital letter and one symbol!");
      return false;
    }

    return true;
  }

function validateFormDiscover() {
    var q1 = document.forms["myForm"]["q1"].value;
    var q2 = document.forms["myForm"]["q2"].value;
    var q3 = document.forms["myForm"]["q3"].value;
    var q4 = document.forms["myForm"]["q4"].value;
    var q5 = document.forms["myForm"]["q5"].value;

    if (q1 === "" || q2 === "" || q3 === "" || q4 === "" || q5 === "") {
        alert("Please answer all questions.");
        return false;
    }
}

function validateFormPrompt() {
  var maxTokensInput = document.getElementById("maxTokens");
  var maxTokensValue = maxTokensInput.value.trim();

  var promptInput = document.getElementById("prompt");
  var promptValue = promptInput.value.trim();

  // Check if maxTokensValue is not a number
  if (isNaN(maxTokensValue)) {
    alert("Please enter a valid number for Max Tokens.");
    maxTokensInput.focus();
    return false;
  }

  // Convert maxTokensValue to a number
  var maxTokensNumber = parseInt(maxTokensValue);

  // Check if maxTokensNumber is not a positive number
  if (maxTokensNumber <= 0) {
    alert("Please enter a positive number for Max Tokens.");
    maxTokensInput.focus();
    return false;
  }

  // Check if promptValue is empty
  if (promptValue === "") {
    alert("Please fill out the prompt area.");
    promptInput.focus();
    return false;
  }

  // All validations passed
  return true;
}