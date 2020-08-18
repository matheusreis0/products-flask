CREATE TABLE padawans02.product (
	origin varchar(16) DEFAULT origin NOT NULL,
	created_at TIMESTAMP NOT NULL,
	updated_at TIMESTAMP NOT NULL,
	id BINARY(16) NOT NULL,
	sku varchar(16) NOT NULL,
	seller_id BINARY(16) NOT NULL,
	product_code varchar(64) NOT NULL,
	gtin varchar(14) NOT NULL,
	name varchar(128) NOT NULL,
	status varchar(64) NOT NULL,
	brand varchar(128) NOT NULL,
	description TEXT NOT NULL,
	free_shipping BOOL NOT NULL,
	group_id varchar(16) NOT NULL,
	tax_information_id BINARY(16) NULL,
	approved BOOL NOT NULL,
	rejection_reasons TEXT NULL,
	active BOOL NOT NULL,
	part_number varchar(32) NOT NULL,
	in_campaign BOOL NOT NULL,
	odin varchar(64) NOT NULL,
	waiting_invoice BOOL NOT NULL,
	controller_gtin_id BINARY(16) NULL,
	currency varchar(3) NOT NULL,
	offer NUMERIC NOT NULL,
	price NUMERIC NOT NULL,
	inactive_reason varchar(64) NULL,
	CONSTRAINT product_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=latin1
COLLATE=latin1_swedish_ci;
