mydict = {"Fast": "In a quick manner",
          "Raj": "A coder",
          "Marks": [1, 2, 5],
          "anotherdict": {'raj': 'player'},
          1: 2
          }
'''print(mydict['Fast'])
print(mydict['Marks'])
print(mydict['anotherdict']['raj'])
mydict['Marks'] = [45, 78]       # DICTIONARY IS MUTABLE
print(mydict['Marks'])  '''

#DICTIONARY METHODS
print(mydict.keys())   #PRINTS THE KEYS OF THE DICTIONARY
print(mydict.values())   # PRINTS THE VALUES
print(mydict.items())   # PRINTS THE (KEY, VALUE) FOR ALL CONTENTS OF THE DICTIONARY
print(mydict)
updatedict = {
    "lovish": "friend",
    "divya": "friend",
    "shubham": "friend"
}
mydict.update(updatedict)    # UPDATES THE DICTIONARY BY ADDING KEY-VALUE PAIRS FROM UPDATEDICT
print(mydict)
print(mydict.get("Raj2"))   # RETURNS NONE AS Raj2 IS NOT PRESENT IN THE DICTIONARY
print(mydict["Raj2"])       # THROWS AN ERROR AS Raj2 IS NOT PRESENT IN THE DICTIONARY
