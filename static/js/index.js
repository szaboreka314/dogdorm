window.addEventListener('DOMContentLoaded', ()=>{

    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
})