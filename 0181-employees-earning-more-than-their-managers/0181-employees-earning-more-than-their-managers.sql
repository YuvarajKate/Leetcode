# Write your MySQL query statement below
select ee.name as Employee from employee e join employee ee
on e.id=ee.managerId
where e.salary<ee.salary;