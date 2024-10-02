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
}
