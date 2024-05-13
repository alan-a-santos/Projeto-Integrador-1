
function carrega_dadosp(){
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
        //document.getElementById('nascimento').value = item.nascimento
        document.getElementById('celular').value = item.celular,
        document.getElementById('email').value = item.email,
        //document.getElementById('instagram').value = item.instagram,
        document.getElementById('cep').value = item.cep
        document.getElementById('endereco').value = item.endereco
        document.getElementById('num').value = item.numero
        document.getElementById('bairro').value = item.bairro
        document.getElementById('cidade').value = item.cidade
        document.getElementById('dcadastro').value = item.cadastro
        document.getElementById('observa').value = item.observacao
   
        
    })
}