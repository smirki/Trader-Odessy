<?php

$host = 'localhost';
$db_user = 'u176143505_to';
$db_pass = '$4VlfTfxz';
$db_name = 'u176143505_to';

$connection = new mysqli($host, $db_user, $db_pass, $db_name);

if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

?>