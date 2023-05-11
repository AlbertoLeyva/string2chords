def string_to_chords(string):

    chordArr = []
    lyricArr = []

    chordString = ""
    lyricString = ""

    if string == "":
        print("Cadena vacía")
        return
    
    chordAux = 0
    lyricAux = 0

    for i in range(0, len(string)):

        if string[i] == "[":

            if lyricAux != 0:
                chordString = chordString[:-lyricAux+2] 

            start = i
            end = 0

            for j in range(start, len(string)):

                if string[j] == "]":
                    end = j
                    break

            chordAux = end - start
            lyricAux = end - start
            chordString = chordString[:-1]

            for k in range(start + 1, end):
                chordString += string[k]
            
        elif string[i] == "]":
        
            lyricString = lyricString[:-chordAux+1]
            chordAux = 0

        elif string[i] == "*" or string[i] == "$":

            chordArr.append(chordString)
            lyricArr.append(lyricString)

            chordString = ""
            lyricString = ""

            lyricAux = 0

        elif chordAux != 0:

            lyricString += string[i]
            

        else:
            lyricString += string[i]
            chordString += "."
            

    for i in range(0,len(chordArr)):
        print(chordArr[i])
        print(lyricArr[i])

string_to_chords("hola[C] como te va[D]*espero[S] que bien$")