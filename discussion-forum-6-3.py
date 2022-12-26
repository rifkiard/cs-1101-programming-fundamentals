def add_quantity(items, target, qty):
    if(target not in items):
        print( "Item not found")
        return
    
    original_item = items.copy()

    items[items.index(target)] = items[items.index(target)] + " (" + str(qty) + ")"

    print("Your items:")
    print(original_item)
    print("After quantity added:")
    print(items)


add_quantity(["Bottle", "Pencil", "Eraser"], "Pen", 3)
# Output:
# Item not found

add_quantity(["Bottle", "Pencil", "Eraser"], "Pencil", 3)
# Output:
# Your items:
# ['Bottle', 'Pencil', 'Eraser']
# After quantity added:
# ['Bottle', 'Pencil (3)', 'Eraser']