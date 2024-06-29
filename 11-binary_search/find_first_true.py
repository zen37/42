import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
logger = logging.getLogger(__name__)

class Solution:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def search(self, arr: List[bool]) -> int:
        left, right = 0, len(arr) - 1
        self.logger.debug(f"left, right: {left}, {right}")
        counter = 0
        first_true_index = -1
        while left <= right:
            counter += 1
            self.logger.debug(f"{counter} while ...")
            mid = (left + right) // 2
            self.logger.debug(f"mid, arr[mid]: {mid}, {arr[mid]}")
            if arr[mid]:
                first_true_index = mid
                self.logger.debug(f"first_true_index: {first_true_index}")
                right = mid - 1
                self.logger.debug(f"right decreased by 1: {right}")
            else:
                left = mid + 1
                self.logger.debug(f"left increased by 1: {left}")
        self.logger.debug("exit while")

        return first_true_index

def print_result(index: int):
    if index != -1:
        logger.info(f"First True found in position: {index}")
    else:
        logger.info("True not found")
    logger.info("____________________________________")

if __name__ == "__main__":
    s = Solution()
    index_first_true = s.search([False, False, True])
    print_result(index_first_true)
    index_first_true = s.search([False, False, False])
    print_result(index_first_true)
    index_first_true = s.search([True, True, True])
    print_result(index_first_true)
