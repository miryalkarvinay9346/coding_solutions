def remove_duplicates(nums):
   # write your function here...
   k=list(set(nums))
   nums[:len(k)]=k[:len(k)]
   return (len(k))
   #print(k)