# attendysis
A library to analyse time_log data generated from biometric attendance devices.

Start by importing the LoadCsv class 
```python
from Attendysis import Attendysis

def main():
    data=Attendysis(filename)
    data.head()
    data.tail()
    print(data.length)
    print(data.features())
    data.columns(list of specific column titles whose rows you want displayed)

if __name__ == '__main__':
    main()

```
see the use in test.py
