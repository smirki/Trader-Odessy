<?php
session_start();
include 'dbconnect.php';
include 'PlayerDashboard.php';

try {
    $response = [];
    $dashboard = new PlayerDashboard($connection, $_SESSION["id"]);

    $response["resources"] = $dashboard->getResources();
    $response["otherResources"] = $dashboard->getOtherResources();
    $response["ship"] = $dashboard->getShipDetails();
    $response["weaponsTools"] = $dashboard->getWeaponsAndTools();

    echo json_encode($response);
} catch (Exception $e) {
    echo json_encode(['error' => $e->getMessage()]);
}

?>
