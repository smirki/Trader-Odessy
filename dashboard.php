<?php
session_start();

if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
    header("Location: login.html");
    exit;
}

include 'dbconnect.php';
?>

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, <?php echo $_SESSION["username"]; ?>!</h1>

    <h2>Your Resources:</h2>
    <ul>
        <li>Gold: <span id="gold"><?php echo $_SESSION["gold"]; ?></span></li>
        <li>Doubloons: <span id="doubloons"><?php echo $_SESSION["doubloons"]; ?></span></li>
        <li>Food: <span id="food"><?php echo $_SESSION["food"]; ?></span></li>
        <div id="otherResources"></div>
    </ul>

    <h2>Your Ship:</h2>
    <div id="shipDetails"></div>

    <h2>Your Weapons and Tools:</h2>
    <ul id="weaponsTools"></ul>

    <h2>Adventures:</h2>
    <div id="adventureLog"></div>

    <h2>Combat Log:</h2>
    <div id="combatLog"></div>

    <script>
    function updateDashboard() {
    fetch("update_dashboard.php")
        .then(response => response.json())
        .then(data => {
            // Update resources
            document.querySelector("#gold").textContent = data.resources.gold;
            document.querySelector("#doubloons").textContent = data.resources.doubloons;
            document.querySelector("#food").textContent = data.resources.food;
                
                let resourceDetails = "";
                for(let resource of data.otherResources) {
                    resourceDetails += `<li>${resource.name}: ${resource.quantity}</li>`;
                }
                document.querySelector("#otherResources").innerHTML = resourceDetails;
                
                let shipDetails = "You don't have a ship yet.";
                if (data.ship) {
                    shipDetails = `
                        Name: ${data.ship.name}<br>
                        Type: ${data.ship.type}<br>
                        Health: ${data.ship.health}<br>
                        Speed: ${data.ship.speed}<br>
                        Cargo Capacity: ${data.ship.cargo_capacity}<br>
                        Cannons: ${data.ship.cannon_count}<br>
                    `;
                }
                document.querySelector("#shipDetails").innerHTML = shipDetails;

                let weaponsToolsDetails = "";
                for(let item of data.weaponsTools) {
                    weaponsToolsDetails += `<li>${item.name} - Type: ${item.type} - Power: ${item.power}</li>`;
                }
                document.querySelector("#weaponsTools").innerHTML = weaponsToolsDetails;
            })
        .catch(error => {
            console.error("Error updating dashboard:", error);
        });

    setTimeout(updateDashboard, 5000); 
}
    updateDashboard();
    </script>

    <a href="logout.php">Logout</a>
</body>
</html>
