DO 
$$
BEGIN 
   CREATE TABLE IF NOT EXISTS vendor(
		id 				BIGSERIAL PRIMARY KEY,
		first_name 		VARCHAR NOT NULL,
		last_name		VARCHAR,
		email			VARCHAR UNIQUE NOT NULL,
		phone_no		VARCHAR UNIQUE NOT NULL,
		address1		VARCHAR NOT NULL,
		address2		VARCHAR,
		city			VARCHAR NOT NULL,
		state			VARCHAR NOT NULL,
		postal_code		INT NOT NULL,
		country			VARCHAR NOT NULL,
		description		VARCHAR
   );
   
   CREATE INDEX IF NOT EXISTS vendor_email_index ON vendor(email);
   CREATE INDEX IF NOT EXISTS vendor_phone_no_index ON vendor(phone_no);
   
   CREATE TABLE IF NOT EXISTS customer(
		id 				BIGSERIAL PRIMARY KEY,
		first_name 		VARCHAR NOT NULL,
		last_name		VARCHAR,
		email			VARCHAR UNIQUE NOT NULL,
		phone_no		VARCHAR UNIQUE NOT NULL,
		address1		VARCHAR NOT NULL,
		address2		VARCHAR,
		city			VARCHAR NOT NULL,
		state			VARCHAR NOT NULL,
		postal_code		INT NOT NULL,
		country			VARCHAR NOT NULL
   );
   
   CREATE INDEX IF NOT EXISTS customer_email_index ON customer(email);
   CREATE INDEX IF NOT EXISTS customer_phone_no_index ON customer(phone_no);
   
   CREATE TABLE IF NOT EXISTS product(
		id 				BIGSERIAL PRIMARY KEY,
		name			VARCHAR NOT NULL,
		vendor_id 		BIGINT REFERENCES vendor(id) NOT NULL,
		description		VARCHAR NOT NULL,
		qty_in_stock	INT NOT NULL,
		price			INT NOT NULL,
		discount		INT DEFAULT 0 CHECK(discount BETWEEN 0 AND 100),
		rating			INT DEFAULT 0 CHECK(rating BETWEEN 0 AND 5),
		review			VARCHAR
   );
   
   CREATE INDEX IF NOT EXISTS product_name_index ON product(name);
   
   CREATE TABLE IF NOT EXISTS vendor_product(
		vendor_id 		BIGINT REFERENCES vendor(id),
		product_id		BIGINT REFERENCES product(id),
		PRIMARY KEY (vendor_id, product_id)
   );
   
   CREATE TABLE IF NOT EXISTS order_status(
		id 		INT PRIMARY KEY,
		status	VARCHAR UNIQUE NOT NULL
   );
   
   INSERT INTO order_status (id, status) VALUES (1, 'PENDING'), 
												(2, 'PROCESSING'), 
												(3, 'COMPLETED'), 
												(4, 'CANCELED') 
												ON CONFLICT DO NOTHING;
												
	CREATE TABLE IF NOT EXISTS payment(
		id 				BIGSERIAL PRIMARY KEY,
		date			TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
		total_amount 	NUMERIC(19, 2) NOT NULL,
		payment_type	VARCHAR NOT NULL
   );
   
   CREATE TABLE IF NOT EXISTS orders(
		id 				BIGSERIAL,
		customer_id		BIGINT REFERENCES customer(id) NOT NULL,
		status_id		INT REFERENCES order_status(id),
		order_date		TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,
		shipping_date	TIMESTAMP WITH TIME ZONE,
		payment_id		BIGINT REFERENCES payment(id) NOT NULL,
		PRIMARY KEY (id, status_id)
   ) PARTITION BY LIST(status_id);
   
   CREATE TABLE IF NOT EXISTS order_completed PARTITION OF orders FOR VALUES IN (3);
   CREATE TABLE IF NOT EXISTS order_processing PARTITION OF orders FOR VALUES IN (2);
   CREATE TABLE IF NOT EXISTS order_pending PARTITION OF orders FOR VALUES IN (1);
   
   CREATE INDEX IF NOT EXISTS order_customer_id_index ON orders(customer_id);
   
   CREATE INDEX IF NOT EXISTS order_payment_id_index ON orders(payment_id); 
   
   
   CREATE TABLE IF NOT EXISTS order_product(
		order_id 		BIGINT NOT NULL,
		order_status_id	INT NOT NULL,
		product_id		BIGINT REFERENCES product(id),
		quantity		INT NOT NULL,
		price			NUMERIC(19, 2) NOT NULL,
		FOREIGN KEY (order_id, order_status_id) REFERENCES orders(id, status_id),
		PRIMARY KEY (order_id, product_id)
   );
   
END
$$