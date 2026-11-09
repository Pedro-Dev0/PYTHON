def bissexto(ano):
  if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto")
    ano = True
  else:
    print(f"O ano {ano} não é bissexto")
    ano = False
    
bissexto(1900)