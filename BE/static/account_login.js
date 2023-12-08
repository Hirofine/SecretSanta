var api_url = "https://secretsanta.hirofine.fr"

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const usernameInput = document.getElementById("name-input");
    const passwordInput = document.getElementById("password-input");
    const submit_button = document.getElementById("submit-button");

    const cgu_check = document.getElementById("cgu-checkbox");

    form.addEventListener("submit", function (event) {
       
        event.preventDefault(); // Empêchez la soumission du formulaire par défaut
        if (!cgu_check.checked){
            alert("Vous devez accepter les conditions d'utilisations");
            return;
        }
        // Récupérez les données du formulaire
        const pseudo = usernameInput.value;
        const passw = passwordInput.value;

     
        const userData = {
            pseudo: pseudo,
            passw: passw
        };

        fetch(api_url + "/login/", {
            method: "POST",
            body: JSON.stringify(userData),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data["message"] == "Connexion réussie"){
                window.location.href = "https://secretsanta.hirofine.fr/reveal";
            }else{
                console.log("c'est la merder");
            }
            
            
        })
        .catch(error => {
            console.log(error)
            // Gérez les erreurs (par exemple, problème de connectivité avec le serveur)
        });
    
    });
});