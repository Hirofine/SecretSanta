// var api_url = "https://secretsanta.hirofine.fr"
var api_url = "https://dev.secretsanta.hirofine.fr";

var reveal_div = document.getElementById("reveal-div");
const text = document.getElementById("text");
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


function pause(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function update_page(is_connected){
    switch(is_connected){
        case true:
            reveal_div.style.display = "inline";
            text.innerHTML = "Tu es le Papou Noël Secret de "
            a = await retrieve_receiver();
            b = await retrieve_firstgift();
            c = await retrieve_secondgift();
            

            

            name_length = a["pseudo"].length;
            for (i = 0; i<name_length; i++){
                var slot = document.createElement("span");
                slot.id = "slot" + i;
                reveal_div.appendChild(slot);
            }
            const slots = document.querySelectorAll('span');
           
            
            
            const startTime = Date.now();
            is_res = false;
            var delta = 500;
            while(!is_res){
                await pause(10);
                const currentTime = Date.now();
                const elapsedTime = currentTime - startTime;
                for (let i = 0; i < a["pseudo"].length; i++) {
                    if (elapsedTime >= delta * (i + 1)){
                        slots[i].textContent = a["pseudo"].charAt(i);
                    }else{
                        slots[i].textContent = randomChar(); // Affiche une lettre aléatoire
                    }
                }
                // Si tous les chars se sont affichés, sortir de la boucle
                if (elapsedTime >= delta * (name_length + 1)) {
                    is_res = true;
                break;
                }
            } 
            

            


            const smallgift_div = document.createElement("div");
                
            function createGiftDiv(text, name){
                const gift_div = document.createElement("div");
                const gift_text = document.createElement("div");

                gift_text.innerHTML = text;

                // creation de la boite cadeau
                const gift_box = document.createElement("div");
                gift_box.className = "gift-box";
                gift_box.innerHTML = "Cliquer pour déballer";

                gift_box.onclick = function () {
                    gift_box.innerHTML = name;
                    gift_box.classList.add("revealed");
                };

                gift_div.appendChild(gift_text);
                gift_div.appendChild(gift_box);

                return gift_div;
            }

            const firstgift_div = createGiftDiv("Ton premier petit cadeau est pour:", b["pseudo"]);
            const secondgift_div = createGiftDiv("Ton second petit cadeau est pour:", c["pseudo"]);

            smallgift_div.appendChild(firstgift_div);
            smallgift_div.appendChild(secondgift_div);

            reveal_div.appendChild(smallgift_div);

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

function randomChar() {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'; // Liste des caractères possibles
    return alphabet.charAt(Math.floor(Math.random() * alphabet.length));
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

async function retrieve_firstgift(){
    try{
        const response = await fetch(api_url + `/firstgift/`, {
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
        return [];
    }
}

async function retrieve_secondgift(){
    try{
        const response = await fetch(api_url + `/secondgift/`, {
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
        return [];
    }
}
