import sqlite3


con = sqlite3.connect('report_db.db')

cur = con.cursor()

query1 = cur.execute('''Select id, duration from Subscriptions where id = 1447369566;
''')

query2 = cur.execute('''Select ss.name
from Subscriptions ss join Applications app
on ss.app_id = app.id
where app.id = 1363010081;
''')

query3 = cur.execute('''Select app.App_name, sum(developer_proceeds) 
from SubscriptionSubscriber ss join Subscriptions sub
on ss.subscription = sub.id
join Applications app on sub.app_id = app.id
where sub.date between '2019-02-02' and '2019-02-10'
group by app.App_name
order by 1 desc
limit 1
''')

query4 = cur.execute('''Select cast(round(cast(count(distinct subscriber) as real)/(Select count(subscriber)
from SubscriptionSubscriber where introductory_price_type != '-')*100,2) as varchar) || '%' as 'Conversion'
from SubscriptionSubscriber where introductory_price_type != '-' and subscriber in (Select distinct subscriber
from SubscriptionSubscriber where introductory_price_type = '-') and subscription = --id;
''')


results = query3.fetchall()
print(results)

con.commit()

con.close()
