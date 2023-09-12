// EXIBI VALOR DA COMPRA
const valorDigitado = localStorage.getItem('valorDigitado');
if (valorDigitado !== null) {
  const displayDiv = document.getElementById('valor-Compra');
  displayDiv.textContent = `${valorDigitado}`;
}

// JavaScript para exibir a data e hora atuais
function atualizarDataHora() {
    const divDataHora = document.getElementById("dataHora");
    const dataHoraAtual = new Date();
    divDataHora.textContent = dataHoraAtual.toLocaleString('pt-BR');
}

// Chamar a função quando o conteúdo da página estiver carregado
window.onload = function() {
    atualizarDataHora();
};


// Credito ou Débito
// Obtém a opção e a quantidade de parcelas selecionadas do Local Storage
const opcao = localStorage.getItem('opcaoSelecionada');
const parcelas = localStorage.getItem('parcelasSelecionadas');
const valorParcela = localStorage.getItem('valorParcelamento');

// Exibe a opção selecionada na página
const divOpcaoSelecionada = document.getElementById('opcaoSelecionada');
if (opcao === 'credito') {
    if (parcelas === '1') {
        divOpcaoSelecionada.textContent = `Crédito - R$${valorParcela} à vista`;
    } else {
        divOpcaoSelecionada.textContent = `Crédito - R$${valorParcela.toFixed(2).replace(".", ",")} parcelado em ${parcelas}x`;
    }
} else if (opcao === 'debito') {
      divOpcaoSelecionada.textContent = 'Débito';
} else {
      divOpcaoSelecionada.textContent = 'Nenhuma opção foi selecionada.';
}

