const username = document.getElementById("username");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirm-password");
const email = document.getElementById("email");

document.getElementById("register-btn").addEventListener("click", function() {
    
  const data = {
    username: username.value,
    password: password.value

  };

  fetch("/user/register", {  
    method: "POST",         
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': '{{ csrf_token }}',  // Django CSRF 令牌
      },
    body: new URLSearchParams({
        'username': username,
        'password': password,
        'confirm-password': confirmPassword,
        'email': email
    })
    
  })   
   .then(response => response.json())
   .then(data => {
      console.log(data);        
      if (data.status === '200') {
        alert(data.message);
        // 可以重定向到某个页面
        window.location.href = '';
       // #TODO 重定向到某个页面
      } else {
        alert(data.message);
      }



      if(data.success) {
        alert("Registration successful");
        window.location.href = "http://localhost:3000/login";
      } else {
        alert("Registration failed");        
      }
    })
   .catch(error =>{ 
    console.log(error);
      alert("Registration failed");});
});


