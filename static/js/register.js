$.noConflict();

jQuery(document).ready(function ($) {
    $("#register-form").submit(function (e) {
        e.preventDefault();
        let email = $("#email").val();
        let pass1 = $("#pass1").val();
        let pass2 = $("#pass2").val();
        mydata = {
            email: email,
            password: pass1,
            password2: pass2,
            csrfmiddlewaretoken: '{{ csrf_token }}'
        }
        console.log(mydata)
        $.ajax({
            url: "http://localhost:8000/accounts/register/",
            method: "POST",
            data: mydata,
            success: function (data) {
                console.log(data)
            }
        })
    });
})