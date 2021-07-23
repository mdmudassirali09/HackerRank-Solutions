from collections import Counter
def stringAnagram(dictionary, query):
    d = ["".join(sorted(word)) for word in dictionary]
    q = ["".join(sorted(word)) for word in query]
    count = Counter(d)
    for w in q:
        if w in count.keys():
            print(count[w])
        else:
            print(0)
            
if __name__ == "__main__":
    dictionary_count=int(input())
    dictionary=[]
    for i in range(dictionary_count):
        dictionary.append(input())
    query_count=int(input())
    query=[]
    for i in range(query_count):
        query.append(input())
    stringAnagram(dictionary, query)
