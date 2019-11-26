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
//Carga el contendio del formulario crer empleado desde el movil a una modal
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


//CArgar modal de nueva categoria con su formulario
function cargarModal() {
    let select = document.getElementById("categorias");
    if (select.value === 'nueva') {
        $('#modalCategoria').modal({
            show: true,
        });
    }
}

//Metodo que me carga el formulario de nueva mesa
function formNuevaMesa(ruta, ruta1, idMesa) {
    let select = document.getElementById("mesas");
    if (select.value === 'nueva') {
        $('#modalVentas').modal({
            show: true,
        });
        $.ajax({
            url: ruta,
            success: function(respuesta) {
                document.getElementById("resultadoVentas").innerHTML = respuesta

            },
            error: function() {
                console.log("error");
            }
        })
    } else {
        $.ajax({
            url: ruta1,
            data: "idMesa=" + idMesa,
            method: 'GET',
            success: function(respuesta) {
                document.getElementById("comanda").innerHTML = respuesta
                document.getElementById("comanda-pc").innerHTML = respuesta


            },
            error: function() {
                console.log("error");
            }
        })

    }
}

function llenar(ruta, categoria) {
    $.ajax({
        url: ruta,
        data: "categoria=" + categoria,
        method: "get",
        success: function(respuesta) {
            document.getElementById("productoselect").innerHTML = respuesta;
        },
        error: function() {
            console.log("no se pueden encontrar los datos");
        }
    });
}

function pagar(ruta) {
    $.ajax({
        url: ruta,
        success: function() {
            alert("Pagó")
        },
        error: function() {
            console.log("erro");
        }
    })
}
// reportes
function today(ruta){
    $.ajax({
        url: ruta,
        dataType: "json",
        success: function(respuesta) {
            
            var nombres = '';
            var datos = '';

            for(var i=0;i<respuesta.producto.length;i++)
            {
                
                nombres += respuesta.producto[i].producto__nombreProducto  + ',';
                datos += respuesta.producto[i].cantidad  + ', ';
                
                
            }

        
            nombres=nombres.substr(0,(nombres.length-1))
            datos=datos.substr(0,(datos.length-2))

           
            var labelsmy = []
            labelsmy = nombres.split(",");
            console.log(labelsmy)
            

            datamy = datos.split(",");
            console.log(datamy)




            // espacio del chart
            new Chart(document.getElementsByClassName("grafica"), {
                type: 'bar',
                data: {
                  labels: labelsmy,
                  datasets: [
                    {
                      label: "venta (unidades)",
                      backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9"],
                      data: datamy
                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                    text: 'cantidades vendidas hoy'
                  }
                }
            });



            // espacio del chart


            

            
        },
        error: function() {
            alert('error');
        }
    });
}        


//ver detalle
function verDetalle(ruta) {
    $.ajax({
        url: ruta,
        dataType: "json",
        success: function(respuesta) {
            var salida = "";
            for (const i in respuesta.producto) {
                salida += "<tr>";

                salida += "<td>" + respuesta.producto[i].producto__nombreProducto + "</td>";
                salida += "<td>" + respuesta.producto[i].precio + "</td>";
                salida += "<td>" + respuesta.producto[i].cantidad + "</td>";
                salida += "</tr>";

            }




            document.getElementById("detalle").innerHTML = salida;

        },
        error: function() {
            alert('error');
        }

    });
}