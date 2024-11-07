
# Nama : Radjikin Septiawan
# NIM : 312410071
# TIF 24 A1 


# Data barang
inventory = [
    {"id": 1, "name": "Beras", "price": 12000},
    {"id": 2, "name": "Minyak Goreng", "price": 15000},
    {"id": 3, "name": "Gula Pasir", "price": 10000},
    {"id": 4, "name": "Mie Instan", "price": 3000},
    {"id": 5, "name": "Susu Cair", "price": 8000}
]

print(f'''
{inventory[0]["id"]}. {inventory[0]["name"]} : {inventory[0]["price"]}
{inventory[1]["id"]}. {inventory[1]["name"]} : {inventory[1]["price"]}
{inventory[2]["id"]}. {inventory[2]["name"]} : {inventory[2]["price"]}
{inventory[3]["id"]}. {inventory[3]["name"]} : {inventory[3]["price"]}
{inventory[4]["id"]}. {inventory[4]["name"]} : {inventory[4]["price"]}
      ''')
# Menambahkan barang ke keranjang
cart = []
while cart.__len__() < 99:
    userInput = input("Masukkan Id Barang: ")
    if userInput == "1":
        cart.append(inventory[0])
    elif userInput == "2":
      cart.append(inventory[1])
    elif userInput == "3":
      cart.append(inventory[2])
    elif userInput == "4":
      cart.append(inventory[3])
    elif userInput == "5": 
       cart.append(inventory[4])
    elif userInput.lower() == "selesai":
        break
# Menampilkan daftar barang
question = input("Ingin menampilkan list belanjaan? : (yes/no)")
if question.lower() == "yes":
    for item in cart: 
        print(item)
elif question.lower() == "no":
        print("Terimakasih")
# Menghitung total harga

totalHarga = input("Total Harga ?(yes/no)")
if totalHarga.lower() == "yes":
    total = sum(item["price"] for item in cart)
    print(f'total harga : {total}')
        
# Mencetak Struk
with open("strukBelanjaan.txt","w") as createDirectory:
    for item in cart:
        createDirectory.write(f"{item["name"]} : {item["price"]} \n")
    total = sum(item["price"] for item in cart)
    createDirectory.write(f"\nTotal Harga: Rp{total}\n")