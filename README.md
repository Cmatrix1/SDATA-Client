# SDataClient

SDataClient is a Python library that allows you to retrieve data from the SData website using either the Playwright or Requests library. It provides two methods, `get_data_playwright` and `get_data_requests`, for fetching data based on a given question.

## Installation

To use SDataClient, you need to have Python 3.x installed on your system. You can install the library by following these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/SDataClient.git
   ```

2. Navigate to the project directory:

   ```shell
   cd SDataClient
   ```

3. Install the required dependencies:

   ```shell
   pip install playwright requests bs4
   ```

## Usage

Here's an example of how to use SDataClient in your Python code:

```python
from sdata import SDataClient

# Initialize the SDataClient instance
client = SDataClient()

# Provide a question to get the data
question = "Python"

# Get data using the Playwright method
playwright_result = client.get_data_playwright(question)
print(playwright_result)

# Get data using the Requests method
requests_result = client.get_data_requests(question)
print(requests_result)
```

## Performance

SDataClient offers two methods for retrieving data: `get_data_playwright` and `get_data_requests`. You can measure the runtime of each method using the following code:

```python
import time
import asyncio

# ...

question = "Python"
client = SDataClient()

# Measure runtime for get_data_playwright method
start_time_playwright = time.time()
playwright_result = asyncio.run(client.get_data_playwright(question))
end_time_playwright = time.time()
elapsed_time_playwright = end_time_playwright - start_time_playwright
print("Playwright method runtime:", elapsed_time_playwright, "seconds")

# Measure runtime for get_data_requests method
start_time_requests = time.time()
requests_result = client.get_data_requests(question)
end_time_requests = time.time()
elapsed_time_requests = end_time_requests - start_time_requests
print("Requests method runtime:", elapsed_time_requests, "seconds")
```

## Contributing

If you want to contribute to SDataClient, feel free to fork the repository and submit pull requests. Contributions such as bug fixes, new features, and improvements are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

The SDataClient library was created by [Your Name]. It makes use of the following open-source libraries:

- [Playwright](https://github.com/microsoft/playwright)
- [Requests](https://github.com/psf/requests)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
