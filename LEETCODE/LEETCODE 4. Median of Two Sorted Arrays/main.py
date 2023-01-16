def functio():
    nums1 = [1,3]
    nums2 = [2,7]
    nums1_l = float(len(nums1))
    nums2_l = float(len(nums2))
    nums1_m = int(len(nums1)/2)
    nums2_m = int(len(nums2)/2)
    if (not nums1_l%2): #se è pari
        nums1_m = nums1_m -1
    if (not nums2_l%2): #se è pari
        nums2_m = nums2_m -1
    nums3 = []
    if (not nums1_l):
        if (nums2_l%2):
            return  nums2[int(nums2_l/2)]
        else:
            return (nums2[int(nums2_l/2)] + nums2[int(nums2_l/2)-1])/2
    if (not nums2_l):
        if (nums1_l%2):
            return  nums1[int(nums1_l/2)]
        else:
            return (nums1[int(nums1_l/2)] + nums1[int(nums1_l/2)-1])/2
    if (nums1[nums1_m]>nums2[nums2_m]):
        nums3.append(nums2[nums2_m])
        nums3.append(nums1[nums1_m])
        first = 1
    else:
        nums3.append(nums1[nums1_m])
        nums3.append(nums2[nums2_m])
        first = 2
    l1 = nums1_m-1
    r1 = nums1_m+1
    l2 = nums2_m-1
    r2 = nums2_m+1
    l3 = 0
    r3 = 1
    rimanenti1_l = l1+1
    rimanenti1_r = int(nums1_l-r1)
    rimanenti2_l = l2+1
    rimanenti2_r = int(nums2_l-r2)
    leftStop = True
    rightStop = True
    #left side
    if (first==2):
        while(leftStop):
            if (l2<0 or nums2[l2]<=nums3[l3]):
                leftStop = False
            else:
                nums3.insert(1,nums2[l2])
                l2=l2-1
                r3=r3+1
                rimanenti2_l=rimanenti2_l-1
    if (first==1):
        while(leftStop):
            if (l1<0 or nums1[l1]<=nums3[l3]):
                leftStop = False
            else:
                nums3.insert(1,nums1[l1])
                l1=l1-1
                r3=r3+1
                rimanenti1_l=rimanenti1_l-1
    #right side
    if (first==2):
        while(rightStop):
            if (r1>=nums1_l or nums1[r1]>=nums3[r3]):
                rightStop = False
            else:
                nums3.insert(r2,nums1[r1])
                r1=r1+1
                r3=r3+3
                rimanenti1_r=rimanenti1_r-1
    if (first==1):
        while(rightStop):
            print(r2)
            if (r2>=nums2_l or nums2[r2]>=nums3[r3]):
                rightStop = False
            else:
                nums3.insert(r2,nums2[r2])
                r2=r2+1
                r3=r3+3
                rimanenti2_r=rimanenti2_r-1
    
    len_tot = (rimanenti1_l + rimanenti2_l + int(len(nums3)) + rimanenti1_r + rimanenti2_r)

    if (len_tot%2 == 1):
        return(nums3[int(len_tot/2)-rimanenti1_l-rimanenti2_l])
    return(nums3[int(len_tot/2)-rimanenti1_l-rimanenti2_l] + nums3[int(len_tot/2)-rimanenti1_l-rimanenti2_l+1])/2


if __name__ == "__main__":
    functio()




