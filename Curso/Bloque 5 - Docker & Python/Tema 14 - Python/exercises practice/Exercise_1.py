""" Suppose you are the owner of an online store and you have a list of sales from the last 30 days. You want to analyze the sales by day of the week to identify the days with the highest sales.

tips:
- make a new list with 7 free spots for each day to add the sales with a loop.
- use a variable to keep count of the week day and reset to 0 when it gets to 7.
- use enumerate for the print to terminal. """

sales = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
         140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]

days_of_week = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

days = [0, 0, 0, 0, 0, 0, 0]
count = 0

for sale in sales:
    days[count] += sale
    count += 1
    if count == 7:
        count = 0

for i, day in enumerate(days_of_week):
    print(f"{day}: {days[i]}")

# enumerate(dias_semana) gives you both the index (i) and the day name in each iteration.
# use i to access the corresponding value in days without needing to manually increment or reset a counter.
