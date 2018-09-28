$(document).ready(
    function(){
        // DEFINIR MARGIN-BOTTOM NO SECTION PARA NAO OCORRER CORTES COM O RODAPE
        if ($(window).width() >= 768) {
            $(".section").css({"margin-bottom": "100px"});
        }     
        // BOTOES RELACIONADOS AS CAIXAS DE ENTRADA DE FUNCAO E DADOS DA FUNCAO PARA TELAS MENORES QUE 768PX DE LARGURA               
        $(".toggler-function").click(
                function(){
                $(".toggler-button-function").animate({
                    height: 'toggle'
                });
        });

        //
        $(".toggler-function_data").click(
            function(){
                $("#toggler-button-function_data").animate({
                    height: 'toggle'
                });
        });
        // REAPARECE CAIXAS DE ENTRADA DE FUNCAO E DADOS DA FUNCAO PARA TELAS MAIORES QUE 768PX QUANDO CASO ELAS ESTEJAM FECHADAS
        $(window).resize(
            function() {
                if ($(window).width() >= 768) {
                    $(".toggler-button-function").animate({
                        height: 'show'
                    });
                    $("#toggler-button-function_data").animate({
                        height: 'show'
                    });        
                }
            });
    });
