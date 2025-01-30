class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        return (sum(enemyEnergies[1:]) + currentEnergy) // enemyEnergies[0] if currentEnergy >= enemyEnergies[0] else 0

