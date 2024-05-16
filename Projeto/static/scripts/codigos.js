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
                document.getElementById('num').focus()
            }           
          });
      });
}    
}

function dados_cliente(){
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
        document.getElementById('dcadastro').value = formato(item.cadastro)
        document.getElementById('observa').value = item.observacao
   
        
    })
}

function carrega_dadospedido(){
    var cliente = document.querySelector('#nome').value
    var clie = document.getElementById('nome')
    document.getElementById('observa').value = ""
    document.getElementById('dentrega').value = ""
    document.getElementById('descricao').value =  ""
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
        document.getElementById('celular').value = item.celular
        document.getElementById('email').value = item.email
        document.getElementById('cep').value = item.cep
        document.getElementById('endereco').value = item.endereco
        document.getElementById('num').value = item.numero
        document.getElementById('bairro').value = item.bairro
        document.getElementById('cidade').value = item.cidade
        document.getElementById('anota').value = item.observacao        
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
        document.getElementById('celular').value = item.celular
        document.getElementById('email').value = item.email
        document.getElementById('cep').value = item.cep
        document.getElementById('endereco').value = item.endereco
        document.getElementById('num').value = item.numero
        document.getElementById('bairro').value = item.bairro
        document.getElementById('cidade').value = item.cidade
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
            opcaoVazia.value = ""
            opcaoVazia.text = ""
        select.appendChild(opcaoVazia)
        
        data.forEach(function(dicionario) {           
            var option = document.createElement("option");
            option.value = dicionario.id;
            option.text = formato(dicionario.cadastro);
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
        x = formato(item.dentrega)
        document.getElementById('dentrega').value = x
        document.getElementById('descricao').value = item.descricao
        document.getElementById('entrega').value = item.entrega
        document.getElementById('quant').value = item.quantidade
        document.getElementById('observa').value = item.observa    
         
})
}
function formato(data) {
    var dia  = data.split("-")[2];
    var mes  = data.split("-")[1];
    var ano  = data.split("-")[0];
  
    return ("0"+dia).slice(-2) + '/' + ("0"+mes).slice(-2) + '/' +ano ;
}

function cpf(){

   
   console.log('valor')

}