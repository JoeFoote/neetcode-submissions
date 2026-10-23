class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        if height[p1] > height[p2]:
            peak = p1
        else:
            peak = p2
        vols = []
        while p1 < p2:
            if height[peak] > height[p1]:
                local_peak = height[p1]
                p1 += 1
                #print(f"Left side: local peak: {local_peak}, p1: {p1}")
                #print(height[p1] < local_peak)
                while (height[p1] < local_peak):
                    # Add volume if dips are found
                    vols.append((local_peak - height[p1]))
                    p1 += 1
                # while loop stops when a higher local peak is
                # found. Check if higher than max peak. 
                if height[p1] > height[peak]:
                    peak = p1
                
            else:
                local_peak = height[p2]
                p2 -= 1
                #print(f"Right side: local peak: {local_peak}, p1: {p2}")
                while(height[p2] < local_peak):
                    vols.append((local_peak - height[p2]))
                    p2 -= 1
                if height[p2] > height[peak]:
                    peak = p2
        return sum(vols)