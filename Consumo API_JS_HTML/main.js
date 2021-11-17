function Getter(url){
    let request = new XMLHttpRequest();
    request.open("GET",url,false);
    request.send();
    return request.responseText;
}

function criarLinha(estado){
    linha = document.createElement("tr")
    tdEstado = document.createElement("td")
    tdCasos = document.createElement("td")
    tdMortes = document.createElement("td")
    
    tdEstado.innerHTML = estado.state;
    tdCasos.innerHTML = estado.cases;
    tdMortes.innerHTML = estado.deaths;

    linha.appendChild(tdEstado)
    linha.appendChild(tdCasos)
    linha.appendChild(tdMortes)

    return linha;
}

function main(){
    data = Getter("https://covid19-brazil-api.now.sh/api/report/v1");
    jsondata = JSON.parse(data);
    estados = jsondata['data']
    let tabela = document.getElementById("tabela")
    
    estados.forEach(element => {
        let linha = criarLinha(element);
        tabela.appendChild(linha)
    });
}

main()
console.log("Hello World!")