violation = {"123","456","233","444","667","996","855"}

unpaid_n ={"444","123","667"}

paid_violation ={"999","456","444"}



bad_humans =  violation.intersection(unpaid_n)
not_quite_bad = violation.difference(unpaid_n)
some_bad = paid_violation.intersection(unpaid_n)
very_bad =

print("Не заплатили налоги и нарушили правила:")
for i in bad_humans:
    print ("Номер " + i)

print("Заплатили налоги и нарушили правила:")
for i in not_quite_bad:
    print ("Номер " + i)

print("нарушили ПДД,оплатили штраф, но не оплатили налоги")
for i in some_bad:
    print("Номер "+ i)

print("нарушили ПДД, но не оплатил штраф.")
for i in violation:
    print("Номер" + i)
