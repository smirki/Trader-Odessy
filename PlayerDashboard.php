<?php

class PlayerDashboard {
    private $connection;
    private $playerId;

    public function __construct($connection, $playerId) {
        $this->connection = $connection;
        $this->playerId = $playerId;
    }

    public function getResources() {
        $stmt = $this->connection->prepare("SELECT gold, doubloons, food FROM users WHERE id = ?");
        $stmt->bind_param("i", $this->playerId);
        $stmt->execute();
        return $stmt->get_result()->fetch_assoc();
    }

    public function getOtherResources() {
        $stmt = $this->connection->prepare("SELECT r.name, pr.quantity FROM player_resources pr JOIN resources r ON pr.resource_id = r.resource_id WHERE pr.player_id = ?");
        $stmt->bind_param("i", $this->playerId);
        $stmt->execute();
        $resources = [];
        $result = $stmt->get_result();
        while ($row = $result->fetch_assoc()) {
            $resources[] = $row;
        }
        return $resources;
    }

    public function getShipDetails() {
        $stmt = $this->connection->prepare("SELECT s.name, s.type, ps.health, ps.speed, ps.cargo_capacity, ps.cannon_count FROM player_ships ps JOIN ships s ON ps.ship_id = s.ship_id WHERE ps.player_id = ?");
        $stmt->bind_param("i", $this->playerId);
        $stmt->execute();
        return $stmt->get_result()->fetch_assoc();
    }

    public function getWeaponsAndTools() {
        $stmt = $this->connection->prepare("SELECT wt.name, wt.type, wt.power FROM player_weapons_tools pwt JOIN weapons_tools wt ON pwt.item_id = wt.item_id WHERE pwt.player_id = ?");
        $stmt->bind_param("i", $this->playerId);
        $stmt->execute();
        $weapons = [];
        $result = $stmt->get_result();
        while ($row = $result->fetch_assoc()) {
            $weapons[] = $row;
        }
        return $weapons;
    }
}

?>
