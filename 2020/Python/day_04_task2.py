"""Advent of Code Day 4"""
from day_04_task1 import Passport, parse_passport
from utils import get_data, avg_timer

raw_data = get_data("passports")

def validate_passport(passport_obj: Passport) -> bool:
    byr, iyr, eyr = map(int, [passport_obj.byr, passport_obj.iyr, passport_obj.eyr])
    if not all([(byr >= 1920 and byr <= 2002), (iyr >= 2010 and iyr <= 2020), (eyr >= 2020 and eyr <= 2030)]):
        return False
    
    if passport_obj.hgt.endswith("cm"):
        num = int(passport_obj.hgt[:-2])
        if not (num >= 150 and num <= 193):
            return False
    elif passport_obj.hgt.endswith("in"):
        num = int(passport_obj.hgt[:-2])
        if not (num >= 59 and num <= 76):
            return False
    else:
        return False
    
    if passport_obj.hcl.startswith("#"):
        for i in passport_obj.hcl[1:]:
            try:
                i = int(i)
                if i not in range(0, 10):
                    return False
            except ValueError:
                if i not in "abcdef":
                    return False
    else:
        return False
    
    if passport_obj.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: 
        return False

    if not (passport_obj.pid.isnumeric() and len(passport_obj.pid) == 9):
        return False

    return True

@avg_timer()
def main() -> None:
    count = 0
    for raw_string in raw_data:
        try:
            obj = Passport(**parse_passport(raw_string))
            if validate_passport(obj):
                count += 1
        except TypeError:
            continue
    print(count)
