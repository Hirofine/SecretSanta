var api_url = "https://be.magimathicart.hirofine.fr"
var reveal_div = document.getElementById("reveal-div");
document.addEventListener("DOMContentLoaded", function () {

    
    console.log("loaded page");
    fetch(api_url + `/verify-session/`,{
        method: 'GET',
        credentials: 'include'
    })
            .then(response => response.json())
            .then(data => {
               console.log(data);
               console.log(data.data);
               update_page(data.data)
            })
            .catch(error => {
                console.error("Erreur lors de la vérification du pseudo : " + error);
            });

});

async function update_page(is_connected){
    switch(is_connected){
        case true:
            reveal_div.style.display = "block";
            a = await retrieve_receiver();
            reveal_div.innerHTML = "Tu es Secret Santa de " + a["pseudo"];
            console.log("case true");
            break;
        case false:
            reveal_div.style.display = "none";
            console.log("case false");
            break;
        default:
            
            console.log("case default");
            break;
       }
}

async function retrieve_receiver(){
    try {
        const response = await fetch(api_url + `/userCadeau/`, {
            method: 'GET',
            credentials: 'include'
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log("data :", data);
        
        
        return data;
    } catch (error) {
        console.error("Erreur lors de la vérification du pseudo : " + error);
        return []; // Retourne une liste vide en cas d'erreur
    }
}