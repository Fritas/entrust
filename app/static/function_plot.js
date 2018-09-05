var width_graph = det_width();
var height_graph = det_height();

function det_width (){
    // tamanho da tela * porcentagem que as colunas ocupam / 100
    var window_width = $(window).width();
    if (window_width >= 1200) {
        var colms = 8; //col-xl-8
    } else if (window_width >= 992) {
        var colms = 8; //col-lg-8
    }
    else if (window_width >= 768) {
        var colms = 8; //col-md-8
    }
    else if (window_width >= 576) {
        var colms = 12; //col-sm-12 
    }
    else if (window_width < 576) {
        var colms = 12; //col-12
    }
    colms = colms - 1
    return (window_width * (colms * 100 / 12) / 100);
}

function det_height() {
    var window_width = $(window).width();
    if (window_width >= 1500) {
        var percentage = 84;
    } else if (window_width >= 1200) {
        var percentage = 80; //col-xl-8
    } else if (window_width >= 992) {
        var percentage = 75; //col-lg-8
    }
    else if (window_width >= 768) {
        var percentage = 70; //col-md-8
    }
    else if (window_width >= 576) {
        var percentage = 60; //col-sm-12 
    }
    else if (window_width < 576) {
        var percentage = 60; //col-12
    }
    return $(window).height() *  percentage  / 100;
}

function reloadGraph (){
    width_graph = det_width();
    height_graph = det_height();
    function_plotar();
}

// https://mauriciopoppe.github.io/function-plot/
function function_plotar(function_graph){
    functionPlot({
        width: width_graph,
        height: height_graph,
        target: '.graph',
        color: 'green',
        //The little circle that has the x-coordinate of the mouse position is called a "tip", the following options can be configured:
        tip: {
            xLine: true,    // dashed line parallel to y = 0
            yLine: true,    // dashed line parallel to x = 0
            renderer: function (x, y, index) {
            // the returning value will be shown in the tip
            }
        },
        data: [
                {
                    fn: function_graph, //'{{ dic.function_graph }}',
                    graphType: 'polyline', //permite uma maior complexidade de funções
                }
            ]
        })
}
