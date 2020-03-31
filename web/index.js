$('#channelForm').submit(function(e){
    console.log('DOIN IT');
    console.log($('#channelForm').serializeArray())
    e.preventDefault();
    location.href = "/channel/message/" + $('#channelForm').serializeArray()[0].value;
});