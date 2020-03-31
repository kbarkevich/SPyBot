$('#messageForm').submit(function(e){
    e.preventDefault();
    $.ajax({
        url: '/sendmsg',
        type: 'post',
        data: $('#messageForm').serialize(),
        success:function(){
            console.log("Did it!");
        }
    });
    $("#message").val("");
});

function backHome() {
    location.href = "/";
}