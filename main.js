function SubmitForm(){
    $.ajax({
        url:"https://api.apispreadsheets.com/data/2872/",
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