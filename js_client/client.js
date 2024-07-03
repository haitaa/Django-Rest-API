const loginForm = document.getElementById("login-form");
const baseEndpoint = "http://localhost:8000/api";
if (loginForm) {
    // handle this login form
    loginForm.addEventListener("submit", handleLogin);
}

function handleLogin(event) {
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}/token/`;
    let loginFormData = new FormData(loginForm);
    let loginObjectData = Object.fromEntries(loginFormData);
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(loginObjectData),
    };
    fetch(loginEndpoint, options)
        .then((response) => {
            return response.json();
        })
        .then((x) => {
            console.log(x);
        })
        .catch((err) => {
            console.log("err", err);
        });
}
