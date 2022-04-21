def main():
    software = 990000
    banyakbeli = int(input("Masukkan banyak pembelian: "))
    if (banyakbeli >= 10 and banyakbeli <= 19):
        discount = 20/100 * software *banyakbeli
        total = software*banyakbeli - discount
        print(f"Diskon = Rp.{discount:,.2f}")
        print(f"Total = Rp.{total:,.2f}")
    elif(banyakbeli >= 20 and banyakbeli <= 49):
        discount = 30/100*software*banyakbeli
        total = software*banyakbeli - discount 
        print(f"Diskon = Rp.{discount:,.2f}")
        print(f"Total = Rp.{total:,.2f}")   
    elif(banyakbeli >=50 and banyakbeli <= 99):
        discount = 40/100*software*banyakbeli
        total = software*banyakbeli - discount
        print(f"Diskon = Rp.{discount:,.2f}")
        print(f"Total = Rp.{total:,.2f}")
    elif(banyakbeli >=100):
        discount = 50/100*software*banyakbeli
        total = software*banyakbeli - discount
        print(f"Diskon = Rp.{discount:,.2f}")
        print(f"Total = Rp.{total:,.2f}")
    else:
        total = software*banyakbeli
        print(f"Total = Rp.{total:,.2f}")

main()
