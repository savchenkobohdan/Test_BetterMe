import sqlite3


con = sqlite3.connect('report_db.db')

cur = con.cursor()

# Tables creation
data = cur.executemany('''CREATE TABLE `Applications` (
	`id` INT NOT NULL,
	`App_name` VARCHAR(255),
	PRIMARY KEY (`id`)
);

CREATE TABLE `Subscriptions` (
	`id` INT NOT NULL,
	`app_id` INT,
	`name` VARCHAR(255),
	`group` INT NOT NULL,
	`duration` VARCHAR(255) NOT NULL,
	`date` DATE NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Subscriber` (
	`id` INT NOT NULL,
	`country` VARCHAR(255) NOT NULL ,
	`device` VARCHAR(255) NOT NULL ,
	`reset` VARCHAR(255) NOT NULL ,
	`Refund` VARCHAR(255) NOT NULL,
	`purchase_date` DATE NOT NULL,
	`units` INT NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `SubscriptionSubscriber` (
	`id` INTEGER PRIMARY KEY,
	`subscriber` INT NOT NULL ,
	`subscription` INT NOT NULL ,
	`customer_currency` VARCHAR(255) NOT NULL ,
	`customer_price` DECIMAL NOT NULL ,
	`proceeds_currency` VARCHAR(255) NOT NULL ,
	`opt_in_duation` VARCHAR(255) NOT NULL ,
	`introductory_price_type` VARCHAR(255) NOT NULL ,
	`introductory_price_duration` VARCHAR(255) NOT NULL ,
	`developer_proceeds` DECIMAL NOT NULL,
	`preserved_pricing` VARCHAR(255) NOT NULL,
	`preserved_reason` VARCHAR(255) NOT NULL ,
	`client` TEXT NOT NULL
);''')

con.commit()

con.close()