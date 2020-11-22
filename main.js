function SubmitForm(){
    if(document.getElementById("passwordInput").value == "INSERT HERE"){ // INSERT YOUR PASSWORD (IT'S NOT SAFE)
    $.ajax({
        url:"INSERT HERE", // INSERT YOUR SPREADSHEETS API LINK FOR IT TO WORK
        type:'post',
        data:$("#userInputForm").serializeArray(),
        success: function(){
          alert("Form Data Submitted :)")
        },
        error: function(){
          alert("There was an error :(")
        }
    })
  }
};

function CheckPassword(){

}