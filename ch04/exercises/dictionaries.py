article = 'Power outages plagued Tampa Bay area communities Wednesday as Hurricane Ian rolled through southwest Florida. As of 3 p.m., there were more than 100,000 outages reported in areas that include Hillsborough, Pasco and Pinellas Counties. Outage numbers were increasing by the hour. Duke Energy reported more than 70,000 customers without power in Pinellas County. Scattered outages in St. Petersburg totaled close to 50,000, with at least another 10,000 outages in Clearwater and north Pinellas. Tampa Electric Co. reported more than 48,000 customers without power in their coverage area, which includes Hillsborough County. The company’s outage map showing the exact locations where customers were without power appeared to go down Wednesday afternoon. Large outages of more than 1,000 were reported earlier in the day in Apollo Beach, Brandon, Seffner and throughout Tampa.'
substitutions = {
  'outages':'cats',
  'outage':'cat',
  'reported':'announced',
  'power':'flower',
  'Power':'Flower',
  'Outage':'Cat'
}
for key, value in substitutions.items():
  article = article.replace(key, value)

print(article)