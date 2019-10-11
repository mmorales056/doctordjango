/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

// este metodo me carga el contenido de el formulario editar empleado a la ventana modal
function editarEmpleado(ruta) {
    $.ajax({
        url: ruta,
        success: function(respuesta) {
            document.getElementById('modaleditar').innerHTML = respuesta;
        },
        error: function() {
            console.log("No se a podido tener la informacion");
        }
    })


}

function crearEmpleadoMovil(ruta) {
    $.ajax({
        url: ruta,
        success: function(respuesta) {
            document.getElementById('modaleditar').innerHTML = respuesta;
        },
        error: function() {
            console.log("No se pudieron obtener los datos");
        }
    })
}


/* MODULO PRODUCTOS*/
function crearProductoMovil(ruta) {
    $.ajax({
        url: ruta,
        success: function(respuesta) {
            document.getElementById('editarProducto').innerHTML = respuesta;
        },
        error: function() {
            console.log('Error al traer los datos');
        }
    });
}

function editarProducto(ruta) {
    $.ajax({
        url: ruta,
        success: function(respuesta) {
            document.getElementById('editarProducto').innerHTML = respuesta;
        },
        error: function() {
            console.log("No se a podido tener informacion");
        }

    });
}

function verProducto(ruta) {
    $.ajax({
        url: ruta,
        dataType: "json",
        success: function(respuesta) {
            var salida = "";
            salida = "<table class='table table-dark'>";
            $.each(respuesta, function(indice, valor) {
                salida += " <tr> <td> " + indice + "</td><td>" + valor + "</td></tr>"
            });
            salida += "</table>";
            document.getElementById("editarProducto").innerHTML = salida;
        },
        error: function() {
            console.log("no se pueden encontrar los datos");
        }
    });
}

//Este metodo me da formato de punto de mil a los campos que lo requieren
function notNegative(num) {
    num = document.getElementById('precioVenta').value;
    console.log(num);
    if (num >= 0) {
        document.getElementById('precioVenta').innerHTML = num;
        console.log("entro aca");
    } else {
        document.getElementById('precioVenta').innerHTML = -(num);
        console.log("entro aca else");
    }
}

//CArgar modal de nueva categoria con su formulario
function cargarModal() {
    let select = document.getElementById("categorias");
    if (select.value === 'nueva') {
        $('#modalCategoria').modal({
            show: true,
        });
    }
}