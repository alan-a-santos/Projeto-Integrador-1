function pesq(){

    var cliente = document.querySelector('#nome').value

    fetch('/consulta', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cliente: cliente })
    })
    .then(response => response.json())
    .then(data => {
        const item = data[0]
        console.log(data)
        document.getElementById('id').value = item.id
        document.getElementById('cpf').value = item.cpf,
        document.getElementById('nascimento').value = item.nascimento
        document.getElementById('celular').value = item.celular,
        document.getElementById('email').value = item.email,
        document.getElementById('instagram').value = item.instagram,
        document.getElementById('cep').value = item.cep
        document.getElementById('endereco').value = item.endereco
        document.getElementById('num').value = item.numero
        document.getElementById('bairro').value = item.bairro
        document.getElementById('cidade').value = item.cidade
        document.getElementById('dcadastro').value = item.cadastro
        document.getElementById('observa').value = item.observacao
   
        
    })

    //fetch('/consulta').then((retorno)=> console.log(retorno))
    // const response = await fetch('/consulta')
    // console.log(response)
    // const data = await response.json()
    // console.log(data)
   //var clie = document.querySelector('#nome').value
  
//    var cliente = new XMLHttpRequest()

// cliente.open('POST', '/consulta', true)
// cliente.setRequestHeader('Content-Type', 'application/json')
// cliente.onreadystatechange=function() {
//    if (cliente.readyState === XMLHttpRequest.DONE && cliente.status === 200){
       
//         console.log("retornado com sucesso")
//             var item = JSON.parse(cliente.responseText)
//         document.getElementById('id').value = item.id 
//         document.getElementById('cpf').value = item.cpf
//      }

// cliente.send(JSON.stringify({clie:clie}))
// }
//     var cliente = fetch('/static/clientesp.json').then((response)=>{response.json().then((clientes)=>{console.log(clientes)})})
//     fetch('/static/niver.json').then((response)=>{response.json().then((niver) =>{console.log(niver)})})

//     console.log(cliente)
}
