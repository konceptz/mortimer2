var xmlhttp = new XMLHttpRequest();
var loginform = document.getElementById("loginform");
loginform.addEventListener("submit", function(e){
  xmlhttp.open("POST","/authN/",true);
  xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xmlhttp.send("username=" + document.getElementById("username").value + "&password="+document.getElementById("password").value + "&csrfmiddlewaretoken="+ $('input').val() );
  xmlhttp.onreadystatechange=function()
  {

    var jsonResponse = new Object();
    jsonResponse = JSON.parse(xmlhttp.response);

    if (jsonResponse.authenticated){
          document.getElementById("login_response").innerHTML = "Welcome Back, " + jsonResponse.username;
          document.getElementsByClassName("main-container")[0].style.backgroundColor = "#468966";
          setTimeout(function()
          {
            window.location.replace(jsonResponse.redirect);
          },1000);
    } 
    else {
      document.getElementById("login_response").innerHTML = "Sorry, but the login information you have entered is invalid";
        document.getElementsByClassName("main-container")[0].style.backgroundColor = "#8E2800";
    }   
  
  };
}, false);