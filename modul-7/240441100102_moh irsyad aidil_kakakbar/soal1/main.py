from cash import CashPayment
from credit_card import CreditCardPayment
from e_wallet import EWalletPayment

def main():
    print("=== Sistem Pembayaran ===")
    try:
        amount = float(input("Masukkan total belanja (Rp): "))
    except ValueError:
        print("Input tidak valid. Harus berupa angka.")
        return

    print("\nPilih metode pembayaran:")
    print("1. Tunai")
    print("2. Kartu Kredit")
    print("3. Dompet Digital")
    
    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == "1":
        method = CashPayment()
    elif choice == "2":
        method = CreditCardPayment()
    elif choice == "3":
        method = EWalletPayment()
    else:
        print("Pilihan tidak valid.")
        return

    method.pay(amount)

if __name__ == "__main__":
    main()
