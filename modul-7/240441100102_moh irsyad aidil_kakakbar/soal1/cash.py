from payment_method import PaymentMethod

class CashPayment(PaymentMethod):
    def pay(self, amount):
        discount = 0.05
        final_amount = amount * (1 - discount)
        print(f"\n=== Pembayaran Tunai ===")
        print(f"Total sebelum diskon: Rp{amount:,.0f}")
        print(f"Diskon 5%: -Rp{amount * discount:,.0f}")
        print(f"Total dibayar: Rp{final_amount:,.0f}")
