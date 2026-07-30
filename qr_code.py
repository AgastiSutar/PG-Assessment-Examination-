import qrcode


# Enter your Flask address
address = input("Enter the Examination Address : ")


# Create QR Code
image = qrcode.make(address)


# Save the QR Code
image.save("PG Assessment QR Code.png")


print("\nQR Code Generated Successfully.")
print("File Name : PG Assessment QR Code.png")
