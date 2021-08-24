import sqlite3
import pandas as pd
from forex_python.converter import CurrencyRates


con = sqlite3.connect('report_db.db')

cur = con.cursor()
file_names = ('20190201', '20190202', '20190203', '20190204', '20190205', '20190206', '20190207', '20190208', '20190209'
              , '20190210')
path = "C:\\Test_Genesis\\BetteME\Data\\"

c = CurrencyRates()

# DataBase filling
for file_name in file_names:

#   Conversion of ID's from data to the 'int' type in Python
    cur.executemany(f'''insert or ignore into Applications values (?, ?)
    ''', [[int(record[0])]+list(record)[1:] for record in pd.read_csv(f"{path}{file_name}.txt", delimiter="\t").drop_duplicates("App Apple ID")[["App Apple ID", "App Name"]].to_records(index=False)])

    data = cur.executemany(f'''insert or ignore into Subscriptions values (?, ?, ?, ?, ?, ?)
    ''', [[int(record[0])]+[int(record[1])]+[str(record[2])]+[int(record[3])]+list(record)[4:]for record in
          pd.read_csv(f"{path}{file_name}.txt", delimiter="\t").drop_duplicates("Subscription Apple ID")[["Subscription Apple ID",
                                                                "App Apple ID", "Subscription Name",
                                                                "Subscription Group ID", "Subscription Duration",
                                                                "Event Date"]].to_records(index=False)])

    data = cur.executemany(f'''insert or ignore into Subscriber values (?, ?, ?, ?, ?, ?, ?)
        ''', [[int(record[0])]+list(record)[1:-1]+[int(record[-1])] for record in (pd.read_csv(f"{path}{file_name}.txt", delimiter="\t")[
            ["Subscriber ID", "Country", "Device", "Subscriber ID Reset",
            "Refund", "Purchase Date", "Units"]].fillna("-").to_records(index=False))])

    df = pd.read_csv(f"{path}{file_name}.txt", delimiter="\t")
    df.replace(" ", "-", inplace=True)

#   Converting currenciens to 'USD'
    list_rate = []
    for i in range(0, len(df)):
        try:
            list_rate.append(c.get_rate('USD', df["Proceeds Currency"][i]))
        except:
            list_rate.append(1)

    se = pd.Series(list_rate)
    df['USD'] = se.values
    df['Developer Proceeds'] = df['Developer Proceeds']*df['USD']

    data = cur.executemany(f'''insert or ignore into SubscriptionSubscriber values (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', [[int(record[0])]+[int(record[1])]+list(record)[2:] for record in df[["Subscriber ID",
        "Subscription Apple ID", "Customer Currency", "Customer Price", "Proceeds Currency", "Marketing Opt-In Duration",
        "Introductory Price Type", "Introductory Price Duration", "Developer Proceeds", "Preserved Pricing",
        "Proceeds Reason", "Client"]].fillna("-").to_records(index=False)])


con.commit()

con.close()
