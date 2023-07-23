# PythonMonkey Emscripten Example

This example will demonstrate using [Emscripten](https://emscripten.org/) to compile a C library to webassembly and loading it from Python using [PytyhonMonkey](https://pythonmonkey.io/).

PythonMonkey is a Python library for executing JavaScript and WebAssembly from Python. Check it out on GitHub: https://github.com/Distributive-Network/PythonMonkey

In this example the following C code will be executed from Python:
```c
#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
int add(int a, int b) {
	return a + b;
}
```

```python
print(my_c_lib.add(1,2)) # this outputs 3
```

## Installation

Install Emscripten https://emscripten.org/docs/getting_started/downloads.html

Install Python with a minimum version of 3.8.

Install PythonMonkey using pip: `$ pip install pythonmonkey`

## Build and Run

Compile the code using emcc
`$ emcc adder.c -s WASM=1 -s SIDE_MODULE=1 -o adder.wasm`

Run the python program:

`$ python3 main.py`

