create table test (one INT);
insert into test values (1);
select * from test;

# mysql -u rrballenger17 -h mysql-instance1.cnpm69av64x3.us-east-1.rds.amazonaws.com -p(password here, 9 character one)
# use theDatabase;

CREATE TABLE doodads (
	doodad_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	doodad_name VARCHAR(40) NOT NULL, 
	doodad_price DECIMAL(10,2) UNSIGNED NOT NULL, 
	doodad_on_hand MEDIUMINT UNSIGNED NOT NULL DEFAULT 0, 
	PRIMARY KEY (doodad_id),
	INDEX (doodad_name),
	INDEX (doodad_price),
	INDEX (doodad_on_hand)
);

CREATE TABLE orders (
order_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
doodad_id INT UNSIGNED NOT NULL,
PRIMARY KEY (order_id),
INDEX (doodad_id)
);


INSERT INTO doodads VALUES 
(NULL, 'a', 19.95, 20),
(NULL, 'b', 15.00, 10),
(NULL, 'c', 22.95, 5),
(NULL, 'd', 10.00, 15);


DELIMITER $$

CREATE TRIGGER update_qty_insert
AFTER INSERT ON orders FOR EACH ROW
BEGIN
UPDATE doodads SET
doodad_on_hand=doodad_on_hand-1
WHERE doodads.doodad_id=NEW.doodad_id;
END $$



INSERT INTO orders (doodad_id) VALUES (3)


CREATE TRIGGER update_qty_delete
BEFORE DELETE ON orders FOR EACH ROW
BEGIN 
UPDATE doodads SET
doodad_on_hand = doodad_on_hand + 1
WHERE doodads.doodad_id = OLD.doodad_id;

END $$

# DROP TRIGGER update_qty_insert
# DROP TRIGGER update_qty_delete

DELIMITER ;

INSERT INTO orders (doodad_id) VALUES (1), (2), (3), (1), (1);

Select * from doodads;

DELETE FROM orders WHERE order_id=4;

SELECT * from doodads;
















