# Trader Odyssey: The Seafarer's Venture

**Trader Odyssey** is a multiplayer game where players navigate through a world of islands, engage in trade, embark on adventurous quests, and partake in thrilling sea battles.

## Table of Contents
1. [Current State of the Game](#current-state-of-the-game)
2. [Game Overview](#game-overview)
3. [Resources Gathering and Consumption](#resources-gathering-and-consumption)
4. [Business Trade](#business-trade)
5. [Ships](#ships)
6. [Combat](#combat)
7. [Base](#base)
8. [Adventures](#adventures)
9. [Player Interaction](#player-interaction)
10. [Achievements & Progression](#achievements-&-progression)
11. [Monetization](#monetization)
12. [Player Toolbar](#player-toolbar)
13. [How to Contribute](#how-to-contribute)

### Current State of the Game
Trader Odyssey is in its early stages of development. The current build offers:
- Player login and session management.
- Dashboard showcasing player resources, ship details, weapons, tools, and logs.
- Backend fetching and updating of player data.

### Game Overview
The world of **Trader Odyssey** comprises various islands including Tropical, Snowy, Deserted, and Volcanic. Each island type possesses unique resources and challenges. With an ever-evolving economy, real-time naval battles, adventurous quests, and deep player interaction, your journey through this world will be a captivating odyssey.

### Resources Gathering and Consumption
#### Primary Resources:
- **Wood, Stone, Metal**:
  - Gathering rate: 10-50 units/hr based on the island type.
  - Consumption: Ships require 2 wood, 1 metal per repair point.
  - Uses: Building and repairs.
  
- **Food**:
  - Gathering rate: 5-30 units/hr (through fishing or island gathering).
  - Consumption: 1 food unit per crew member per hour. It depletes faster during voyages.
  
#### Secondary Resources:
- **Cloth**: Crafted using 2 units of food (from cotton farms).
- **Gunpowder**: Crafted with 1 unit of metal and 1 unit of stone.
- **Spices**: Can be found on specific islands or acquired through trade.

#### Tertiary Resources (Valuables):
- Acquired during adventures, trades, or combats.
- Finding rate: Rare events with a 5% chance during adventures.

### Business Trade
- **Trade Route Profitability**: Depends on supply and demand. For instance, buy spices at Island A for 10 gold, sell at Island B for 20 gold if B lacks spices.
- **Blockade Routes**: Players can demand tolls which range between 10-50% of the trade value.

### Ships
- **Upgrades**:
  - Enhanced Cannons: Cost - 50 metal, 30 wood.
  - Faster Sails: Cost - 40 cloth, 20 wood.
  
- **Maintenance**: 
  - Ships degrade over time or when caught in storms.
  - Degradation rate: Ships lose 1-5% of their integrity per hour based on external conditions.

### Combat
#### Naval Combat:
- **Cannon Damage**: Varies by type; standard cannons cause 10 damage, enhanced ones cause 15.
- **Ship Health**: 
  - Frigate: 100 HP
  - Merchant Ship: 120 HP
  - Battleship: 150 HP
  - Explorer: 130 HP
  
- **Range Advantage**: Long-range cannons cause 80% damage but from a safer distance.

#### Boarding Combat:
Engage in intense close-quarters combat where the strength of the crew is determined by their food level, morale, and weapons. The outcome of these skirmishes can greatly affect the resources looted or lost.

### Base
#### Upgrades:
- Harbor Level 2: Costs 200 wood and 100 stone.
- Warehouse Level 2: Requires 100 wood, 50 stone, and 50 metal. This upgrade boosts storage capacity by 50%.

### Adventures
- **Success Rates**:
  - Treasure Hunts: 60% success, but with a quality map, the chances increase by 10%.
  - Ghost Ships: 40% success rate but with higher rewards.
  - Mystical Islands: These rare islands, appearing only 5% of the time, promise triple resources.

### Player Interaction
- **Trade Agreements**: Set a contract with terms including duration, resource amount, and price. Breaching these contracts results in a loss of reputation points.
- **Wars**: Declaring wars has its cost in resources but allows for unrestricted combat against rival guilds.

### Achievements & Progression
- **Titles**: Earn titles based on achievements.
  - Trader: Complete 100 successful trades.
  - Warrior: Emerge victorious in 50 battles.
  
- **Access**: Certain prestigious markets only open their doors to those with specific titles or achievements.

### Monetization
- **Cosmetic Items**: These are available for players who want to enhance their visual experience.
- **Boosts**: 
  - Speed Boost: Increases ship speed by 20% for 1 hour.
  - Combat Boost: Amplifies cannon damage by 10% for a single battle.

### Player Toolbar
- **Compass**: Directs players to a location but comes with a 10-minute cooldown.
- **Spyglass**: Can be used anytime, but only lasts for a 5-minute duration.

### How to Contribute
We're thrilled to have you on board! Here's how you can contribute:

1. **Fork the Repository**: Start by forking this repository.
2. **Set Up Environment**: Ensure you have all the necessary software and packages installed. You'd need PHP, a local server (like XAMPP), and a MySQL database.
3. **Pick an Issue**: Look through the issues or milestones. Pick something that appeals to you.
4. **Code**: Make your changes. Ensure you adhere to the code structure and conventions already in place.
5. **Test**: Before submitting a pull request, make sure your changes don't break any existing functionality and that they work as expected.
6. **Submit a Pull Request**: Once you're satisfied with your changes, submit a pull request. Make sure to provide a detailed description of the changes you made.

If you have ideas for new features or improvements, please create an issue to discuss them before working on them. This ensures that your efforts align with the game's direction and vision.

---
We hope to see **Trader Odyssey** sail to new horizons with your support! 🌊⚓
