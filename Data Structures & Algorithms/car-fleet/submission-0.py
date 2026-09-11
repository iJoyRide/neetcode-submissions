class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        fleet = []

        cars.sort(reverse=True)

        for p, s in cars:
            time = (target - p) / s
            if len(fleet) == 0 or time > fleet[-1]:
                fleet.append(time)

        return len(fleet)

            
            