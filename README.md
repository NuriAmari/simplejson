# simplejson
A clone of Python's [simplejson](https://pypi.org/project/simplejson/) package built to demonstrate and develop the language tools I've created [here](https://github.com/NuriAmari/Language-Tools). For those unfamiliar with simplejson, it is a python utility, now included with the language, used to encode and decode JSON data.

Currently the tool depends upon simplejson to dump objects once parsed and created, as I'm less interested in that task and it is unrelated to the language tools. However, I will likely remove all depedencies upon simplejson eventually. 

## Usage

Currently, the main loading and dumping methods from simplejson are supported in simplified form:

### load

Tokenizes and parses a JSON file from a stream implementing the `TextIOBase` interface. Returns an object representing the JSON data, just as simplejson does.

`json.load(input_stream: StringIO)`

### loads

Functions identically to load, but uses a string rather than a stream to retrieve data from.

`json.loads(input_str: str)`

### dump

Stringifies a JSON serializable object and writes the result to the provided stream. Currently uses simplejson.

`json.dump(json_object: Object, stream: TextIOBase)`

### dumps

Functions identically to dump, but returns the string directly rather than writing to a stream. Also depends on simplejson.

## Limitations

- Only ASCII characters are supported
- Escaped characters in strings are supported, but do no behave exactly like simplejson for the time being

