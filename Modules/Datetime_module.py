
# %% codecell
import datetime

# %% markdown
# There are two types of datetimes, the "naive" datetime where the datetime does not determine timezones, daylight savings etc and  the "aware" datetimes, where all these information are available.<br>
# The normal datetime format in computers is YYYY/MM/DD .

# %% markdown
# We start by creating a date. We make sure we pass integers with no leading zeroes in our month and day values or else we get an error.
# %% codecell
dte = datetime.date(2020, 4, 6)
print(dte)

# %% markdown
# If we want to see our local date we use the .today method, which gives us a date object.
# %% codecell
tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)

# %% markdown
# If we want the day of the week of a given date, we can use the .weekday and the .isoweekday methods. The difference between those 2 is that for .weekday Monday=0 && Sunday=6 and for the .isoweek day Monday=1 && Sunday=7.
# %% codecell
print(tday.weekday())
print(tday.isoweekday())

# %% markdown
# For the difference between two dates or times we use timedeltas.
# Say for example we want the date one week from now either passed or will follow. We execute the following:
# %% codecell
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

# %% markdown
# For finding out the remaining days until an event occurs we can use simple arithmetic calculations. And since we have datetime objects we can access certain attributes.
# %% codecell
event_day = datetime.date(2020, 7, 21)
till_event = event_day - tday
print(till_event)
print(till_event.days)
print(till_event.total_seconds())

# %% markdown
# The time objects are of the format hh/minmin/ss/μs.
# %% codecell
tme = datetime.time(19, 30, 45, 1000)
print(tme)

# %% markdown
# If we want both the datetime and the time we use the .datetime method. Which grants us access to all the possible information that we want.
# %% codecell
dte_tme = datetime.datetime(2020, 4, 6, 19, 30, 45, 1000)
print(dte_tme)
print(dte_tme.date())
print(dte_tme.time())
print(dte_tme.year)
print(dte_tme.month)
print(dte_tme.day)
print(dte_tme.hour)
print(dte_tme.minute)
print(dte_tme.second)

# %% markdown
# It also allows us to have arithmetic computations just like any other date time object.
# %% codecell
print(dte_tme + tdelta)
print(dte_tme - tdelta)

# %% markdown
# We can also use some other alternative constructors, for the definition go to the OOP turorials, for the .datetime method.<br>
# <li> .today(), returns the current local datetime with a time zone of none.</li><br>
# <li> .now(), gives us the option for passing a timezone. If we do not pass any, it retuns the same value as the .today()</li><br>
# <li> .utcnow(), gives us the current UTC date and time without any timezone information, as a native datetime object.</li><br>
# %% codecell
dte_today = datetime.datetime.today()
dte_now = datetime.datetime.now()
dte_utcnow = datetime.datetime.utcnow()
print(dte_today)
print(dte_now)
print(dte_utcnow)

# %% markdown
# ## Manipulating datetime objects with pytz
# %% codecell
import pytz

# %% markdown
# It is always recommented to use time aware UTC times when using the pytz module. To make a datetime object timezone aware we create it as follows:
# %% codecell
dt_utc_aware = datetime.datetime(2020, 4, 6, 19, 30, 45, tzinfo=pytz.UTC)
print(dt_utc_aware)

# %% markdown
# Which is the same as the date time object below:
# %% codecell
dte_now_utc = datetime.datetime.now(tz=pytz.UTC)
print(dte_now_utc)

# %% markdown
# When we want to conver UTC time to our timezone we can use the .astimezone, method.
# %% codecell
dte_loc = dte_now_utc.astimezone(pytz.timezone('Europe/Athens'))
print(dte_loc)

# %% markdown
# For finding out all the time zones in the pytz module we perform the following query:
# %% codecell
for tz in pytz.all_timezones:
    print(tz)

# %% markdown
# Making a "naive" datetime object, date time aware with the .localize, method and converting it to another timezone.
# %% codecell
dte_naiv = datetime.datetime.now()
dte_tizn = pytz.timezone('Europe/Athens')
dte_awar = dte_tizn.localize(dte_naiv)
print(dte_awar)
dte_conv = dte_awar.astimezone(pytz.timezone('Iran'))
print(dte_conv)

# %% markdown
# ## Formating Datetime objects<br>
# Isoformat:
# %% codecell
print(dte_awar.isoformat())

# %% markdown
# Converting a datetime object to a string with the .strftime, method.
# %% codecell
print(dte_awar.strftime('%d %B, %Y'))

# %% markdown
# Converting a string to a datetime object with the .strptime, method.
# %% codecell
dte_str = 'April 06, 2020'
dte_str_conv = datetime.datetime.strptime(dte_str, '%B %d, %Y')  # Passing the datetime format the string has.
print(dte_str_conv)
