word = input("Enter a word")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newtext = ''
key = int(input("Enter a key between 1 and 26"))


cryptdecrypt = input('Are you encrypting or decrypting? Type encrypt for encryption and decrypt for decryption')

if cryptdecrypt == 'encrypt':
  
  for i in range(len(word)):
    whereisletter = alphabet.find(word[i])
    newletter = alphabet[(whereisletter+key)%26]
    newtext = newtext+newletter
    
  print newtext

elif cryptdecrypt == 'decrypt':
  for i in range(len(word)):
    whereisletter = alphabet.find(word[i])

    newletter = alphabet[(whereisletter-key)%26]
    newtext = newtext+newletter
  print newtext
