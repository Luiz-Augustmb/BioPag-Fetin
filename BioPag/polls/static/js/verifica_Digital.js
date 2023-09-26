$(document).ready(function () {
    $.get("/verify_fingerprint/", function (data) {
        console.log("Dados recebidos:", data);  // Adicione esta linha para depuração

        if (data.conexao) {
            console.log("Conexão bem-sucedida.");  // Adicione esta linha para depuração

            if (data.valid) {
                window.location.href = "/pag_Aprovado/";
            } else {
                window.location.href = "/pag_Negado/";
            }
        } else {
            console.log("Erro de Hardware.");  // Adicione esta linha para depuração
            alert("Erro de Hardware, por favor tente novamente!");
            window.location.href = "/verifica_Digital/";
        }
    }).fail(function () {
        console.log("Erro na requisição AJAX.");  // Adicione esta linha para depuração
        alert("Erro na leitura biométrica. Por favor, tente novamente.");
        window.location.href = "/verifica_Digital/";
    });
});
