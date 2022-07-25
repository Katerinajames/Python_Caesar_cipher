
import pyperclip

message="gw3EkivE1pw5EjtiksEq1E5pq2mEj7Eizo3umv2,1iqlENqtj7,j32E7w3E5qttEvm4mzEkwv4qvkmEumH"

key=8
mode = 'encrypt'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = '' 
for symbols in message:
	if symbols in SYMBOLS:
           symbolIndex=SYMBOLS.find(symbols)
           if mode =='decrypt':    
             translatedIndex = symbolIndex + key
           elif mode == 'encrypt':
             translatedIndex = symbolIndex - key 
           if translatedIndex >= len(SYMBOLS):
             translatedIndex = translatedIndex-len(SYMBOLS)   
           elif translatedIndex < 0:
             translatedIndex = translatedIndex + len(SYMBOLS) 
           translated = translated + SYMBOLS[translatedIndex]
	else:
		translated = translated + symbols	               			    
print(translated)
pyperclip.copy(translated)        
