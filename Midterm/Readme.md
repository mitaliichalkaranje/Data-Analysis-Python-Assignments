
## You need a read me file

Feedbacks :
---
* Had to submit .py file. 
* Do not store the data in a single file.

> Fetch Data file seems to be incorrect. 


```python
for k in range(1,100):
    results = requests.get(url="https://api.stackexchange.com/2.2/questions?tagged=python;pandas&page=1&pagesize=100&site=stackoverflow&key=Qbw)9y9ZFui61wxBzFU7mQ((") 
    raw_data=results.json()
    d={}
    for data in raw_data['items']:
        d=data     # Why do you need this ?
    sleep(0.5)     # Not saving the data ?
```
