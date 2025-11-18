"""
Task 2.3: Handle Errors in API Requests

Goal: Learn to handle common API errors including 404s, timeouts, and invalid JSON.

Exercises:
- Handle 404 errors
- Handle timeout errors
- Handle invalid JSON responses
"""

import httpx

# Exercise 3.1: Handle 404 errors
url = "https://jsonplaceholder.typicode.com/posts/9999"
# TODO: Send GET request and handle 404 error
try:
    response = httpx.get(url)
    if response.status_code == 404:
        print("Error 404: Resource not found")
    else:
        print("Request successful:")
        print(response.json())
except httpx.HTTPError as e:
    print(f"HTTP error occurred: {e}")


# Exercise 3.2: Handle timeout errors
# TODO: Send GET request with a very short timeout and catch timeout exception
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/posts", timeout=0.0001)
    print("Request completed with status code:", response.status_code)
except httpx.TimeoutException as e:
    print(f"Request timed out: {e}")
except httpx.HTTPError as e:
    print(f"HTTP error occurred: {e}")


# Exercise 3.3: Handle invalid JSON responses
url = "https://jsonplaceholder.typicode.com/posts"
# TODO: Try parsing JSON and handle invalid JSON errors
try:
    response = httpx.get(url)
    data = response.json()
    print("JSON parsed successfully. Number of posts:", len(data))
except ValueError as e:
    print(f"Invalid JSON received: {e}")
except httpx.HTTPError as e:
    print(f"HTTP error occurred: {e}")
