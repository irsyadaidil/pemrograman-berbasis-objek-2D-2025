from payment_method import PaymentMethod

class EWalletPayment(PaymentMethod):
    def pay(self, amount):
        cashback = 0.02
        print(f"\n=== Pembayaran Dompet Digital ===")
        print(f"Total: Rp{amount:,.0f}")
        print(f"Cashback 2%: Rp{amount * cashback:,.0f} akan dikembalikan setelah pembayaran.")
        print(f"Total dibayar: Rp{amount:,.0f}")
