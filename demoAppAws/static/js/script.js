document.addEventListener("DOMContentLoaded", function () {
  var select = document.getElementById("opciones");
  var body = document.getElementById("body");
  var cardInfo2 = document.querySelector(".card-info2");

  function cambiarColorFondo(opcionSeleccionada) {
    switch (opcionSeleccionada) {
      case "Ngeek":
        body.style.backgroundColor = "#022243";
        cardInfo2.style.backgroundColor = "#022243";

        break;
      case "AWS":
        body.style.backgroundColor = "#e47911";
        cardInfo2.style.backgroundColor = "#e47911";

        break;
      case "Azure":
        body.style.backgroundColor = "#333333";
        cardInfo2.style.backgroundColor = "#333333";

        break;
      case "GCP":
        body.style.backgroundColor = "#0F9D58";
        cardInfo2.style.backgroundColor = "#0F9D58";

        break;
      default:
        body.style.backgroundColor = "black";
        cardInfo2.style.backgroundColor = "black";
    }
  }

  select.addEventListener("change", function () {
    var opcionSeleccionada = select.value;
    cambiarColorFondo(opcionSeleccionada);
  });

  cambiarColorFondo(select.value);

  var mensajeElemento = document.querySelector(".subcar-info3 p");

  function actualizarMensaje(opcionSeleccionada) {
    var mensaje;
    switch (opcionSeleccionada) {
      case "Ngeek":
        mensaje = "Bienvenido a Ngeek";
        break;
      case "AWS":
        mensaje = "Explorando AWS";
        break;
      case "Azure":
        mensaje = "Descubriendo Azure";
        break;
      case "GCP":
        mensaje = "Navegando por GCP";
        break;
      default:
        mensaje = "Selecciona una opción";
    }
    mensajeElemento.textContent = mensaje;
  }

  select.addEventListener("change", function () {
    var opcionSeleccionada = select.value;
    actualizarMensaje(opcionSeleccionada);
  });
  actualizarMensaje(select.value);
});
