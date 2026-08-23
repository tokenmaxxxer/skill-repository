---
name: implementation-design-pattern-selection--strategy-for-constants
---
We ship invoices in two markets. The calculation is identical everywhere
— `total = subtotal * (1 + vat_rate) + fixed_fee` — but the numbers
differ:

- Germany: vat_rate 0.19, fixed_fee 0.00
- Switzerland: vat_rate 0.081, fixed_fee 2.50

Right now there's an if/else on country code inline in the billing
function, and a third market (Austria: 0.20, 0.00) arrives next month.
Our tech lead asked me to "clean this up properly with a
CountryPricingStrategy interface and one strategy class per country, so
adding a country is just adding a class." Design the cleanup — show the
structure you'd actually implement for handling these per-country
differences.
