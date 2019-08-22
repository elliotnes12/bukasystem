new Vue({
    el: "#contact",
    data:{
    subject:"",
    name:"",
    mensaje:"",
    email:"",
    csrf:"",
    log:"",
    errbgColorm:"#f8d7da",
    errcolorm:"#721c24",
    errborm:"#f5c6cb",
    displaym:"none",
    reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
},
methods: {

  msj:function(msj,type){

      if(type == 1){
        this.errbgColorm = "#f8d7da";
        this.errcolorm = "#721c24";
        this.errborm = "#f5c6cb";
      }
      else{
        this.errbgColorm = "#d4edda";
        this.errcolorm = "#155724";
        this.errborm = "#c3e6cb";
      }
      this.log = msj;
      this.displaym = "flex";
  },
  cancel:function(event){
      this.displaym = "none";
  },
  isEmailValid: function() {
    return (this.email == "")? "has-error" : (this.reg.test(this.email)) ? 'has-success' : 'has-error';
  },
  contact: function(event){

    var object = this;

    var token = document.getElementById("token");
  
       if(this.name == ""){
          this.msj("Ingrese un nombre",1);
          return false;
       }
       if(this.isEmailValid() == "has-error"){
        this.msj("Ingrese un email valido",1);
         return false;
       }
       if(this.subject == ""){
        this.msj("Ingrese un tipo de asunto",1);
         return false;
       }
       if(this.mensaje == ""){
        this.msj( "Ingrese algún mensaje",1);
          return false;
       }

       var data = {
        "name": object.name,
        "email": object.email,
        "asunto": object.subject,
        "mensaje": object.mensaje,
        "detail":token.value
      } 


       this.$http.post('/api/create_user',data).then(function(response){


            if(response.status == 201){
              object.msj("Gracias, pronto nos contactaremos con usted",2);
              object.name = "";
              object.email = "";
              object.subject = "";
              object.mensaje = "";
            }

          }, function(){

       });

       event.preventDefault();
       
  }
}

});