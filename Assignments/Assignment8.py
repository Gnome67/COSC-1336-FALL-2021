"""
Talha Sohail
2092858
COSC 1336
Assignment 8
"""
import string

def encryptLetter(messageLetter,codeLetter):
  alphabet = list(string.ascii_uppercase)
  shift = alphabet.index(codeLetter)
  specialRow = alphabet[shift:] + alphabet[:shift]
  messageIndex = alphabet.index(messageLetter.upper())
  cypher = specialRow[messageIndex]
  if(messageLetter.isupper()):
    return cypher.upper()
  else:
    return cypher.lower()
  #return specialRow[messageIndex]

def encrypt(message,codeWord):
  index = 0
  x = ""
  codeWord = codeWord.upper()
  for letter in message:
    if(letter.isalpha()):
      encryptList = encryptLetter(letter,codeWord[index])
      index = (index + 1) % len(codeWord)
      x += encryptList
      if(index == len(codeWord)):
        index == 0
    else:
      x += letter
  return x

def decryptLetter(messageLetter,codeLetter):
  alphabet = list(string.ascii_uppercase)
  shift = alphabet.index(codeLetter)
  specialRow = alphabet[shift:] + alphabet[:shift]
  specialIndex = specialRow.index(messageLetter.upper())
  cypher = alphabet[specialIndex]
  if(messageLetter.isupper()):
    return cypher.upper()
  else:
    return cypher.lower()

def decrypt(message,codeWord):
  index = 0
  decryptIt = ""
  codeWord = codeWord.upper()
  for letter in message:
    if(letter.isalpha()):
      decryptList = decryptLetter(letter, codeWord[index])
      index = (index + 1) % len(codeWord)
      decryptIt += decryptList
    else:
      decryptIt += letter
  return decryptIt

def ask_choice():
  choice = input("E for Encrpyt, D for Decrypt: ")
  if(choice.upper()== "E"):
    message = input("Please enter a message you would like to encrypt: ")
    codeWord = input("Please enter a key for encryption: ")
    print(encrypt(message,codeWord))
  elif(choice.upper() == "D"):
    message = input("Please enter a message you would like to decrypt: ")
    codeWord = input("Please enter a key for decryption: ")
    print(decrypt(message,codeWord))

def askAgain():
  while True:
    again = input("Would you like to do another? (Y/N): ")
    if(again.upper() == "Y"):
      ask_choice()
    else:
      print("Goodbye!")
      break

plain_text = """The quick brown fox jumps over the lazy dog."""
example = "A test string, just for practice - here in Houston."
easy_secret = """S xgjx llvkek, cmwv wsk hvctxbui - jvvx ar Jfyllsp."""
bonusEncrypt = "bonus"
secret_message = """Xvnn’k is gbsu kvmzfg fi? Ez qbokjb Jykuablwmoax? Fp, al zsjf pimtwa:
Cx xs nlw noee’v uc qcw, xs nlw fbbq Lp rb ims qbofufl fgtg; nhv jt gi djjr,
Nzf trqws arh, lis tlwbhrl kioey gg vbhgvf. Tiv’t kvfd! J deuq uvry, ojgu hgu cay ebb zijf.
Pl Dgws, V ue ocg wgwsgimt tbl ypzq, Hgs qnlw J kui vphu zwfr hjgo al wgth;
Vn qfoehk ns ail jt zyf nm tujnsank xsnl; Kvqu imuknlv uvvhyt rjydm bbn ao al xwtweyk:
Cig cx jh oy s twa ng dciyl icaims, W ng lis ziku cszworvhy tchf smwiy.
Fp, tncli, al wga, kvmz ocg u ebb slgn Saadbbq: Age’g cysds! V qgvzq hgu zbmw tc tlwbh nh zpbboj
Bg bhw noa ggss, zyliwaek, xchfv tvnlw gfbg ef Tbl lis oyku vbjw J vnpw. P, rb hgu kvmz pbr ggss!
Eulise jjpqyuan wg, Qwthzijfznhv, uveimhv zs zpgg, Nzbh uy oiwpb zbhu hg thbgsdv gi liwf zahvg,
Fwu vvg vfdnll; iwf jstgciju guudm pr gses Nhv dfbqft tbl upbiiq qig cfuc uck qiemw:
Xs jimmr ail ewr cf uvnn ebb’f wgndnhq Uvnn xfoem zjg sydmcjmzjd gi vjs jcli if.
Nzjg quq jg pudmsq nzf truku cs Wjjgccso: Vr nzbh bolmwiyk uvvm vbm, nhv dczyk tosy zpar,
Qamz fnsor n naq-hby oisa nzf rns at bngwe, Oax jpify zja nn lis auef cs Wjjgccso.
Vr nzbh fbsmz ycnf huck eol, ufe gry gmr naw, Xwyf qfoefq pb gbw wwtcd gsnml iwf hwjuuvgvff,
Ufe gns ‘Lp-abljpk vm Kbwan Uswfjabb:’ Gbwo kvfd is fnjjd uck tzrynf oax kicj bat gpujt.
Oax kbm ‘Gbwts jimorf C zbr bh Uswfjao’g quq.’ Pzq gwo tblyfh: lyl bzy mzbzy vw gceagu,
Phn zf’zy lwnszvws kvnz briufuotyk Xvnn xfogm zf rvx liog xsz: huyf tvnfd pie hsnsf.
Zsnwycss wa bat aboli of bgvgrbgmr jijeg Uujsm gbw lwaa, Tfrsije oax Wysgyj,
Xoeqady nhv Uoyvgu, Gnfatphlq bbq Adpipykuse, Vw jb gbwjf sfgxwaa uvdf zjfgufq sszyecse’x.
Liwf mlpfl mzbzy nzf ubiv noa nwbqu bat gbh; Sor Platdvh Uswfjabb fbsmz ay’ws ub vq,
Gfbg liwf xsz hb nzf saxaou bz lis jijmr, Ool xs vh au guudm pr lwnszvws’r;
Jy xfk, jy zbdcs xfk, jy tbbq ix cfbnzfff; Zgs vr ng-eol nzbh fbweg uck czbiv xwgb ef
Guudm pr gq cfbnzff; oy zf br’yj tc icdf, Huck eol mzbzy awohyy zjg pifewgcgo:
Oax yfbgfwnsa cf Fbtfsor aio b-prx Kioyf liwae liszmwmjrm sdqhlkfr gbwz krlw ocg bwss,
Nhv icyx lisvl ebbuigeg pbwbd jbamsf ufz gcyslg Gbsu tboyih jcli if ohpb Fuaoh Platdvh’k eol."""

ask_choice()
askAgain()