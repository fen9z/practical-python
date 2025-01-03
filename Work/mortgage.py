# mortgage.py
#
# Exercise 1.10 - my first version

principal = 500000.0
rate_yearly = 0.05
payment_monthly = 2684.11
total_paid = 0.0
# extra payment from start month to end month
month_count = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
payment_extra_times = extra_payment_end_month - extra_payment_start_month + 1


# payment for the rest of months
while principal > 0:
    while payment_extra_times > 0 and (
        extra_payment_start_month <= month_count <= extra_payment_end_month
    ):
        principal = principal * (1 + rate_yearly / 12) - payment_monthly - extra_payment
        payment_extra_times -= 1
        month_count += 1
        total_paid += payment_monthly + extra_payment
        print(month_count, total_paid, principal)

    principal = principal * (1 + rate_yearly / 12) - payment_monthly
    total_paid += payment_monthly
    month_count += 1
    print(month_count, total_paid, principal)

print("total_paid", total_paid, "month_count:", month_count)
