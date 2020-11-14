document.addEventListener('DOMContentLoaded',()=>{
    var form = document.getElementById('contact-form')
    var name = document.getElementById('name-field')
    var email = document.getElementById('email-field')
    var subject = document.getElementById('subject-field')
    var message = document.getElementById('message-field')
    var csrfMiddlewareToken = form.childNodes[1].getAttribute('value')
    var spinner = document.getElementById('spinner-contact')

    form.addEventListener('submit',(event)=>{
        event.preventDefault()
        nameValue = name.value.trim()
        emailValue = email.value.trim()
        subjectValue = subject.value.trim()
        messageValue = message.value.trim()
        name.value = ""
        name.disabled = true
        email.value = ""
        email.disabled = true
        subject.value = ""
        subject.disabled = true
        message.value = ""
        message.disabled = true
        spinner.style.display = 'block'
        $.ajax({
        url : window.location.href, // the endpoint
        type : "POST", // http method
        data : { name:nameValue, email:emailValue, subject:subjectValue, message:messageValue, csrfmiddlewaretoken:csrfMiddlewareToken }, // data sent with the post request

         //handle a successful response
        success : function(json) {
            name.disabled = false
            email.disabled = false
            subject.disabled = false
            message.disabled = false
            spinner.style.display = 'none'
            window.alert('Your message has been sent successfully')
        },
//
//        // handle a non-successful response
//        error : function(xhr,errmsg,err) {
//            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
//            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
//        }
    });
    })
})

