var xmlhttp = new XMLHttpRequest();
var loginform = document.getElementById("loginform");
loginform.addEventListener("submit", function(e){
  xmlhttp.open("POST","/authN/",true);
  xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xmlhttp.send("username=" + document.getElementById("username").value + "&password="+document.getElementById("password").value + "&csrfmiddlewaretoken="+ $('input').val() );
  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.status == 403){
      document.getElementById("login_response").innerHTML = "Sorry, but the login information you have entered is invalid";
        document.getElementsByClassName("main-container")[0].style.backgroundColor = "#8E2800";
    }
    else
    {
        document.getElementById("login_response").innerHTML = "Welcome Back, " + $('#username').val();
        document.getElementsByClassName("main-container")[0].style.backgroundColor = "#468966";
        setTimeout(function()
        {
          window.location.replace("/home/");
        },1500);
    }


     //console.log(xmlhttp.response);
    //console.log(xmlhttp);
    /*if (xmlhttp.readyState === 4 ){
      if (xmlhttp.status == 403)
      {
        document.getElementById("login_response").innerHTML = "Sorry, but the login information you have entered is invalid";
        document.getElementsByClassName("main-container")[0].style.backgroundColor = "#8E2800";
      }
      //else if we get a good response
      else{     
        document.getElementById("login_response").innerHTML = "Welcome Back, " + response.ucid;
        document.getElementsByClassName("main-container")[0].style.backgroundColor = "#468966";
        setTimeout(function()
        {
          location.reload();
        },1500);
      }
    
    }*/
  };
}, false);