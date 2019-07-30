


# packages

* build-essential

# Languages

## Python3
### Compile
```
python3 -c "import py_compile; py_compile.compile(r'Main.py')"
```

### Run
```
python3 Main.py
```

## C++
### Compile
```
g++ Main.cc -o Main -O2 -Wall -lm -static -std=gnu++17
g++ Main.cc -o Main -O2 -Wall -lm -static -std=gnu++14
g++ Main.cc -o Main -O2 -Wall -lm -static -std=gnu++11
g++ Main.cc -o Main -O2 -Wall -lm -static -std=gnu++98
```
### Run
```
./Main
```

## PHP
### Compile
```
php -l main.php
```
### Run
```
php```