<?php
$host = "localhost";
$db_name = "todo";
$username = "web";
$password = "password";

$conn =new mysqli($host, $username, $password, $db_name);
if($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

function saveData($name, $id, $conn){
$query = "INSERT INTO points(name, id) VALUES($name, $id)";
if($conn->query($query) === TRUE) {
return '<h3 style="text-align:center;">We will get back to you very shortly!</h3>';
}
return "Error: " . $sql . "<br>" . $conn->error;
}

if( isset($_GET['submit'])){
$name = mysqli_real_escape_string($conn, $_GET['name']);
$id = mysqli_real_escape_string($conn, $_GET['id']);

//then you can use them in a PHP function. 
$result = saveData($name, $id, $conn);
echo $result;
}
else{
echo '<h3 style="text-align:center;">A very detailed error message ( ͡° ͜ʖ ͡°)</h3>';
}
?>
