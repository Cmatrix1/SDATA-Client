import asyncio
import time
from sdata import SDataClient


# Example usage
question = """
Python
"""

client = SDataClient()

# Measure runtime for get_data_playwright method
start_time_playwright = time.time()
playwright_result = asyncio.run(client.get_data_playwright(question))
print(playwright_result)
end_time_playwright = time.time()
elapsed_time_playwright = end_time_playwright - start_time_playwright
print("Playwright method runtime:", elapsed_time_playwright, "seconds")

# Measure runtime for get_data_requests method
start_time_requests = time.time()
requests_result = client.get_data_requests(question)
print(requests_result)
end_time_requests = time.time()
elapsed_time_requests = end_time_requests - start_time_requests
print("Requests method runtime:", elapsed_time_requests, "seconds")