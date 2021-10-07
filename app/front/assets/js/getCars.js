function getCarByName( brand,carName ){
    var div = document.getElementById("carOpt");
    var dir = document.getElementById("header-dir");
    var divListCars = document.getElementById("listCars");

    
    if( divListCars.innerHTML == "" ) {
        listCars(brand, false)
    }

    div.innerHTML = peraAe;
    axios.get(`/api/cars/${ brand  }/${ carName }`)
    .then(function( r ){

        innerCars(r.data)
        var h = `<a class="header-dir-items" href="/" >Home</a>`;
        var b = `<a class="header-dir-items" href="/${brand}" > ${brand} </a>`;
        var c = `<span class="header-dir-items" >${ carName }</span>`;
        dir.innerHTML = `${h} > ${b} > ${c}`;
        window.history.pushState(
            {
                func: "getCarByName",
                data: { brand, carName }
            },
            "Mocinetica - " + carName,
            `/${brand}/${carName}/`
        )

    }).catch(function(err){ console.log(err) })
    return null
}


function innerCars(cars) {

    var div = document.getElementById("carOpt");

    
    div.innerHTML = "";
    cars.forEach(car => {
        div.innerHTML += `
        <article class="items" id="carID-${car.id}" onclick="showCar('${car.id}')">
            <b> ${ car.engine } - ${ car.year }</b>
        </article>`;
    });
    return null;
}


function listCars(brand, save){
    var div = document.getElementById("listCars");
    var divListBrands = document.getElementById("listBrands");
    var divCar = document.getElementById("carOpt");
    var dir = document.getElementById("header-dir");

    if (divListBrands.innerHTML == "") {
        listBrands(false)
    }
    
    div.innerHTML = peraAe;
    divCar.innerHTML = "";


    axios.get(`/api/cars/${brand}`)
    .then(function(r){
        var cars = r.data;
        div.innerHTML = "";
        for ( carName in cars) {
            div.innerHTML += `
            <article class="items" id="carID-${carName}" onclick="getCarByName('${ brand }','${ carName }')">
                <h2>${ carName }</h2>
            </article>`;
        }
        if (save) {
            var h = `<a class="header-dir-items" href="/" >Home</a>`;
            var b = `<span class="header-dir-items" > ${brand} </span>`
            dir.innerHTML = `${h} > ${b}`;
            window.history.pushState(
                {
                    func: "listCars",
                    data: {
                        brand: brand
                    }
                },
                null,
                `/${brand}/`
            );
        }
    })
    .catch(function(err){console.log(err)})

    return null;
}

function showCar(id) {
    var div = document.getElementById("car");
    if (div.getAttribute('carID') == id ) {
        div.style.display = "flex";
    } else {
        div.setAttribute('carID', id);
        axios.get(`/api/cars/${ id }`)
        .then(function(r){
            car = r.data
            div.innerHTML = `
            <div class="showCar">
                <p class="btn-close" onclick="document.getElementById('car').style.display='none'" title="fechar">X</p>
                <div>
                    <h2>${ car.name }</h2>
                    <span>Ano: ${ car.year }</span><br>
                    <span>Motor: ${ car.engine }</span><br>
                    <span>Montadora: ${ car.brand }</span><br>
                    <span>Carga de Gás: ${ car.gas_charge } g</span><br>
                <div>
            </div>`
            div.style.display = "flex";
        })
        .catch(function(err){ console.log(err) })
    }
    return null
}

