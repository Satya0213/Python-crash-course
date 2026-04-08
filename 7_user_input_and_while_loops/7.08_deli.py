sandwich_orders = ['tuna', 'chicken', 'egg salad', 'BLT', 'club']
finished_orders = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"Making your order: {current_order} sandwich.")
    finished_orders.append(current_order)

print("\nYour order is complete:\n")
for finished_order in finished_orders:
    print(finished_order.title())