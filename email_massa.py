# coding: utf-8
#!usr/bin/python3

# modulo de importação
import smtplib
import os


print ("""
=================== O B S E R V A Ç Ã O ==========================

1 - Para o script funcionar, você precisar habilitar
nas configuraçoes da google Permitir que aplicativos menos
seguros acessem sua conta.

2 - Você devera esta no modo root.

3 - Para executar o script pelo terminal "python emailmassa.py .
==================================================================
                 """)

ente = input("Aperte [ENTER] para continuar:")
os.system('clear')



print ("""

  __ _                 _                                         _ _
 / _| | ___   ___   __| | __ _ _ __    ___       _ __ ___   __ _(_) |
| |_| |/ _ \ / _ \ / _` |/ _` | '__|  / _ \_____| '_ ` _ \ / _` | | |
|  _| | (_) | (_) | (_| | (_| | |    |  __/_____| | | | | | (_| | | |_
|_| |_|\___/ \___/ \__,_|\__,_|_|     \___|     |_| |_| |_|\__,_|_|_(_)


  +------------------------------------------------+
  | Desenvolvedor : Dalmo s. Cabral (Exumirim)     |
  | Data de Criação: 15/12/2016                    |
  | Facebook: https://www.facebook.com/exu.mirim.3 |
  |                                                |
  | Creditos: Guilherme Root Fernando              |
  | Youtube: Programação e Hacking                 |
  +------------------------------------------------+
                                                    """)

#serve do google
serve = smtplib.SMTP("smtp.gmail.com", 587)
serve.ehlo()
serve.starttls()




user = str(input("\nDigite seu email >> ")) #seu email.

senha = str(input("\nDigite a sua senha >> "))  #sua senha de email

to = str(input("\nDigite o email que você deseja envia >> "))  #email do pessoa que vai receber

numero = int(input("\nDigite a quantidade de email que deseja enviar >> ")) #numero de emails que você quer enviar.

msg = str(input("\nDigite a msg que deseja enviar >> "))  #a msg que vc quer enviar


try:
    serve.login(user, senha) #serve de login do google
    print ("\nVocê esta Logado !!!")

except:
    print ("Email ou senha invalidos ou você precisa dar permissão no seu email")

x = 0

while x <= numero:
    serve.sendmail(user, to, msg)
    x += 1
    print("\n[*] Enviando", x, "E-mail")

print ("\nFim do email em massa...")


