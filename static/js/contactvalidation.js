// function nameValidation(name){
//     if (name === ""){
//         console.log(false)
//         return false
//     }
//     else {
//         console.log(true)
//         return true
//     }
// }

// function emailValidation(email){
//     if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email)){
//       console.log(true)
//       return true
//     }else {
//         console.log(false)
//         return false
//     }
// }

// csrfmiddlewaretoken

document.addEventListener("DOMContentLoaded", function(){
    const name = document.getElementById('name-form')
    console.log(name)
    const email = document.getElementById('email-form')
    const subject = document.getElementById('subject-form')
    const textarea = document.getElementById('textarea-form')
    const form = document.getElementById('contact-form')
    const csrfmiddleware = form.childNodes[1].getAttribute("value")
    const spinner = document.getElementById('spinner')
    console.log(spinner)

    form.addEventListener('submit', (event) => {
        nameValue = name.value.trim()
        emailValue = email.value.trim()
        subjectValue = subject.value.trim()
        textareaValue = textarea.value.trim()
        event.preventDefault()
        spinner.style.display = "block"
        $.ajax({
            url : window.location.href, // the endpoint
            type : "POST", // http method
            data : { name : nameValue,
                     email:emailValue,
                     subject:subjectValue,
                     textarea:textareaValue,
                     csrfmiddlewaretoken:csrfmiddleware 
            }, // data sent with the post request

            // // handle a successful response
            success : function(response) {
                // $('#post-text').val(''); // remove the value from the input
                spinner.style.display = "none"
                name.value = ""
                email.value = ""
                subject.value = ""
                textarea.value = ""
                alert('Your message has been sent successfully')
                console.log("success"); // another sanity check
                console.log(response.data); // log the returned json to the console
            },
        
            // handle a non-successful response
            // error : function(xhr,errmsg,err) {
            //     $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
            //         " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            //     console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            // }
        });
    })
});



