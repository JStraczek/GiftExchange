function SubmitForm(){
    $.ajax({
        url:"INSERT HERE", // INSERT YOUR SPREADSHEETS API LINK
        type:'post',
        data:$("#userInputForm").serializeArray(),
        success: function(){
          alert("Form Data Submitted :)")
        },
        error: function(){
          alert("There was an error :(")
        }
    })
};
