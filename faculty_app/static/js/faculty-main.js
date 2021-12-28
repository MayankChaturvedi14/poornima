document.addEventListener("DOMContentLoaded", function(event) {

    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)
    
    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd){
    toggle.addEventListener('click', ()=>{
    // show navbar
    nav.classList.toggle('show')
    // change icon
    toggle.classList.toggle('bx-x')
    // add padding to body
    bodypd.classList.toggle('body-pd')
    // add padding to header
    headerpd.classList.toggle('body-pd')
    })
    }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
    if(linkColor){
    linkColor.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
    }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    
    // Your code to run since DOM is loaded and ready
    });


    function showTooltip(e) {
        var tooltip = e.target.classList.contains("tooltip")
            ? e.target
            : e.target.querySelector(":scope .tooltip");
        tooltip.style.left =
            (e.pageX + tooltip.clientWidth + 10 < document.body.clientWidth)
                ? (e.pageX + 10 + "px")
                : (document.body.clientWidth + 5 - tooltip.clientWidth + "px");
        tooltip.style.top =
            (e.pageY + tooltip.clientHeight + 10 < document.body.clientHeight)
                ? (e.pageY + 10 + "px")
                : (document.body.clientHeight + 5 - tooltip.clientHeight + "px");
      }
      
      var tooltips = document.querySelectorAll('.couponcode');
      for(var i = 0; i < tooltips.length; i++) {
        tooltips[i].addEventListener('mousemove', showTooltip);
      }


      function Initial_View( id ) {
        // hide previously shown image
        for ( i = 1; i < 10; i++) {
            var obj = document.getElementById( "dept" + i );
            if(obj.style.display == 'none'){
            obj.style.display = "block";
        }}  
    } 


      function ImgView( id ) {
        // hide previously shown image
        for ( i = 1; i < 10; i++) {
            var obj = document.getElementById( "dept" + i );
            if (obj != null)
                obj.style.display = 'none';
        }
        var obj = document.getElementById( "dept" + id );      
        if (obj != null)
            obj.style.display = "block";
}