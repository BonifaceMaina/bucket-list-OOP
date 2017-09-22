
function check_password(){
  if (document.getElementById('password').value == document.getElementById('confirmPassword').value) {
    document.getElementById('submit').disabled = false;
  }
  else{
    document.getElementById('submit').disabled = true;
  }
}


 