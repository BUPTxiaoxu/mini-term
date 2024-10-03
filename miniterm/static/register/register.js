const username = document.getElementById("username");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirm-password");
const email = document.getElementById("email");

document.getElementById("register-btn").addEventListener("click", function() {
    // 输入验证
    if (username.value.trim() === '' || password.value.trim() === '' || email.value.trim() === '') {
        alert("请填写所有必填字段");
        return; // 终止执行
    }

    if (password.value !== confirmPassword.value) {
        alert("密码不匹配");
        return; // 终止执行
    }

    const data = {
        username: username.value,
        password: password.value,
        email: email.value
    };

    fetch("/user/register", {  
        method: "POST",         
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}',  // Django CSRF 令牌
        },
        body: new URLSearchParams(data)
    })   
    .then(response => response.json())
    .then(data => {
        console.log(data);        
        if (data.status === '200') {
            alert(data.message);
            window.location.href = 'login';  // 重定向到登录页面
        } else {
            alert(data.message);
        }
    })
    .catch(error => { 
        console.log(error);
        alert("注册失败");
    });
});


