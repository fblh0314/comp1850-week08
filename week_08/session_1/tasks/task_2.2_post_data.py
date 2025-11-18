"""
Task 2.2: Send Data Using POST Requests

Goal: Learn to send data to an API using POST requests.

Exercises:
- Create a new post
- Add a new comment to a post
- Create a new user
"""

import httpx

# Exercise 2.1: Create a new post
url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "UserID": 11,
    "id": 101,
    "title": "quot quot menses",
    "body": "pueri aleynienses"
}
response = httpx.post(url, json = new_post)
print("New post created: ")
print(response.json())
print()
# TODO: Define new post data and send POST request


# Exercise 2.2: Add a new comment to a post
url = "https://jsonplaceholder.typicode.com/comments"
new_comment = {
    "postID": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "Heres a new comment"
}
response = httpx.post(url, json = new_comment)
print("New comment: ")
print(response.json())
print()
# TODO: Define new comment data and send POST request


# Exercise 2.3: Create a new user
url = "https://jsonplaceholder.typicode.com/users"

new_user = {
    "id": 11,
    "name": "bob marley",
    "username": "big.smoker",
    "address": {
        "street": "Woodwarde",
        "suite": "suite 97",
        "city": "London",
        "zipcode": "9998",
        "geo": {
            "lat": "-78.6895",
            "lng": "87.3672"
        }
    },
    "phone": "07-562-789-981",
    "website": "marley.com",
    "company": {
        "name": "marley LTD",
        "catchPhrase": "real smokaz",
        "bs": "make money moves"
    }
}

response = httpx.post(url, json = new_user)
print("New user added: ")
print(response.json())
print()

# TODO: Define new user data and send POST request
