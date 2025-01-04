# mortgage.py
#
# Exercise 1.10 - my second version
# Exercise 1.11 - my third version fix the program to correct for the overpayment that occurs in the last month.

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

    total_paid += payment_monthly
    principal = principal * (1 + rate_yearly / 12) - payment_monthly

    if (
        month_count >= extra_payment_start_month
        and month_count <= extra_payment_end_month
    ):
        total_paid += extra_payment
        principal = principal - extra_payment

    # print(month_count, round(total_paid, 2), round(principal, 2))
    print(f"{month_count:>4d}, {round(total_paid, 2):>10f}, {round(principal, 2):>10f}")

    # if the last year principal < payment_monthly
    if principal * (1 + rate_yearly / 12) < payment_monthly:
        month_count += 1
        total_paid += principal * (1 + rate_yearly / 12)
        principal = 0
        print(
            f"{month_count:>4d}, {round(total_paid, 2):>10f}, {round(principal, 2):>10f}"
        )


print("total_paid", total_paid, "month_count:", month_count)
