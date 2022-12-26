items = ['Book', 'Desk', 'Laptop', 'Keyboard', 'Mouse']
work_items = items # An alias

print(work_items is items)
# Output:
# True

print(id(work_items))
# Output:
# 4335055424
print(id(items))
# Output:
# 4335055424

# (Both variable have the same reference)

items = ["Bottle", "Pencil", "Eraser"]
print(work_items is items)
# Output:
# False

print(id(items))
# Output:
# 4335627264
# (items id has been changed, the past aliases will no longer identical and will no longer as a reference.)

work_items = items # An alias


print(work_items is items)
# Output:
# True

print(id(work_items))
# Output:
# 4335627264
# (work_items will be identical again because we are re-aliasing it.)


work_items[1] = "Ruler"

print(items)
# Output:
# ['Bottle', 'Ruler', 'Eraser']
# When we change the references or the object itself, the other references or the object itself will be changed too.
