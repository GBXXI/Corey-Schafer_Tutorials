
import django
django.setup()

from django.core.paginator import Paginator

posts = ['1', '2', '3', '4', '5']
p = Paginator(posts, 2)

print(p.num_pages)

for page in p.page_range:
    print(page)

p1 = p.page(1)
print(p1)
print(p1.number)
print(p1.object_list)
print(p1.has_previous())
print(p1.has_next())
print(p1.next_page_number())
