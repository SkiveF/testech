def saut_ligne(text):
    resultat = ""
    
    for caractere in text:
        resultat += caractere
        if caractere == ' ':
            resultat += '\n'
    
    return resultat


if __name__ == '__main__':
    text = "hello world !"
    resultat = saut_ligne(text)
    print(resultat)
