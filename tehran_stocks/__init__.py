import os

import tehran_stocks.config as db
from tehran_stocks.download import (
    get_all_price,
    get_stock_detail,
    get_stock_groups,
    get_stock_ids,
    update_group,
    update_stock_price,
)
from tehran_stocks.models import StockPrice, Stocks

from .initializer import init_db, fill_db

if not os.path.isfile(db.db_path):
    print("No database founded.")
    init_db()
    fill_db()
