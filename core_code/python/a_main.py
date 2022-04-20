import numpy as np

from coregister_00 import coregister_wearables
from write_webpage import write_webpage


def main():
    """

    """

    # coregister datasets
    coregister_wearables()

    # write webpage
    write_webpage()




if __name__ == "__main__":
    main()
