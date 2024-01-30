import matplotlib.pyplot as plt
import qrcode

# Créez une instance de QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Ajoutez des données au QR code
data = "https://www.youtube.com/channel/UCX4NBMYIcwcxX3NpXBHkTMw"
qr.add_data(data)
qr.make(fit=True)

# Créez une image du QR code
img = qr.make_image(fill_color="black", back_color="white")

# Sauvegardez l'image du QR code
img.save("Harsh.png")

# Affichez le QR code avec matplotlib
plt.imshow(img, cmap="gray")
plt.show()
