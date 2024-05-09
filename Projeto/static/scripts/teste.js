function pesq(){

   var clie = document.querySelector('#nome')
   console.log(clie.value)

    var cliente = fetch('/static/clientesp.json').then((response)=>{response.json().then((clientes) =>{console.log(clientes)})})
    fetch('/static/niver.json').then((response)=>{response.json().then((niver) =>{console.log(niver)})})

    console.log(cliente)
}
