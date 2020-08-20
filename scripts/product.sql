CREATE TABLE padawans02.product (
	origin varchar(16) NOT NULL,
	created_at TIMESTAMP DEFAULT current_timestamp,
	updated_at TIMESTAMP DEFAULT current_timestamp ON UPDATE current_timestamp,
	id varchar(36) NOT NULL,
	sku varchar(16) NOT NULL,
	seller_id varchar(36) NOT NULL,
	product_code varchar(64) NOT NULL,
	gtin varchar(14) NOT NULL,
	name varchar(128) NOT NULL,
	status varchar(64) NOT NULL,
	brand varchar(128) NOT NULL,
	description TEXT NOT NULL,
	free_shipping BOOL NOT NULL,
	group_id varchar(16) NOT NULL,
	tax_information_id varchar(36) DEFAULT '',
	approved BOOL NOT NULL,
	rejection_reasons TEXT NULL,
	active BOOL NOT NULL,
	part_number varchar(32) NOT NULL,
	in_campaign BOOL NOT NULL,
	odin varchar(64) NOT NULL,
	waiting_invoice BOOL NOT NULL,
	controller_gtin_id varchar(36) DEFAULT '',
	currency varchar(3) NOT NULL,
	offer DECIMAL(10, 2) NOT NULL,
	price DECIMAL(10, 2) NOT NULL,
	inactive_reason varchar(64) DEFAULT '',
	CONSTRAINT product_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=latin1
COLLATE=latin1_swedish_ci;
