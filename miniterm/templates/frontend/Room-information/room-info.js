const temperatureElement = document.getElementById("temp-value");
const humidityElement = document.getElementById("hum-value");
const faceElement = document.getElementById("face-name");
const resultElement = document.getElementById("result-value");
const faceTimeElement = document.getElementById("face-time");
const eventElement = document.getElementById("event-value");
const timeElement = document.getElementById("time");

fetch("/log/temp", {
    method: "GET",
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-CSRFToken': '{{ csrf_token }}',  // Django CSRF 令牌
      }})
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.status === "200") {
            temperatureElement.innerHTML = data.temperature + "°C";
            humidityElement.innerHTML = data.humidity + "%";
            // faceElement.innerHTML = data.face;
            // eventElement.innerHTML = data.event;
            timeElement.innerHTML = data.time;
        } else {
            console.log("Error: " + data.message);
        }
    })
    .catch(error => console.error(error));

fetch("/log/face", {
        method: "GET",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}',  // Django CSRF 令牌
          }})
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.status === "200") {
                faceElement.innerHTML = data.name;
                faceTimeElement.innerHTML = data.time;
                resultElement.innerHTML = data.result;
            } else {
                console.log("Error: " + data.message);
            }
        })
        .catch(error => console.error(error));

        fetch("/log/access", {
            method: "GET",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': '{{ csrf_token }}',  // Django CSRF 令牌
              }})
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.status === "200") {
                    // eventElement.innerHTML = data.event;
                    // timeElement.innerHTML = data.time;
                } else {
                    console.log("Error: " + data.message);
                }
            })
            .catch(error => console.error(error));




document.getElementById("control-system-btn").addEventListener("click", function() {
    window.location.href = "/control-system/";
});

document.getElementById("user-management-btn").addEventListener("click", function() {
    window.location.href = "/user-management/";
});