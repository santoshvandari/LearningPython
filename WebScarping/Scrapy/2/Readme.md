# 

Please Follow the mentioned thigs to used it. 
- Create the Virtual Environment(It is not Necessary but Recommended)
    ```bash 
    python -m virtualenv virtual
    # For Linux : python3 -m virtualenv virtual
    ```
- Install the scrapy and scrapy-playwright
    ```bash
    pip install scrapy 
    pip install scrapy-playwright
    playwright install
    ```
- Visit the Folder Directory and Start Scraping
    ```bash
    cd Test/Test
    scrapy crawl example
    ```

This code scrap the Nepase Share data(only script name and last tranction price) and store in the `nepsedata.txt` file. 
