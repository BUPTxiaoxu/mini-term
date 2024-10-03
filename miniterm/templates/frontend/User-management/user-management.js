// This is the code for user management system.
//新增
const addBtn = document.getElementById("add-user-btn");
document.getElementById("add-user-btn").addEventListener("click", addRow);
function addRow() {
    var table = document.getElementById("user-list");
    //获取插入的位置
  var rowCount = table.rows.length;
  var newRow = table.insertRow(rowCount);
  var nameCell = newRow.insertCell(0);
  var passwordCell = newRow.insertCell(1);
  var roleCell = newRow.insertCell(2);
  var accessLevelCell = newRow.insertCell(3);
  var authorizationCell = newRow.insertCell(4);
  var actionCell = newRow.insertCell(5);
  
    nameCell.innerHTML = "undefined";
    passwordCell.innerHTML = "undefined";
    roleCell.innerHTML = "undefined";
    accessLevelCell.innerHTML = "undefined";
    authorizationCell.innerHTML = "undefined";
    actionCell.innerHTML = "<button onclick='editRow(this)'>Edit</button><button onclick='deleteRow(this)'>Remove</button>";
}

//編輯

//刪除
function deleteRow(btn) {
    var row = btn.parentNode.parentNode;
    var table = document.getElementById("user-list");
    table.deleteRow(row.rowIndex);

    //delete from database here 
    fetch('/user/delete', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-CSRFToken': '{{ csrf_token }}',  // Django CSRF 令牌
        },
        body: new URLSearchParams({
            name: row.cells[0].innerHTML,
            password: row.cells[1].innerHTML,
            role: row.cells[2].innerHTML,
            access_level: row.cells[3].innerHTML,
            authorization: row.cells[4].innerHTML,
        })//这里接口文档参数是UserID
    })
   .then(response => response.json())
   .then(data => {
        console.log(data);
        if (data.status === '200') {
          alert("Deleted successfully");
        } else {
          alert("Failed to delete data");
        }
    })
   .catch(error => {
    console.error(error);
    alert("Failed to delete data");
    });
}

//編輯
function editRow(btn) {
    var row = btn.parentNode.parentNode;
    var nameCell = row.cells[0];
    var passwordCell = row.cells[1];
    var roleCell = row.cells[2];
    var accessLevelCell = row.cells[3];
    var authorizationCell = row.cells[4];
    var actionCell = row.cells[5];
    nameCell.innerHTML = "<input type='text' value='" + nameCell.innerHTML + "'>";
    passwordCell.innerHTML = "<input type='text' value='" + passwordCell.innerHTML + "'>";
    roleCell.innerHTML = "<input type='text' value='" + roleCell.innerHTML + "'>";
    accessLevelCell.innerHTML = "<input type='text' value='" + accessLevelCell.innerHTML + "'>";
    authorizationCell.innerHTML = "<input type='text' value='" + authorizationCell.innerHTML + "'>";
    actionCell.innerHTML = "<button onclick='saveRow(this)'>Save</button><button onclick='cancelEdit(this)'>Cancel</button>";
}

function saveRow(btn) {
    var row = btn.parentNode.parentNode;
    var nameCell = row.cells[0];
    var passwordCell = row.cells[1];
    var roleCell = row.cells[2];
    var accessLevelCell = row.cells[3];
    var authorizationCell = row.cells[4];
    var actionCell = row.cells[5];
    nameCell.innerHTML = nameCell.getElementsByTagName("input")[0].value;
    passwordCell.innerHTML = passwordCell.getElementsByTagName("input")[0].value;
    roleCell.innerHTML = roleCell.getElementsByTagName("input")[0].value;
    accessLevelCell.innerHTML = accessLevelCell.getElementsByTagName("input")[0].value;
    authorizationCell.innerHTML = authorizationCell.getElementsByTagName("input")[0].value;
    actionCell.innerHTML = "<button onclick='editRow(this)'>Edit</button><button onclick='deleteRow(this)'>Remove</button>";

    //save to database here 
    fetch('/user/add', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-CSRFToken': '{{ csrf_token }}',  // Django CSRF 令牌
        },
        body: new URLSearchParams({
            name: nameCell.getElementsByTagName("input")[0].value,
            password: passwordCell.getElementsByTagName("input")[0].value,
            role: roleCell.getElementsByTagName("input")[0].value,
            access_level: accessLevelCell.getElementsByTagName("input")[0].value,
            authorization: authorizationCell.getElementsByTagName("input")[0].value,
        })
    })
   .then(response => response.json())
   .then(data => {
        console.log(data);
        if (data.status === '200') {
          alert("Saved successfully");
        } else {
          alert("Failed to save data");
        }
    })
   .catch(error => {
    console.error(error);
    alert("Failed to save data");
    });
}



