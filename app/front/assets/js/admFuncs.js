function delCar( id ){
    var v = window.confirm("Deseja realmente excluir esse item?")
    if (v) {

        axios.delete(`/api/cars/${id}`)
        .then(function(){
            id = 'carID-' + id;
            var el = document.getElementById(id);
            el.parentNode.removeChild(el);
        })
        .catch(function(err){
            console.log(err);
        })
    return null
    }
}

function redirectForUpdateCar( id ) {
    window.location.href = '/dash/upcar/' + id + "/"
}

function logout() {
    window.location.href = '/auth/logout'
}

var formSetBrand = document.getElementById("setBrand-form")
formSetBrand.addEventListener("submit", setBrand, false)

function setBrand( evt ) {
    evt.preventDefault()

    var bName = document.getElementById("setBrand-name")
    
    
    if ( bName.value != "" ) {
        
        var fData = new FormData()

        fData.append("name",bName.value)
        
        axios.post("/api/brands", fData)
        .then(function(r){
            window.alert(`Montadora '${r.data.name}' adicionada com sucesso!`)
            listBrands()
        }).catch(function(err){
            console.log(err)
        })
    } else {
        window.alert("Campo 'Nome' não pode ficar vazio!")
    }
    return null
}

function getListOfBrands() {

    var sel = document.getElementById("setCar-Selectbrand");
    
    sel.innerHTML = '<option value="">Selecione uma Montadora</option>'
    axios.get("/api/brands")
    .then(function(r){
        allBrands = r.data
        for(var inter in allBrands){
            n = allBrands[inter].name
            sel.innerHTML += `<option value="${ n }">${ n }</option>`
        }
    })
    .catch(function(err){ console.log(err) });
    return null;
}


var formSetCar = document.getElementById("setCar-form")
formSetCar.addEventListener("submit", setCar, false)

function setCar( evt ) {
    evt.preventDefault();
    
    var name = document.getElementById("setCar-name")
    var year = document.getElementById("setCar-year")
    var brand = document.getElementById("setCar-Selectbrand")
    var engine = document.getElementById("setCar-engine")
    var gasCharge = document.getElementById("setCar-gasCharge")
    
    if ( name.value != "" & year.value != "" 
        & engine.value != "" & brand.value != "" & gasCharge.value != "" ) {
        var form = new FormData();
        form.append("name", name.value)
        form.append("year", year.value)
        form.append("brand", brand.value)
        form.append("engine", engine.value)
        form.append("gas_charge", gasCharge.value)

        axios.post("/api/cars", form)
        .then(function( r ) {
            car = r.data
            getCarByName(car.brand, car.name)
            window.alert(`'${car.name}' foi adicionado com sucesso!`)
        }).catch(function(err) {
            if (err.response ) {
                if (err.response.data.car) {
                    window.alert("Não adicionado")
                }
            }
        })
    } else {
        alert("Todos os campos são obrigatorios!")
    }
    return null
}

