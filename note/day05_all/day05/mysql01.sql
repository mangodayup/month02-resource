--创建 class 表
create table class (
id int primary key auto_increment,
name varchar(30) not null,
age tinyint unsigned not null,
sex enum("m","w","o")  comment " 性别",
score float default 0
);

--兴趣爱好
create table `hobby`(
`id` int primary key auto_increment,
`name` varchar(30) not null,
`hobby` set("sing","dance","draw") comment "选择兴趣爱好",
`level` char(2),
`price` decimal(7,2),
`remark` text
);

--插入操作
insert into class values
(1,"Lily",18,'w',76.5),
(2,"Lucy",18,'w',83);

insert into class
(name,age,score)
values
("Tom",17,91),
("Alex",19,72);

insert into hobby
(name,hobby,level,price,remark)
values
("Joy","sing,dance","A",65800,"骨骼惊奇，练舞奇才"),
("Emma","sing","B",16800,"天籁之音");

insert into hobby
(name,hobby,level,price)
values
("Abby","draw","C",8800.009),
("Jame","draw,dance","B",49800.1);


--练习01：
--创建一个数据库 books  设置utf8格式
create database books charset=utf8;

--在其中创建一个数据表 book
--字段： id  书名  作者  出版社  价格  备注
use books;

create table book(
id int primary key auto_increment,
bname varchar(30) not null,
author varchar(30),
press varchar(50),
price float default 0,
comment text
);

--向其中插入一些数据
--作者： 老舍  沈从文  钱钟书  鲁迅 ....
--出版社 ： 中国文学  人民教育  机械工业
--价格 ： 30 - 120
insert into book (bname,author,press,price,comment)
values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",43,"你是祥子么？"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","人民教育出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","中国文学出版社",53,"好时光"),
("围城","钱钟书","中国文学出版社",44,"你心中的围城是什么");

insert into book (bname,author,press,price)
values
("林家铺子","茅盾","机械工业出版社",51),
("巨人传","忘了","人民教育出版社",47);


