nums = [1]+list(map(int, input().split()));nejrada=["neni"];rada=[];prvnindex=0
for index, num in enumerate(nums): #pravý index je vždy - 1
    if (num%3==0) and ((nums[index-1]%3==0) or (nejrada[0]=="neni") or ((len(nejrada)==(len(rada)+1)) and (sum(nejrada)<sum([num]+rada))) or not(rada)):
        rada.append(num)
        if (len(rada)>len(nejrada)) or (nejrada[0]=="neni") or ((len(nejrada)==(len(rada))) and (sum(nejrada)<sum(rada))):nejrada=rada;prvnindex=index-len(nejrada)
        if ((index+1)==len(nums)): continue
        elif not(nums[index+1]%3==0):rada=[]
print(f"{prvnindex} {0 if nejrada[0] == "neni" else len(nejrada)} {0 if nejrada[0] == "neni" else sum(nejrada)}")