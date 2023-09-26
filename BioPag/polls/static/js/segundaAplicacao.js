$(document).ready(function() {
    $("#limpaBancoButton").click(function() {
        console.log("Botão foi clicado!");
        $.ajax({
            type: "GET",
            url: "/limpa_banco/",  // Use a URL diretamente
            success: function(response) {
                if (response.conexao) {
                    if (response.valid) {
                        alert("Banco de dados esvaziado com sucesso!");
                        window.location.href = "/";
                    } else {
                        alert("Erro ao esvaziar o banco de dados.");
                    }
                } else {
                    alert("Erro na conexão com o Arduino.");
                }
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error("Erro:", errorThrown);
            }
        });
    });
});
