# stolpop
Short Takeoff and Landing Plane Optimization

## Ideas for layout
So optimizer needs gradient ->


## Directory Layout

```
├── models/
│   ├── avl.exe
│   └── xfoil.exe
├── src/
│   └── stolpop/
│       ├── methods/
│       └── utilities/
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

- **methods/**: Specific functions that will likely be used once in the overall process. One method should not include another (or at least try to). Each function should be its own `.py` file.
- **utilities/**: General functions that are used within methods. Each function should be its own `.py` file.
- **scripts/**: Any one-time run/executable scripts.
- **tests/**: Test scripts to test functions or algorithms. Can be unit tests or whole optimizations.
- **models/**: Any external model or executable, e.g. XFOIL Alex -Testing push.