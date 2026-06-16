var form = document.getElementById("form");
form.addEventListener("submit", function(event) {
    event.preventDefault(); validation()});

function validation() {
    var name = document.getElementById("name");
    var message = document.getElementById("message");
    var err_name = document.getElementById("name_div");
    var err_message = document.getElementById("mes");
    err_name.innerHTML = "";
    err_message.innerHTML = "";
    name.classList.remove('error');
    message.classList.remove('error');
    var flag = true;
    
    if (name.value.length < 3)
    {
        name.classList.add('error');
        err_name.innerHTML = "Ваше имя должно быть больше трех символов";
        flag = false;
    }
    if (message.value.length < 10)
    {
        message.classList.add('error');
        err_message.innerHTML = "Ваше сообщение должно быть больше десяти символов";
        flag = false;
    }
    if (flag)
    {
        form.submit();
    }

}