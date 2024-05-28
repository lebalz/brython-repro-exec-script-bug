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



https://github.com/lebalz/brython-repro-exec-script-bug/assets/22354689/aaf9b3d0-53cb-4388-969b-1543bb52e177

