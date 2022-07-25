
import pyperclip

message="You can show black is white by argument,said Filby,but you will never convince me."

key=8
mode = 'encrypt'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = '' 
for symbols in message:
	if symbols in SYMBOLS:
           symbolIndex=SYMBOLS.find(symbols)
           if mode =='encrypt':    
             translatedIndex = symbolIndex + key
           elif mode == 'decrypt':
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
