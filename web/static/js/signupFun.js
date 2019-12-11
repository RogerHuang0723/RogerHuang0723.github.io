// $(document).ready(function() {
//    if($("#password").text()=="" || $("#email").text()=="" || $("#username").text()==""){
//         $("#submit").attr('disabled',true);
//    }else{
//     $("#submit").attr('disabled',false);
//    }
//   })


function CheckAllField(){

    if($("#username").val().length<1 || $("#email").val().length<5 || $("#password").val().length<8){
        return false;
    }
    else{
        return true;
    }
  }

$("#password").on('keydown keyup keypress change',function(){
    var intCount=$("#password").val().length;
    var txtpassError=$("#passwordError");
    if(intCount<8){
      txtpassError.text("密碼需超過8個字");
    }
    else{
      txtpassError.text("");
    }
  })
  
  $("#email").on('keydown keyup keypress change',function(){
    var intCount=$("#email").val().length;
    var txtpassError=$("#emailError");
    if(intCount<5){
      txtpassError.text("帳號需超過5個字");
    }
    else{
      txtpassError.text("");
    }
  })
  
  $("#username").on('keydown keyup keypress change',function(){
    var intCount=$("#username").val().length;
    var txtpassError=$("#nameError");
    if(intCount<1){
      txtpassError.text("姓名不可為空");
    }
    else{
      txtpassError.text("");
    }
  })
  
  $("#submit").click(function(){
    if(CheckAllField()==false){
        $("#checkError").text("請檢查以上欄位都有輸入正確");
        return false;
    }
    else{
        return true;
    }
  })
