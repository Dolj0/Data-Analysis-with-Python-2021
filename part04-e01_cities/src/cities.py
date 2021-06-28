#!/usr/bin/env python3

import numpy as np
import pandas as pd

def cities():
    c = np.array([[643272, 715.48],[279044, 528.03],[231853, 689.59], [223027, 240.35],[201810, 3817.52]])
    df = pd.DataFrame(c, columns = ["Population", "Total area"], index=["Helsinki","Espoo","Tampere","Vantaa","Oulu"])
    return df
    
def main():
    print(cities())
    return
    
if __name__ == "__main__":
    main()
