<html>
<head>
<title>Pentester Lab: Week 3</title>
</head>
<body>
<?php
$server_name = "127.0.0.1";
$user_name = "root";
$password = "password";
$database_name = "PentestersLab";

// Creating the connection
$connection = new mysqli($server_name, $user_name, $password, $database_name);


// Check this connection
if ($connection->connect_error) {
    die("Connection failed: " . mysql_error());
}

// MySQL query and results 
$query = "SELECT * FROM `Week3` WHERE `id`=" . $_GET['id'];
$result = mysqli_query($connection, $query);

while($row = mysqli_fetch_array($result)) {
echo "[ID: " . $row['ID']  . "] " . $row['value'];
}

mysqli_close($connection)
?>
</body>
</hmtl>
