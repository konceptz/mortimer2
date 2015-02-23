// form handlers for application functions

$(".mod_cred").submit(function(event){
    var form = $(this);
    if(form[0].button.value =="Show Creds"){

        $.post(
            "/mod_creds/",
            form.serializeArray(),
            function(response, textStatus, jqXHR){
                form[0].parentNode.getElementsByClassName('creds')[0].innerHTML = response;
            });
        form[0].button.value ="Hide Creds";
        event.preventDefault();
    }
    else{
        form[0].parentNode.getElementsByClassName('creds')[0].innerHTML = "";
        form[0].button.value ="Show Creds";
        event.preventDefault();
    }
});

$(".rm_cred").submit(function(event){
    var form = $(this);
    $.post(
            "/remove_creds/",
            form.serializeArray(),
            function(response, textStatus, jqXHR){
                console.log(response);                  // for debugging only
            });
    event.preventDefault();
});

$(".mk_cred").submit(function(event){
    var form = $(this);
    $.post(
            "/create_creds/",
            form.serializeArray(),
            function(response, textStatus, jqXHR){
                console.log(response);                  // for debugging only
            });
    event.preventDefault();
});
