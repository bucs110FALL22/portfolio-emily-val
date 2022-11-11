#Part A
class StringUtility: 
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string
  '''This method prints out each string in the test string list
  
  returns self.string: unaltered test strings
  '''
  #Part B
  def vowels(self):
    vowels = set("aeiouAEIOU")
    count = 0
    for i in self.string:
      if i in vowels:
        count = count + 1
    if count > 4:
      count = "many"
    count = str(count)
    return count
  '''Counts the number of vowels in a string, and returns "many" if count > 4

  Returns count: the number of vowels in each string
  '''

  def bothEnds(self):
    return self.string[0] + self.string[1] + self.string[-2] + self.string[-1] if len(self.string) > 2 else ""
  '''
  Return a string made of the first 2 and last 2 chars of the original string if string > 2
  '''
  
  def fixStart(self):
    return self.string[0] + self.string[1: ].replace(self.string[0], "*") if len(self.string) > 0 else self.string
  '''Changes all occurences of a string's first character to "*" except the first character itself

  Returns altered string if length of string > 1, else returns self.string
  '''
  
  def asciiSum(self):
    sum = 0
    for string in self.string:
      for char in string:
        value = ord(char)
        sum += value 
    return sum
  '''Adds up the ascii values of each character in a string

  Returns sum of ascii values 
  '''

  def cipher(self):
    altstr = ""
    for string in self.string:
      length = int(len(self.string))
      for char in string:
        if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
          newchar = char
        else:
          asciival = int(ord(char))
          newval = asciival + length
          if 64 < asciival < 91:
            if newval > 90:
              newval = newval - 26
          elif newval > 122:
            newval = newval - 26
            if newval > 122:
              newval = newval - 26
          newchar = chr(newval)
        altstr = altstr + newchar
    return altstr
  '''Creates an encoded string by incrementing all letters by the length of the string

  Returns altstr: an originally empty string that becomes concatenated by the shifted letter based on self.string length
  '''
        
        
          
          
          
      
    
    