import requests
from datetime import datetime
import uuid

# function to download the book cover image and save it to the media folder
def download_book_cover(url):
    # replace zoom=1 in the url with zoom=3
    url = url.replace('zoom=1', 'zoom=3')
    response = requests.get(url)
    if response.status_code == 200:
        # get the image name from the url
        # image_name = url.split('/')[-1]

        uuid_name = uuid.uuid4()
        image_name = f"{uuid_name}.jpg"

        # save the image to the media folder
        with open('media/book_covers/' + image_name, 'wb') as f:
            f.write(response.content)
        return f"book_covers/{image_name}"
    else:
        return None

# function to search for books in the Google Books API
def search_books(query, max_results=10):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "maxResults": max_results
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    books = []
    for item in data.get("items", []):
        volume_info = item.get("volumeInfo", {})
        
        # Extraer la información necesaria
        title = volume_info.get("title", "")
        authors = volume_info.get("authors", [""])
        isbn = volume_info.get("industryIdentifiers", [{}])[0].get("identifier", "")
        published_date = volume_info.get("publishedDate", "")
        thumbnail = volume_info.get("imageLinks", {}).get("thumbnail", "")
        
        # Convertir la fecha de publicación a un objeto datetime
        try:
            published_date = datetime.strptime(published_date, "%Y-%m-%d").date()
        except ValueError:
            try:
                published_date = datetime.strptime(published_date, "%Y").date()
            except ValueError:
                published_date = None

        # if missing isbn continue
        if not isbn:
            print(f"El libro {title} no tiene ISBN")
            continue

        books.append({
            "title": title,
            "author": ", ".join(authors),
            "isbn": isbn,
            "published_date": published_date,
            "cover_image_url": thumbnail
        })

    print(books)
    return books
