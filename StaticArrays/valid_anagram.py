def valid_anagram(s: str, t: str) -> bool:
    mapS = {}
    for element in s:
        if element in mapS:
            mapS[element] += 1
        else:
            mapS[element] = 1

    mapT = {}
    for element in t:
        if element in mapT:
            mapT[element] += 1
        else:
            mapT[element] = 1

    return True if mapT == mapS else False
    
print(valid_anagram("racecar","racecrar"))