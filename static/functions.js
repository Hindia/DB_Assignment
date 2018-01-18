
$(function(){
	var operation = "A"; //"A"=Adding; "E"=Editing
	var selected_index = -1; //Index of the selected list item
	var tbClients = JSON.parse(request.responseText);
	//var tbClients = localStorage.getItem("tbClients");//Retrieve the stored data
	tbClients = JSON.parse(tbClients); //Converts string to object
	if(tbClients == null) //If there is no data, initialize an empty array
		tbClients = [];
});

function Add(){
	var data = JSON.stringify({
		ID    : $("#txtID").val(),
		Name  : $("#txtName").val(),
		Address : $("#txtAddress").val()
	});
	var request = new XMLHttpRequest();
	request.open("POST", "http://localhost:8000/companies/", false);
	request.setRequestHeader("Authorization", "Basic " + btoa("admin:password123"));
	request.setRequestHeader("X-CSRFToken", readCookie("csrftoken"));
	request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	request.send(data);
	alert("The data was saved.");
	var array = JSON.parse(request.responseText);
	console.log(array);
	return true;
} 
function Edit(){
	tbClients[selected_index] = JSON.stringify({
			ID    : $("#txtID").val(),
			Name  : $("#txtName").val(),
			Address : $("#txtAddress").val()
		});//Alter the selected item on the table
	localStorage.setItem("tbClients", JSON.stringify(tbClients));
	alert("The data was edited.");
	operation = "A"; //Return to default value
	return true;
}
function Delete(){
	tbClients.splice(selected_index, 1);
	localStorage.setItem("tbClients", JSON.stringify(tbClients));
	alert("Client deleted.");
	location.reload(true);
} 

function List(){		
	$("#tblList").html("");
	$("#tblList").html(
		"<thead>"+
		"	<tr>"+
		"	<th></th>"+
		"	<th>ID</th>"+
		"	<th>Name</th>"+
		"	<th>Address</th>"+
		"	</tr>"+
		"</thead>"+
		"<tbody>"+
		"</tbody>"
		);
	for(var i in tbClients){
		var cli = JSON.parse(tbClients[i]);
	  	$("#tblList tbody").append("<tr>"+
								 	 "	<td><img src='edit.png' alt='Edit"+i+"' class='btnEdit'/><img src='delete.png' alt='Delete"+i+"' class='btnDelete'/></td>" + 
									 "	<td>"+cli.ID+"</td>" + 
									 "	<td>"+cli.Name+"</td>" + 
									 "	<td>"+cli.Address+"</td>" + 
	  								 "</tr>");
	}
} 

$("#frmCadastre").bind("submit",function(){
	if(operation == "A")
		return Add();
	else
		return Edit();		
}); 
$(".btnEdit").live("click", function(){
	operation = "E";
	selected_index = parseInt($(this).attr("alt").replace("Edit", ""));
	var cli = JSON.parse(tbClients[selected_index]);
	$("#txtID").val(cli.ID);
	$("#txtName").val(cli.Name);
	$("#txtAddress").val(cli.Address);
	$("#txtID").attr("readonly","readonly");
	$("#txtName").focus();
}); 
$(".btnDelete").live("click", function(){
	selected_index = parseInt($(this).attr("alt").replace("Delete", ""));
	Delete();
	List();
}); 