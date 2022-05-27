# aiobcrypt

Aiobcrypt is a Python library for offloading bcrypt operations to a 
`ThreadPool`, making them non-blocking in asynchronous projects like 
[FastAPI](https://fastapi.tiangolo.com/).

As bcrypt is slow by design this prevents, in the case of FastAPI, request from
stalling until bcrypt is done. This is managed by wrapping all bcrypt methods
in an async wrapper and letting them run in a ThreadPool.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install aiobcrypt.

```bash
pip install aiobcrypt
```

## Usage

```python
import aiobcrypt

password = b'hello async world'

async def hash_and_verify():
    # Generate salt
    salt = await aiobcrypt.gensalt()

    # Generate hashed password
    hashed_password = await aiobcrypt.hashpw(password, salt)

    # Validate hashed password
    valid_password = await aiobcrypt.checkpw(password, hashed_password)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to 
discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This is licensed the same way as [bcrypt](https://pypi.org/project/bcrypt/)
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)