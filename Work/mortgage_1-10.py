# mortgage.py
#
# Exercise 1.10 - my second version

principal = 500000.0
rate_yearly = 0.05
payment_monthly = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
month_count = 0


# payment for the rest of months
while principal > 0:
    month_count += 1
    principal = principal * (1 + rate_yearly / 12) - payment_monthly
    total_paid += payment_monthly

    if (
        month_count >= extra_payment_start_month
        and month_count <= extra_payment_end_month
    ):
        principal = principal - extra_payment
        total_paid += extra_payment

    print(month_count, round(total_paid, 2), round(principal, 2))


print("total_paid", total_paid, "month_count:", month_count)
