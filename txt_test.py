texto= "t a asdas aetaet ads bvxcb asdf sdfg as as sad fdf svz sey yty yttyytt at y ar 32 fdsfd sxdfsdf sdfsdfsdfsdfdbh 34g fdg y 6rdt"
txt_len=len(texto)
count=0
for i in range(txt_len-2):
    if(texto[i]=='t' and texto[i+1]== ' '):
        count+=1
print(count)