from payment_method import PaymentMethod

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        fee = 0.03
        final_amount = amount * (1 + fee)
        print(f"\n=== Pembayaran Kartu Kredit ===")
        print(f"Total: Rp{amount:,.0f}")
        print(f"Biaya tambahan 3%: +Rp{amount * fee:,.0f}")
        print(f"Total dibayar: Rp{final_amount:,.0f}")
