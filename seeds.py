from src.models import Authors, Quotes
import json


with open('authors.json') as f:
    authors_data = json.load(f)

with open('quotes.json') as f:
    quotes_data = json.load(f)


for author_data in authors_data:
    author = Authors(**author_data)
    author.save()

for quote_data in quotes_data:
    author_name = quote_data.get('author')
    author = Authors.objects.get(fullname=author_name) if author_name else None
    quote = Quotes(author=author, quote=quote_data['quote'], tags=quote_data.get('tags'))
    quote.save()
