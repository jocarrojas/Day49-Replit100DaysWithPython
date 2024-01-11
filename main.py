#Read in the data from the high.score file.
f=open("high.score","r")
allData={}
x=0
maxScore=0
while True:
    contents=f.readline().strip()
    if contents=="":
      break
    x+=1
    splitContents=contents.split(" ")
    splitContents[1]=int(splitContents[1])
    allData[x]=splitContents

    #Identify which of those users had the highest score. Automatically! (Not you doing it!)
    if splitContents[1]>maxScore:
        maxScore=splitContents[1]

#Output the name and score of the winner.
for key,value in allData.items():
  if value[1]==maxScore:
    print(f'The winner is {value[0]} with {value[1]}.')



