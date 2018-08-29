class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        min_gas, min_gas_loc = 0, -1
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < min_gas:
                min_gas = tank
                min_gas_loc = i
        return min_gas_loc+1
