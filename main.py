import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient
from interface.root_component import Root

# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("8d0922c254c066f9325a2dc6acdb82ccbd1c108cdcd0d1fa9e2a193deef06892",
                            "a86579e0a1ef79d25380986ba179edb44f821bf3165fd99b0dcaff5deb963e55",
                            testnet=True, futures=True)

    bitmex = BitmexClient("q4m3msIRvLyN3PcO7SqCMSf4", "giwHvf3Qg_o7aQ7U8Bkue_Fv2BOb6mFqkyq0CXihyX9v5-pJ", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
