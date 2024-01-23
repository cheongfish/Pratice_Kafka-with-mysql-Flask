CREATE TABLE test (
  id BIGINT auto_increment primary key,
  user_id BIGINT not null,
  title varchar(100) not null,
  done boolean not null
);
