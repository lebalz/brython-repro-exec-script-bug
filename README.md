# Bug Reproduction

## Run the code

A little reproduction of the bug - no dependecies, no styling, just the code.

Run it with:
```bash
python app.py
```

The Code is executed with

```js
code = `from python_runner import from_lib
print("Hello from", from_lib())`;
window.__BRYTHON__.runPythonSource(
    code, 
    {
        pythonpath: ["/bry-libs/"],
    }
);
```

The lib import crashes when the code is executed from the root domain (http://localhost:3000), but works when executed from a subdomain (http://localhost:3000/demo).

<video>
    <source src="./bug-repro.mp4" type="video/mp4">
</video>