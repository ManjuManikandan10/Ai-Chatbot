async function sendMessage(){

    let message=document.getElementById("message").value;

    if(message==""){
        return;
    }

    let chatBox=document.getElementById("chat-box");

    chatBox.innerHTML += "<p class='user'><b>You:</b> "+message+"</p>";

    let response=await fetch("/ask",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    let data=await response.json();

    chatBox.innerHTML += "<p class='bot'><b>Bot:</b> "+data.answer+"</p>";

    document.getElementById("message").value="";

    chatBox.scrollTop=chatBox.scrollHeight;

}