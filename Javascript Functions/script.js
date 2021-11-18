function onSubmit(){
    let peso = document.getElementById("weight").value
    let altura = document.getElementById("height").value

    let imc = peso / (altura**2);

    alert(imc)
}