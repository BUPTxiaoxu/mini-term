const faceImg = document.getElementById("face-img");
const faceName = document.getElementById("face-name");


// document.getElementById("room-info-btn").addEventListener("click", function() {
//     window.location.href = "/room-info/";
// });

// document.getElementById("user-management-btn").addEventListener("click", function() {
//     window.location.href = "/user-management/";
// });

document.getElementById("add-face-btn").addEventListener("click", function() {

    fetch("/control/face/add", {  
        method: "POST",         
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}',  // Django CSRF 令牌
          },
        body: new URLSearchParams({
            'username': username,
            'confirm-password': confirmPassword,
        })

        
      })  
});

document.getElementById("remove-face-btn").addEventListener("click", function() {

    fetch("/control/face/delete", {  
        method: "POST",         
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}',  // Django CSRF 令牌
          },
        body: new URLSearchParams({
            'username': username,
            'confirm-password': confirmPassword,
        })

        
      })  
});