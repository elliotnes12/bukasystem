
class ModalAlert{
    clmodal:string = "";
    modal(menssage:string = "") {
       var uiparent = document.querySelector("body");
       console.log(uiparent);
    }
}


(function(window,alert){

    window.modal = window.$modal = new ModalAlert();
    modal.modal();

})(window,alert)