# Combine first name and last name into a single "Full name"

full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()

print(full_name('     leonard', 'REEPLE'))
