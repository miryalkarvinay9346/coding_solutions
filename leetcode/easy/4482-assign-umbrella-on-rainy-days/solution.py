class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        a=0
        b=0
        c=0
        k=["None"]*len(rain)
        for i in range(len(rain)-1):
            if rain[i]==rain[i+1]==1:
                if rain[i]==1:
                    if a>b:
                        k[i]="Bob"
                        b+=1
                    else:
                        k[i]="Alice"
                        a+=1      
                else:
                    a+=1
                    k[i]="Alice"
            elif rain[i]==1:
                b+=1
                k[i]="Bob"
            else:
                k[i]="None"
        if rain[len(rain)-1]==1:
            k[len(rain)-1]="Bob"
        return k
                
                