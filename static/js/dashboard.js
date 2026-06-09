document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    form.addEventListener("submit", (e) => {

        const edad = parseInt(
            document.querySelector(
                'input[name="edad"]'
            ).value
        );

        const peso = parseFloat(
            document.querySelector(
                'input[name="peso"]'
            ).value
        );

        const grasa = parseFloat(
            document.querySelector(
                'input[name="grasa"]'
            ).value
        );

        if(edad < 10 || edad > 100){
            alert("Edad inválida");
            e.preventDefault();
            return;
        }

        if(peso <= 0){
            alert("Peso inválido");
            e.preventDefault();
            return;
        }

        if(grasa < 0 || grasa > 60){
            alert("Porcentaje de grasa inválido");
            e.preventDefault();
            return;
        }

    });

});