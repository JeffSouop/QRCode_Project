import qrcode
from PIL import Image

Logo_added=(int(input("Voulez-vous ajouter un logo à 0votre QRcode ? :\n 0 = non ; 1 = oui\n")))

if Logo_added>0:
 Logo_link =(input("notez le chemin du fichier image\nPar exemple : /home/alban/gererate_qr-code/tux.jpeg\n"))
 logo = Image.open(Logo_link)

 basewidth = 100

 wpercent = (basewidth/float(logo.size[0]))
 hsize = int((float(logo.size[1])*float(wpercent)))
 logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
 QRcode = qrcode.QRCode(
 error_correction=qrcode.constants.ERROR_CORRECT_H
 )

 url=(input("Tapez l'adresse complète avec https:// ou le texte voulu :\n"))

 QRcode.add_data(url)

 QRcode.make()

 QRcolor=(input("Quelle couleur voulez-vous ?\norange, black, white, ... ???\n"))

 QRimg = QRcode.make_image(
 fill_color=QRcolor, back_color="White").convert('RGB')

 pos = ((QRimg.size[0] - logo.size[0]) // 2,
 (QRimg.size[1] - logo.size[1]) // 2)
 QRimg.paste(logo, pos)

 name_wanted=(input("Tapez le nom voulu (sans extention) pour le fichier PNG du QR-code :\n"))
 name_out=name_wanted+'.png'
 QRimg.save(name_out)

 print('QR code generated!')

else:
 print("OK, pas de logo\n")

# adjust image size
QRcode = qrcode.QRCode(
error_correction=qrcode.constants.ERROR_CORRECT_H
)

url=(input("Tapez l'adresse complète avec https:// ou le texte voulu :\n"))

QRcode.add_data(url)

QRcode.make()

QRcolor=(input("Quelles couleur voulez-vous ?\nOrange, Black, White, ... ???\n"))

QRimg = QRcode.make_image(
fill_color=QRcolor, back_color="White").convert('RGB')

name_wanted=(input("Tapez le nom voulu (sans extention) pour le fichier PNG du QR-code :\n"))
name_out=name_wanted+'.png'
QRimg.save(name_out)

print('QR code generated!')