class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []
        seen = set()
        nums = sorted(nums)
        for p1 in range(len(nums)):
            target = nums[p1] * -1
            p2 = p1+1
            p3 = len(nums)-1
            while(p2 < p3):
                if nums[p2] + nums[p3] == target:
                    trip = frozenset({nums[p1], nums[p2], nums[p3]})
                    if trip not in seen:
                        seen.add(trip)
                        trips.append([nums[p1], nums[p2], nums[p3]])
                if nums[p2] + nums[p3] > target:
                    p3 -= 1
                else:
                    p2 += 1

        return trips