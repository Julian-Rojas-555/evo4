document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    form.addEventListener("submit", (e) => {

        const username = document.querySelector(
            'input[name="username"]'
        ).value.trim();

        const password = document.querySelector(
            'input[name="password"]'
        ).value.trim();

        if(username.length < 3){
            alert("El usuario debe tener al menos 3 caracteres");
            e.preventDefault();
            return;
        }

        if(password.length < 4){
            alert("La contraseña debe tener al menos 4 caracteres");
            e.preventDefault();
            return;
        }

    });

});