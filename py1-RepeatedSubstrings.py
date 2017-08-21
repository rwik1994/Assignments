class RepeatedSubstrings():
    def decompress(self,compressed):
        repeats = compressed.split('&')
        #print repeats
        decom=""
        decompressed=""
        temp=""
        for i in repeats:
            if i!="" and repeats[repeats.index(i)][0].isdigit()==True:
                splitlist=i.split('-')
                #print splitlist
                #print "Under splitlist"
                if splitlist[1].isdigit()==True:
                    #print "Ekhane dhuklo"
                    if compressed[int(splitlist[0]):int(splitlist[1])].isalpha()==True:
                        #print "Now here"
                        #print splitlist[1]
                        concat=compressed[int(splitlist[0]):int(splitlist[1])]
                        if repeats[repeats.index(i)].isalpha()==True:
                            decompressed=repeats[repeats.index(i)]+concat
                    else:
                        decompressed=("?"*(int(splitlist[1])-int(splitlist[0])+1))
                else:
                    for i,c in enumerate(splitlist[1]):
                        #print c
                        if c.isdigit()==True:
                            temp=temp+c
                        else:
                            break
                    #print temp
                    if compressed[int(splitlist[0]):int(temp)].isalpha()==True:
                        #print "Oh achha ekhane"
                        concat=compressed[int(splitlist[0]):int(temp)]
                        if repeats[repeats.index(i)].isalpha()==True:
                            decompressed=repeats[repeats.index(i)]+concat
                    else:
                        #print "Tahle ekhne"
                        decompressed=("?"*(int(temp)-int(splitlist[0])+1))
                    temp=""
            else:
                decompressed=repeats[repeats.index(i)]
            decom=decom+decompressed                
        return decom
