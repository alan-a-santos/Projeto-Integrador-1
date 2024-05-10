function consultacep(){

        
   if (document.getElementById(cep) != ""){
        console.log("fffffff")
        const cep = document.getElementById('cep')
        cep.addEventListener('blur', e=> {
        const value = cep.value.replace(/[^0-9]+/, '');
        const url = `https://viacep.com.br/ws/${value}/json/`;

        fetch(url)
        .then( response => response.json())
        .then( json => {
          
            if( json.logradouro ) {
                console.log(json)
            document.querySelector('input[name=endereco]').value = json.logradouro;
                document.querySelector('input[name=bairro]').value = json.bairro;
                document.querySelector('input[name=cidade]').value = json.localidade;
                //document.querySelector('input[name=estado]').value = json.uf;
            }      
            
          });
      });
}    
}

function carrega_dados(){
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
}