from extensions import jalali
from django.utils import timezone

def persian_numbers_converter(string):
	numbers = {
	"0":"۰",
	"1":"۱",
	"2":"۲",
	"3":"۳",
	"4":"۴",
	"5":"۵",
	"6":"۶",
	"7":"۷",
	"8":"۸",
	"9":"۹",
	}

	for e, p in numbers.items():
		string = string.replace(e, p)

	return string

def jalali_converter(time):
	time = timezone.localtime(time)
	jmonth = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند",]
	time_to_str = f"{time.year},{time.month},{time.day}"
	time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

	output = f"ساعت {time.hour}:{time.minute} ، {time_to_tuple[2]} {jmonth[time_to_tuple[1]-1]} {time_to_tuple[0]}"
	return persian_numbers_converter(output)


def jalali_converter_date(time):
	time = timezone.localtime(time)
	jmonth = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند",]
	time_to_str = f"{time.year},{time.month},{time.day}"
	time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

	output = f"{time_to_tuple[2]} {jmonth[time_to_tuple[1]-1]} {time_to_tuple[0]}"
	return persian_numbers_converter(output)