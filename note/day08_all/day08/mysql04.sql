-- homework （见E-R图）
-- book表 拆分 为三个表
-- 图书  出版社   作家
--
-- 分别设计这三张表和表与表之间的
-- 关系
-- 先画出 E-R图，然后再写出语句

create table author(
id int primary key auto_increment,
name varchar(30),
age tinyint,
comment text
);

create table press(
id int primary key auto_increment,
pname varchar(30),
address varchar(256),
tel char(16)
);

create table books(
id char(20) primary key,
bname varchar(20),
price float,
author_id int,
press_id int,
foreign key (author_id) references author(id),
foreign key (press_id) references press(id)
);

create table press_author(
id char(20) primary key,
author_id int,
press_id int,
foreign key (author_id) references author(id),
foreign key (press_id) references press(id)
);





视图：
create view good_student_view as
select * from class where score>80;

create view student_hobby_view as
select c.name,c.score,h.hobby,h.price
from class as c,hobby as h
where c.name=h.name;

alter view good_student_view as
select name,age,score from class
where score>85;


自定义函数

delimiter $$

create function st() returns int
begin
    update class set score=99 where id=1;
    delete from class where sex='o';
    return (select age from class where name="Abby");
end $$
delimiter ;


局部变量
delimiter $$
create function st2() returns int
begin
    declare a int;
    declare b int;
    set a=(select score from class where name="Lily");
    select score from class where name="Abby" into b;
    return a-b;
end $$
delimiter ;


函数参数
delimiter $$
create function st3(name1 varchar(30))
returns int
begin
 return (select score from class
 where name=name1);
end $$
delimiter ;


练习01：
编写一个函数，传入两个学生姓名
返回这两个学生分数之差
delimiter $$
create function queryScore(name1 varchar(30),name2 varchar(30))
returns int
begin
    declare score_1 int;
    declare score_2 int;
    set score_1=(select score from class where name=name1);
    set score_2=(select score from class where name=name2);
    return score_1-score_2;
end $$
delimiter ;

存储过程
delimiter $$
create procedure st()
begin
    update class set score=100 where id=1;
    select * from class order by score desc;
end $$
delimiter ;

call st();

存储过程参数
create procedure st1(inout a int)
begin
   select * from class where id=a;
   set a=10000;
end $$

set @num=10;
call(@num);


delimiter $$

create procedure p_out ( OUT num int )
begin
    select num;
    set num=100;
    select num;
end$$

delimiter ;

set @num=10;
call p_out(@num)

练习02
编写一个存储过程，传入一个学生的ID
将该学生的分数改为98分，然后删除
比这个学生分数还高的所有人

create procedure delete_stu(in uid int)
begin
    update class set score=98 where id=uid;
    delete from class where score>98;
end




