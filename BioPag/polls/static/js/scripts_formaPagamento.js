//Exibir o valor da compra
const valorDigitado = localStorage.getItem('valorDigitado');
if (valorDigitado !== null) {
  const displayDiv = document.getElementById('display');
  displayDiv.textContent = `${valorDigitado}`;
}

// Função para calcular e exibir o valor da parcela
function calculateParcela(parcelas) {
  const valorDigitado = localStorage.getItem('valorDigitado');

  console.log("Valor digitado:", valorDigitado); // Verifique o valor aqui

  if (valorDigitado !== null) {
    // Remove "R$" e substitui ',' por '.' para garantir que o valor seja tratado corretamente como número
    const valorNumerico = parseFloat(valorDigitado.replace("R$", "").replace(",", "."));

    console.log("Valor numérico:", valorNumerico); // Verifique o valor convertido aqui

    if (!isNaN(valorNumerico)) {
      let displayText = '';
      if (parcelas === 1) {
        // Exibir o valor total da compra à vista
        const valorTotal = `R$ ${valorNumerico.toFixed(2).replace(".", ",")}`;
        displayText = `<span class="valor-option">${valorTotal}</span> <span class="parcela-option">à vista</span>`;
        console.log("Parcelas: " + parcelas)
        // Armazenar a opção e o valor total no Local Storage
        localStorage.setItem('opcaoParcelamento', 1);
        localStorage.setItem('valorParcelamento', valorTotal);
      } else if (parcelas > 1) {
        // Exibir o valor da parcela escolhida
        const valorParcela = valorNumerico / parcelas;
        const valorDisplay = `R$ ${valorParcela.toFixed(2).replace(".", ",")}`;
        const parcelaDisplay = `${parcelas}x`;
        displayText = `<span class="valor-option">${valorDisplay}</span> <span class="parcela-option">${parcelaDisplay}</span>`;
        console.log("Valor parcela: " + valorParcela.toFixed(2))
        console.log("Parcelas: " + parcelas)
        // Armazenar a opção e o valor da parcela no Local Storage
        localStorage.setItem('opcaoParcelamento', parcelaDisplay);
        localStorage.setItem('valorParcelamento', valorParcela.toFixed(2));
      } else {
        displayText = "Número de parcelas inválido";
      }

      const display = document.getElementById('display');
      display.innerHTML = displayText;
    } else {
      console.log("Erro: valor digitado não é um número válido.");
    }
  }
}


// Armazene a opção e a quantidade de parcelas no Local Storage
localStorage.setItem('opcaoSelecionada', 'credito');
localStorage.setItem('parcelaSelecionada', parcelas);
