CREATE TABLE my_test (
    client_id character varying(36) NOT NULL,
    value character varying(255),
    last_changed  character varying(255)
);

INSERT INTO my_test (client_id, value, last_changed)
VALUES ('1234','2000','1985');
