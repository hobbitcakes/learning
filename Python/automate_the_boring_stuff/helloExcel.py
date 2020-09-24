import numpy as np
import pandas as pd
import logging

def main():
    pd.ExcelWriter('./HelloExcel.xlsx')
    logging.info("Hello, Excel!")
    pass

if __name__ == '__main__':
    main()