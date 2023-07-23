import pythonmonkey as pm
"""
This code demonstrates loading a WebAssembly C library in  Python
using PythonMonkey.
"""

# get the WebAssembly module from JS
WebAssembly = pm.eval('WebAssembly')

# read the wasm file
file = open('lib.wasm', 'rb')
wasm_bytes = bytearray(file.read())

# instantiate a new wasm module
wasm_module = pm.new(WebAssembly.Module)(wasm_bytes)

# create an import object which specifies the wasm environment
import_object = {
    'env': {
        '__memory_base': 0,
        '__table_base': 0,
        'memory': pm.eval('new WebAssembly.Memory({ initial: 256, maximum: 256 })'),
        'table': pm.eval('new WebAssembly.Table({ initial: 0, maximum: 0, element: "anyfunc" })'),
        '__indirect_function_table': pm.eval('new WebAssembly.Table({ initial: 0, maximum: 0, element: "anyfunc" })'),
        '__stack_pointer': pm.eval('new WebAssembly.Global({ value: "i32", mutable: true }, 8192)'),
        'abort': lambda: exec('raise Exception("Abort!")') 
    }
}

# call the add function from the library
my_c_lib = pm.new(WebAssembly.Instance)(wasm_module, import_object).exports;
print(my_c_lib.add(1,2))

