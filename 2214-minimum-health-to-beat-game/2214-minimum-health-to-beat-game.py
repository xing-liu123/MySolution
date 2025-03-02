class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        maxDamage = max(damage)

        damageReduction = min(maxDamage, armor)

        return sum(damage) - damageReduction + 1