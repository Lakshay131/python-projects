from googlesearch import search


print("welcome to the browser!")
print("(search_______________)")

query = input("entre your query here---")

print("searching.......")


try:
    for result in search(query, num_results=5, lang="en"):
        print(result)
except Exception as e:
    print(f"Error: {e}")