// form handlers for application functions

$(".app").submit(function(event){
    var form = $(this);
    if(form[0].button.value =="Show Creds"){

        $.post(
            "/get_creds/",
            form.serializeArray(),
            function(response, textStatus, jqXHR){
                form[0].childNodes[1].childNodes[7].innerHTML = response;                   //TODO: find better way to do this.
            });
        form[0].button.value ="Hide Creds";
        event.preventDefault();
    }
    else{
        form[0].childNodes[1].childNodes[7].innerHTML = "";                                 //TODO: and this too.
        form[0].button.value ="Show Creds";
        event.preventDefault();
    }
});

$(".rm").submit(function(event){
    var form = $(this);
    $.post(
            "/remove/",
            form.serializeArray(),
            function(response, textStatus, jqXHR){
                console.log(response);                  // for debugging only
            });
    event.preventDefault();
});

$(".mk").submit(function(event){
    var form = $(this);
    $.post(
            "/create/",
            form.serializeArray(),
            function(response, textStatus, jqXHR){
                console.log(response);                  // for debugging only
            });
    event.preventDefault();
});
