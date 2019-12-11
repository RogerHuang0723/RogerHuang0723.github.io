$(document).ready(function() {
  var myJSON = JSON.parse(dic);
 
  // console.log(user);
  $('#result').text(myJSON.USER_ID);
});

$("#test-btn").click(function(){ 
  if($('#result').is(':visible')==true){
    // $('#result').text("");
    $("#result").hide();
  }
  else{
    
    // console.log(myJSON.OP_DATE);
    $("#result").show();
   
  }
  // var dic="{{title|escapejs}}";
  // console.log(dic.USER_TITLE);
  
})
