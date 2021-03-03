--homework
--查询练习
--1. 查找30多元的图书
select * from book where price>=30 and price<40;

--2．查找人民教育出版社出版的图书　
select * from book where press="人民教育出版社";

--3．查找老舍写的，中国文学出版社出版的图书
select * from book
where author="老舍" and press="中国文学出版社";

--4．查找备注不为空的图书
select * from book where comment is not null;

--5．查找价格超过60元的图书，只看书名和价格
select bname,price from book where price>60;

--6．查找鲁迅写的或者茅盾写的图书
select * from book where author="鲁迅" or author="茅盾";
select * from book where author in ("鲁迅","茅盾");


--alter 语句
增加字段
alter table hobby
add phone char(11) not null after price;

删除字段
alter table hobby drop level;

修改数据类型
alter table hobby modify phone char(16);

修改字段名
alter table hobby change phone tel char(16);


--时间数据类型
insert into marathon values
(1,"尼古拉斯赵四","1998-10-11","2021-1-1 9:18:3","2:47:56"),
(2,"托尼帕克","2000/7/7","2021-1-2 19:11:45","2:26:26"),
(3,"曹操","1999/5/7","2021-1-25 20:19:5","2:33:54");

alter table marathon
modify registration_time datetime
default now();

insert into marathon
(athlete,birthday,performance)
values
("史蒂芬","1999-1-6","2:42:56");


--alter，时间 练习
练习 使用book表
1. 将呐喊的价格修改为45元
update book set price=45 where bname="呐喊";

2. 增加一个字段出版时间 类型为 date 放在价格后面
alter table book
add publish_time date after price;

3. 修改所有老舍的作品出版时间为 2018-10-1
update book set publish_time="2018-10-1"
where author="老舍";

4. 修改所有中国文学出版社出版的但是不是老舍的作品出版时间为 2020-1-1
update book set publish_time="2020-1-1"
where author!="老舍" and press="中国文学出版社";

5. 修改所有出版时间为Null的图书 出版时间为 2019-10-1
update book set publish_time="2019-10-1"
where publish_time is null;

6. 所有鲁迅的图书价格增加5元
update book set price=price+5
where author="鲁迅";

7. 删除所有价格超过70元或者不到40元的图书
delete from book where price not between 40 and 70;


--高级查询语句
模糊查询
select * from class
where name like "A%";

select * from class
where name like "___";

select * from hobby
where hobby like "%sing%";

重命名
select name as 姓名,score as 分数
from class as 班级;

select name,score from class as c
where c.score > 90;

select name 姓名,score 分数
from class 班级;

排序
select * from class order by score;

select * from class order by score desc;

select * from class where sex='m'
order by score desc;

select * from class
order by age desc,score desc;

限制操作数量
select * from class
where sex="m" limit 2;

update class set score=60
where score<60 limit 1;

select * from class where sex="m"
order by score desc
limit 1;

select * from class where sex='m'
order by score desc
limit 1 offset 2;

联合查询
select * from class where sex='m'
union
select * from class where score > 90;

select * from class where sex='m'
union all
select * from class where score > 90;

select name,age,sex from class where sex='m'
union all
select name,age,score from class where score > 90;

select name,age,score from class where score>90
union
select name,hobby,price from hobby;

子查询
select * from
(select * from class where sex='m') as man
where score >=85;

select * from class
where score >
(select score from class
where name="Tom");

select * from class
where name in
(select name from hobby);


--高级查询练习
1. 查找所有蜀国人信息，按照攻击力排名
select * from sanguo
where country="蜀"
order by attack desc;

2. 将赵云攻击力设置为360，防御设置为70
update sanguo set attack=360,defense=70
where name="赵云";

3. 吴国英雄攻击力超过300的改为300，最多改2个
update sanguo set attack=300
where country="吴" and attack>300
limit 2;

4. 查找攻击力超过200的魏国英雄名字和攻击力并显示为姓名， 攻击力
select name as 姓名,attack as 攻击力
from sanguo
where country="魏" and attack>200;

5. 所有英雄按照攻击力降序排序，如果相同则按照防御升序排序
select * from sanguo
order by attack desc,defense;

6. 查找名字为3字的
select * from sanguo where name like "___";

7. 查找攻击力比魏国最高攻击力的人还要高的蜀国英雄
select * from sanguo
where attack > (select attack
from sanguo
where country="魏"
order by attack desc
limit 1)
and country="蜀";

8. 找到魏国防御力排名2-3名的英雄
select * from sanguo where country="魏"
order by defense
limit 2 offset 1;

9. 查找所有女性角色中攻击力大于180的和男性中攻击力小于250的
select * from sanguo where gender="女" and attack > 180
union
select * from sanguo where gender="男" and attack < 250;


聚合操作

聚合函数演示：
select avg(attack) from sanguo
where country="蜀";

select country,avg(attack),avg(defense)
from sanguo
where country="蜀";

select count(*) from sanguo
where country="蜀";

聚合分组演示:
 select country,avg(attack)
 from sanguo
 group by country;

--每个国家男性英雄的平均攻击
select country,avg(attack)
 from sanguo
 where gender="男"
 group by country;

--多字段分组
select country,gender,count(*) as 人数
from sanguo
group by country,gender;


聚合筛选
select country,avg(attack)
from sanguo
group by country
having avg(attack) > 250;

聚合去重
select distinct country from sanguo;

select count(distinct country) from sanguo;


聚合操作练习
1. 统计每位作家出版图书的平均价格
select author,avg(price)
from book
group by author;

2. 统计每个出版社出版图书数量
select press,count(*)
from book
group by press;

3. 查看总共有多少个出版社
select count(distinct press) from book;

4. 筛选出那些出版过超过50元图书的出版社，
并按照其出版图书的平均价格降序排序
select press,avg(price)
from book
group by press
having max(price) > 50
order by avg(price) desc;

5. 统计同一时间出版图书的最高价格和最低价格
select publish_time,max(price),min(price)
from book
group by publish_time;

索引操作
create table index_test(
id int auto_increment,
name varchar(30),
primary key(id),
index nameIndex(name)
);

添加索引
create unique index nameIndex
on class(name);







