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

    fetch('/consultap', {
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

function carrega_dadospedido(){
    var cliente = document.querySelector('#nome').value
    var clie = document.getElementById('nome')
    document.getElementById('entrega').value=""
    document.getElementById('observa').value = ""
    document.getElementById('dentrega').value = ""
    document.getElementById('descricao').value =  ""
    document.getElementById('entrega').value =  ""
    document.getElementById('quant').value =  ""
    
  
    fetch('/consultap', {
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
        document.getElementById('cpf').value = item.cpf
        //document.getElementById('nascimento').value = item.nascimento
        document.getElementById('celular').value = item.celular
        document.getElementById('email').value = item.email
        //document.getElementById('instagram').value = item.instagram,
        document.getElementById('cep').value = item.cep
        document.getElementById('endereco').value = item.endereco
        document.getElementById('num').value = item.numero
        document.getElementById('bairro').value = item.bairro
        document.getElementById('cidade').value = item.cidade
        document.getElementById('anota').value = item.observacao
        console.log(item.observa)
        //document.getElementById('anota').value = item.observacao
    })
}

function carrega_dadosp(){
    var cliente = document.querySelector('#nome').value
    var clie = document.getElementById('nome')
    document.getElementById('entrega').value=""
    document.getElementById('observa').value = ""
    document.getElementById('dentrega').value = ""
    document.getElementById('descricao').value =  ""
    document.getElementById('entrega').value =  ""
    document.getElementById('quant').value =  ""
    document.getElementById('status').value = ""
    var select = document.getElementById("spedido");
        while (select.firstChild) {
            select.removeChild(select.firstChild);
        }
    fetch('/consultap', {
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
        document.getElementById('cpf').value = item.cpf
        //document.getElementById('nascimento').value = item.nascimento
        document.getElementById('celular').value = item.celular
        document.getElementById('email').value = item.email
        //document.getElementById('instagram').value = item.instagram,
        document.getElementById('cep').value = item.cep
        document.getElementById('endereco').value = item.endereco
        document.getElementById('num').value = item.numero
        document.getElementById('bairro').value = item.bairro
        document.getElementById('cidade').value = item.cidade
        document.getElementById('anota').value = item.observacao
        console.log(item.observa)
        //document.getElementById('anota').value = item.observacao
    })
}

function carrega_pedidos(){
    var cod = document.querySelector('#id').value
    var sta = document.querySelector('#status').value
    document.getElementById('dentrega').value = ""
    document.getElementById('descricao').value =  ""
    document.getElementById('entrega').value =  ""
    document.getElementById('quant').value =  ""
    document.getElementById('observa').value =  ""
    if (sta == 1){
        sta= "Pedido em Aberto"
    } else{
        sta = "Pedido Entregue"
    }
  
    fetch('/consultap1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cod: cod, sta: sta})
    })
    .then(response => response.json())
    .then(data => {
        const item = data[0]
        
        var select = document.getElementById("spedido");
        while (select.firstChild) {
            select.removeChild(select.firstChild);
        }
        var opcaoVazia = document.createElement("option");
            opcaoVazia.value = ""; // Define o valor como vazio
            opcaoVazia.text = ""; // Define o texto como vazio
        select.appendChild(opcaoVazia)
        
        data.forEach(function(dicionario) {
            // Cria um elemento de opção
            
            var option = document.createElement("option");
            // Define o valor e o texto da opção
            option.value = dicionario.id;
            option.text = dicionario.cadastro;
            // Adiciona a opção ao select
            select.appendChild(option);

            
        })});
}
function carrega_pedido(){
    var pedido = document.querySelector('#spedido').value

    fetch('/consultap2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ pedido: pedido })
    })
    .then(response => response.json())
    .then(data => {
        const item = data[0]
        console.log(data)
         document.getElementById('dentrega').value = item.dentrega
        document.getElementById('descricao').value = item.descricao
        document.getElementById('entrega').value = item.entrega
        document.getElementById('quant').value = item.quantidade
        document.getElementById('observa').value = item.observa
        // //document.getElementById('instagram').value = item.instagram,
        // document.getElementById('cep').value = item.cep
        // document.getElementById('endereco').value = item.endereco
        // document.getElementById('num').value = item.numero
        // document.getElementById('bairro').value = item.bairro
        // document.getElementById('cidade').value = item.cidade

    
})
}
function limpar(){
    document.getElementById('id').value = ""
    document.getElementById('cpf').value =""
    document.getElementById('nascimento').value = ""
    document.getElementById('celular').value = ""
    document.getElementById('email').value = ""
    document.getElementById('instagram').value = ""
    document.getElementById('cep').value = ""
    document.getElementById('endereco').value = ""
    document.getElementById('num').value = ""
    document.getElementById('bairro').value = ""
    document.getElementById('cidade').value =""
    document.getElementById('dcadastro').value =""
    document.getElementById('observa').value = ""
    document.getElementById('dentrega').value = ""
    document.getElementById('descricao').value =  ""
    document.getElementById('entrega').value =  ""
    document.getElementById('quant').value =  ""
    
}
