function listBrands(save=true) {

    var div  = document.getElementById("listBrands");
    var divCar  = document.getElementById("carOpt");
    var divListCars  = document.getElementById("listCars");

    div.innerHTML = peraAe;
    divCar.innerHTML = "";
    divListCars.innerHTML = "";

    axios.get("/api/brands")
    .then(function(r){
        var brands = r.data;
        div.innerHTML = "";
        for(var i = 0; i < brands.length; i++) {
            div.innerHTML += `
            <article class="items" id="brand-${brands[i].id}" onclick="listCars('${brands[i].name}','true')">
                <h3>${brands[i].name}</h3>
            </article>`
        }
    })
    .catch(function(err){ console.log(err) })
    
    if (save) {
        window.history.pushState({ func: "listBrands" }, null, "/" );
    }
    return null;
}