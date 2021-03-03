外键约束 示例
insert into dept values
(1,"技术部"),
(2,"销售部"),
(3,"市场部"),
(4,"行政部"),
(5,'财务部'),
(6,'总裁办公室');


insert into person values
(1,"Lily",29,20000,2),
(2,"Tom",27,16000,1),
(3,"Joy",30,28000,1),
(4,"Emma",24,8000,4),
(5,"Abby",28,17000,3),
(6,"Jame",32,22000,3);

符合语法但是不合理
insert into person values
(7,"Tonny",26,15000,7);

添加外键约束
alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id);

级联动作
alter table person
drop foreign key dept_fk;

alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete cascade
on update cascade;

alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete set null
on update set null;

表关系 （见笔记）

alter table athlete_item
add number tinyint;

练习01：根据所学表关系，梳理用户朋友圈表
存储内容不变，但是要重新设计关系，建立数据表

--用户表
create table user(
id int primary key auto_increment,
name varchar(30),
passwd char(64),
tel char(16)
);

--朋友圈
create table pyq(
id int primary key auto_increment,
image varchar(20),
content varchar(256),
time datetime,
address varchar(128),
user_id int,
foreign key (user_id) references user(id)
);

--点赞，评论
create table user_pyq(
id int primary key auto_increment,
u_id int,
p_id int,
comment varchar(512),
`like` bit,
foreign key(u_id) references user(id),
foreign key(p_id) references pyq(id)
);

多表查询
select c.name,c.age,c.score,h.hobby
from class as c,hobby as h;

select c.name,c.age,c.score,h.hobby
from class as c,hobby as h
where c.name = h.name;

select dept.dname,person.name,person.salary
from dept,person
where dept.id = person.dept_id;

内连接
select name,dname,salary
from person inner join  dept
on  person.dept_id=dept.id
where salary > 18000
order by salary;

左连接 （没有部门的也能找到啦）
select name,dname,salary
from person left join  dept
on  person.dept_id =dept.id
where salary > 18000
order by salary;

右连接
select dname,count(person.id)
from person right join  dept
on  person.dept_id =dept.id
group by dname;


查询操作综合练习
1. 查询每位老师教授的课程数量
select teacher.tname,count(teacher_id)
from teacher left join course
on teacher.tid = course.teacher_id
group by teacher.tname;

2. 查询学生的信息及学生所在班级信息
select sid,sname,gender,caption
from student left join class
on student.class_id = class.cid;

3. 查询各科成绩最高和最低的分数,
形式 : 课程ID  课程名称 最高分 最低分
select cid as 课程ID,cname as 课程名称,
max(number) as 最高分,min(number) as 最低分
from course left join score
on course.cid = score.course_id
group by cid,cname;

4. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select student.sid,sname,avg(number)
from student left join score
on student.sid = score.student_id
group by student.sid,sname
having avg(number) > 85;

5. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select student.sid,sname
from student left join score
on student.sid = score.student_id
where course_id=2 and number > 80;

6. 查询各个课程及相应的选修人数
select  cname,count(course_id)
from course left join score
on course.cid = score.course_id
group by cname;

7. 查询每位学生的姓名，所在班级和各科平均成绩
select sname,caption,avg(number)
from student left join class
on student.class_id = class.cid
left join score
on student.sid = score.student_id
group by sname,caption;


视图：
create view good_student_view as
select * from class where score>80;








