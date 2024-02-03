def calc_area_info(start, end, cycle) -> (int, int, int):
    left = start % cycle
    right = end % cycle
    full_cycles = (end - start) // cycle
    return left, right, full_cycles
