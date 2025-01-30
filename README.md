# Modular Architecture for informatics in Python - v1

## Overview

This project experiments with modular architectures for (bio)informatics using Python and FastAPI. It aims to facilitate the development, testing, and deployment of informatics API tools by providing a structured and reusable codebase. This is the first iteration. 

## Features

- **Modular Design**: Easily extend and maintain your informatics tools.
- **Reusable Components**: Common informatics functionalities are encapsulated in reusable modules.
- **Scalability**: Designed to handle large datasets and complex computations.
- **Documentation**: Comprehensive documentation for each module and functionality.

## Installation

This project was created using `uv`. To install the dependencies using pip, run:

```bash
pip install -r requirements.txt
```

## Directory Structure

```
.
├── README.md
├── __init__.py
├── app
│   ├── __init__.py
│   ├── main.py
│   └── tests
│       ├── __init__.py
│       └── test_data.json
├── controllers
│   ├── __init__.py
│   └── informatic_controller.py
├── pyproject.toml
├── repositories
│   ├── __init__.py
│   └── informatic_repository.py
├── requirements.txt
├── routers
│   ├── __init__.py
│   └── informatic_router.py
├── services
│   ├── __init__.py
│   └── informatic_service.py
└── uv.lock
```

## Dependencies

```
```
modular-arch-python v0.1.0
├── fastapi v0.115.7
│   ├── pydantic v2.10.6
│   │   ├── annotated-types v0.7.0
│   │   ├── pydantic-core v2.27.2
│   │   │   └── typing-extensions v4.12.2
│   │   └── typing-extensions v4.12.2
│   ├── starlette v0.45.3
│   │   └── anyio v4.8.0
│   │       ├── idna v3.10
│   │       ├── sniffio v1.3.1
│   │       └── typing-extensions v4.12.2
│   └── typing-extensions v4.12.2
└── uvicorn v0.34.0
    ├── click v8.1.8
    └── h11 v0.14.0

```
```
## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainer.
