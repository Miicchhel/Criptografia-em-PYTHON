# -*- coding: utf-8 -*-
class Cesar:
   
   def __init__(self):
    self.letras='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
   '''Metodo que criptografa:
   chamando o metodo 'crip' e passando os atributos Texto_normal e chave, quando a chave nao for passada
   sera igual a 3, por default.'''
   def crip(self,texto_normal,chave=3):
      texto_cifrado= ' '
      texto_normal=texto_normal.upper()
      #Analisando se cada 'i' em 'texto_normal' está em self.letras. Se sim, pegamos a 'posição+chave' e add na string vazia texto_cifrado       
      for i in texto_normal:
         if i in self.letras:
            pos=self.letras.find(i)+chave                
            if pos >= 26:
               pos -= 26
            texto_cifrado += self.letras[pos]      
      return texto_cifrado

   #Metodo que descriptografa 
   def decrip(self, texto_cifrado, chave=-3):
      texto_normal=' '
      texto_cifrado=texto_cifrado.upper()
      
      for i in texto_cifrado:
         if i in self.letras:
            pos=self.letras.find(i)+chave
            texto_normal += self.letras[pos]
      return texto_normal


  
      
