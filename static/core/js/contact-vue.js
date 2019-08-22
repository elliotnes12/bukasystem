new Vue({
    el: "#contact",
    data:{
    subject:"",
    name:"",
    mensaje:"",
    email:"",
    log:""
},
methods: {

  contact: function(event){

       event.preventDefault();
       alert("entro "+this.name);
  }
}

});
