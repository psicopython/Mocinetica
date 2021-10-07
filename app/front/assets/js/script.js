
const notFound = `
<article class="err">
    <h2 class="err-items">404 Não Encontrado</h2>
    <span class="err-items">Acho que vc ta meio perdido, parça</span><br>
    <span class="err-items">Tem carro com esse ID não</span><br>
</article>`;

const peraAe = `<div id="peraAe">
<h1>Pera Aê, só um minuto!</h1>
<img src="/assets/img/loading.gif" alt="loading gif">
</div>`

window.onpopstate = function(e) {

    if( e.state ) {
        console.log("chamou aq, pô")
        switch (e.state.func) {
            case "getCarByYear":
                getCarByYear(
                    e.state.data.brand,
                    e.state.data.carName,
                    e.state.data.carYear
                    );
                break;

            case "getCarByName":
                getCarByName(e.state.data.brand, e.state.data.carName);
                break;

            case "listCars":
                listCars( e.state.data.brand );
                break;

            case "listBrands":
            default:
                listBrands();
                break;
        }
    }
    return null;
}


function loading(opt) {
    div = document.getElementById("peraAe")
    if ( opt == "show" ) {
        div.style.display = "flex"
    } else if ( opt == "hidden" ){
        div.style.display = "none"
    }
    return null
}

function toggle(id, opt=null) {
    div = document.getElementById(id)
    if (opt == "show") {
        div.style.display = "flex"
    } else if (opt == "hide") {
        div.style.display = "none"
    } else {
        if (div.style.display != "flex") {
            div.style.display = "flex"
        } else {
            div.style.display = "none"
        }
    }
    return null
}

var formLogin = document.getElementById("login-form");
if (formLogin){
    formLogin.addEventListener(
        "submit", login, false
    )
}

function login( evt ) {
    evt.preventDefault()
    var fd = new FormData();
    var div = document.getElementById("msgArea");
    var u = document.getElementById("login-form-user");
    var p = document.getElementById("login-form-password");

    fd.append("user", u.value);
    fd.append("password", p.value);

    if (u.value.length > 3 && p.value.length > 3){
        axios.post("/auth/login", fd)
        .then(function(r){
            div.style.color = "rgb(100,200,60)"
            div.innerText = "Loggado com sucesso! Você será redirecionado em instantes"
            window.location.href = r.data.location
        })
        .catch(function(err){ 
            if (err.response.status == "401") {
                div.style.color = "rgb(255,100,100)"
                div.innerText = "Usuario ou senha invalidos"
            } else if (err.response.status == "400") {
                div.style.color = "rgb(100,100,100)"
                div.innerText = "Por favor, tente novamente!"
            }
        })
    }
}