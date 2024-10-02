// This is the code for user management system.
//新增
const addBtn = document.getElementById("add-user-btn");
Document.getElementById("add-user-btn").addEventListener("click", addRow);
function addRow() {
    var table = document.getElementById("user-list");
    //获取插入的位置
  var rowCount = table.rows.length;
  var newRow = table.insertRow(rowCount);
  var nameCell = row.insertCell(0);
  var passwordCell = row.insertCell(1);
  var roleCell = row.insertCell(2);
  var accessLevelCell = row.insertCell(3);
  var authorizationCell = row.insertCell(4);
  var actionCell = row.insertCell(5);
  
  
nameCell.innerHTML = "undefined";
passwordCell.innerHTML = "undefined";
roleCell.innerHTML = "undefined";
accessLevelCell.innerHTML = "undefined";
authorizationCell.innerHTML = "undefined";
}

//編輯

//刪除
function deleteRow(btn) {
    var row = btn.parentNode.parentNode;
    var table = document.getElementById("user-list");
    table.deleteRow(row.rowIndex);
}
